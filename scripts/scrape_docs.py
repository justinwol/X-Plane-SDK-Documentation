#!/usr/bin/env python3
"""
X-Plane SDK Documentation Scraper

This script handles the automated scraping of X-Plane SDK documentation
from official sources. It extracts content, handles pagination, and
saves raw documentation data for further processing.

Purpose:
- Scrape X-Plane SDK documentation from web sources
- Handle different documentation formats and structures
- Save raw content for processing pipeline
- Manage rate limiting and respectful scraping practices

Usage:
    python scrape_docs.py [options]

Dependencies:
    - requests: For HTTP requests
    - beautifulsoup4: For HTML parsing
    - concurrent.futures: For parallel processing
"""

import json
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Comment

from change_detector import calculate_content_hash, load_existing_hashes, save_content_hashes
from process_content import read_sdk_map_file

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraping.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
RATE_LIMIT_DELAY = 0.3  # 0.3 seconds between requests
MAX_RETRIES = 3
TIMEOUT = 30
MAX_WORKERS = 5  # Conservative thread count for respectful scraping

# File paths
PROJECT_ROOT = Path(__file__).parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "raw_data"
SCRAPED_CONTENT_FILE = RAW_DATA_DIR / "scraped_content.json"
CATEGORIZED_URLS_FILE = RAW_DATA_DIR / "categorized_urls.json"

# Request headers to appear as a legitimate browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def scrape_single_url(url: str) -> Dict[str, Union[str, int, bool, Dict]]:
    """
    Extract content from one URL using requests and BeautifulSoup.
    
    Args:
        url: URL to scrape
        
    Returns:
        Dict containing:
        - url: Original URL
        - content: Extracted main content (HTML)
        - raw_html: Full page HTML
        - status_code: HTTP status code
        - success: Boolean indicating success
        - error: Error message if failed
        - metadata: Additional information (title, description, etc.)
        - code_examples: List of extracted code examples
        - timestamp: When the content was scraped
    """
    result = {
        'url': url,
        'content': '',
        'raw_html': '',
        'status_code': 0,
        'success': False,
        'error': None,
        'metadata': {},
        'code_examples': [],
        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    
    session = requests.Session()
    session.headers.update(HEADERS)
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.debug(f"Scraping {url} (attempt {attempt + 1}/{MAX_RETRIES})")
            
            response = session.get(url, timeout=TIMEOUT)
            result['status_code'] = response.status_code
            result['raw_html'] = response.text
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract main content
                result['content'] = extract_main_content(soup)
                
                # Extract metadata
                result['metadata'] = extract_metadata(soup, url)
                
                # Extract code examples
                result['code_examples'] = extract_code_examples(soup)
                
                result['success'] = True
                logger.debug(f"Successfully scraped {url}")
                break
                
            elif response.status_code == 404:
                result['error'] = f"Page not found (404): {url}"
                logger.warning(result['error'])
                break  # Don't retry 404s
                
            elif response.status_code == 403:
                result['error'] = f"Access forbidden (403): {url}"
                logger.warning(result['error'])
                break  # Don't retry 403s
                
            else:
                result['error'] = f"HTTP {response.status_code}: {url}"
                logger.warning(result['error'])
                
        except requests.exceptions.Timeout:
            result['error'] = f"Timeout after {TIMEOUT}s: {url}"
            logger.warning(result['error'])
            
        except requests.exceptions.ConnectionError:
            result['error'] = f"Connection error: {url}"
            logger.warning(result['error'])
            
        except requests.exceptions.RequestException as e:
            result['error'] = f"Request error: {e}"
            logger.warning(result['error'])
            
        except Exception as e:
            result['error'] = f"Unexpected error: {e}"
            logger.error(result['error'])
            
        # Exponential backoff for retries
        if attempt < MAX_RETRIES - 1:
            delay = (2 ** attempt) * 1.0  # 1s, 2s, 4s
            logger.debug(f"Retrying {url} in {delay}s...")
            time.sleep(delay)
    
    return result


def extract_main_content(soup: BeautifulSoup) -> str:
    """
    Get main documentation content from BeautifulSoup object.
    
    Args:
        soup: BeautifulSoup object of the page
        
    Returns:
        str: Cleaned main content HTML
    """
    # Remove unwanted elements
    unwanted_selectors = [
        'nav', 'header', 'footer', 'aside',
        '.navigation', '.nav', '.sidebar', '.menu',
        '.advertisement', '.ads', '.ad',
        '.social', '.share', '.comments',
        'script', 'style', 'noscript',
        '.breadcrumb', '.breadcrumbs',
        '.search', '.search-form',
        '.pagination', '.pager'
    ]
    
    for selector in unwanted_selectors:
        for element in soup.select(selector):
            element.decompose()
    
    # Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    
    # Try to find main content area using common patterns
    main_content_selectors = [
        'main',
        'article',
        '.content',
        '.main-content',
        '.documentation',
        '.doc-content',
        '#content',
        '#main',
        '.entry-content',
        '.post-content',
        '.page-content'
    ]
    
    main_content = None
    for selector in main_content_selectors:
        main_content = soup.select_one(selector)
        if main_content:
            logger.debug(f"Found main content using selector: {selector}")
            break
    
    # If no main content area found, use body but remove more elements
    if not main_content:
        main_content = soup.find('body')
        if main_content:
            # Remove additional unwanted elements from body
            for selector in ['.header', '.footer', '.nav-wrapper']:
                for element in main_content.select(selector):
                    element.decompose()
    
    # If still no content, use the whole soup
    if not main_content:
        main_content = soup
    
    # Clean up the content
    if main_content:
        # Remove empty paragraphs and divs
        for tag in main_content.find_all(['p', 'div']):
            if not tag.get_text(strip=True) and not tag.find(['img', 'video', 'audio']):
                tag.decompose()
        
        # Clean up whitespace in text nodes
        for text_node in main_content.find_all(string=True):
            if text_node.parent.name not in ['pre', 'code']:
                cleaned_text = re.sub(r'\s+', ' ', text_node).strip()
                text_node.replace_with(cleaned_text)
        
        return str(main_content)
    
    return ""


def extract_code_examples(soup: BeautifulSoup) -> List[Dict[str, str]]:
    """
    Find and extract code snippets from the documentation.
    
    Args:
        soup: BeautifulSoup object of the page
        
    Returns:
        List of dictionaries containing code examples with context
    """
    code_examples = []
    
    # Common selectors for code blocks
    code_selectors = [
        'pre code',
        'pre',
        '.code',
        '.highlight',
        '.codehilite',
        '.syntax',
        'code.language-c',
        'code.language-cpp',
        'code[class*="language-c"]',  # More flexible C++ selector
        '.c-code',
        '.cpp-code'
    ]
    
    for selector in code_selectors:
        code_blocks = soup.select(selector)
        
        for i, block in enumerate(code_blocks):
            code_text = block.get_text()
            
            # Skip very short code snippets (likely inline code)
            if len(code_text.strip()) < 10:
                continue
            
            # Try to determine the language
            language = 'unknown'
            
            # Check class attributes for language hints
            classes = block.get('class', [])
            for cls in classes:
                if 'language-' in cls:
                    language = cls.replace('language-', '')
                elif cls in ['c', 'cpp', 'c++', 'c-code', 'cpp-code']:
                    language = cls
            
            # Check parent classes
            if language == 'unknown' and block.parent:
                parent_classes = block.parent.get('class', [])
                for cls in parent_classes:
                    if 'language-' in cls:
                        language = cls.replace('language-', '')
                    elif cls in ['c', 'cpp', 'c++', 'highlight-c', 'highlight-cpp']:
                        language = cls
            
            # Heuristic detection for C/C++ code
            if language == 'unknown':
                c_patterns = [
                    r'\b(int|char|float|double|void|struct|typedef)\b',
                    r'\b(XP[A-Z][a-zA-Z]*)\b',  # X-Plane API functions
                    r'#include\s*[<"]',
                    r'\*\s*\w+\s*\(',  # Function pointers
                    r'\w+\s*\*\s*\w+',  # Pointer declarations
                ]
                
                for pattern in c_patterns:
                    if re.search(pattern, code_text):
                        language = 'c'
                        break
            
            # Get context (preceding heading or paragraph)
            context = ""
            prev_element = block.parent
            while prev_element and not context:
                prev_sibling = prev_element.find_previous_sibling(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
                if prev_sibling:
                    context = prev_sibling.get_text().strip()[:200]  # First 200 chars
                    break
                prev_element = prev_element.parent
            
            code_example = {
                'code': code_text.strip(),
                'language': language,
                'context': context,
                'selector_used': selector,
                'index': i
            }
            
            code_examples.append(code_example)
    
    # Remove duplicates (same code content)
    seen_codes = set()
    unique_examples = []
    for example in code_examples:
        code_hash = calculate_content_hash(example['code'])
        if code_hash not in seen_codes:
            seen_codes.add(code_hash)
            unique_examples.append(example)
    
    logger.debug(f"Extracted {len(unique_examples)} unique code examples")
    return unique_examples


def extract_metadata(soup: BeautifulSoup, url: str) -> Dict[str, str]:
    """
    Extract metadata from the page.
    
    Args:
        soup: BeautifulSoup object of the page
        url: Original URL
        
    Returns:
        Dict containing metadata
    """
    metadata = {
        'url': url,
        'domain': urlparse(url).netloc
    }
    
    # Extract title
    title_tag = soup.find('title')
    if title_tag:
        metadata['title'] = title_tag.get_text().strip()
    
    # Extract meta description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag:
        metadata['description'] = desc_tag.get('content', '').strip()
    
    # Extract main heading
    h1_tag = soup.find('h1')
    if h1_tag:
        metadata['main_heading'] = h1_tag.get_text().strip()
    
    # Extract all headings for structure
    headings = []
    for level in range(1, 7):
        for heading in soup.find_all(f'h{level}'):
            headings.append({
                'level': level,
                'text': heading.get_text().strip(),
                'id': heading.get('id', '')
            })
    metadata['headings'] = headings
    
    # Count various elements
    metadata['paragraph_count'] = len(soup.find_all('p'))
    metadata['code_block_count'] = len(soup.find_all(['pre', 'code']))
    metadata['link_count'] = len(soup.find_all('a'))
    
    # Extract function name from URL if it's an API page
    path_parts = urlparse(url).path.strip('/').split('/')
    if len(path_parts) >= 2 and path_parts[0] == 'sdk':
        metadata['api_function'] = path_parts[-1]
        metadata['api_module'] = path_parts[1] if len(path_parts) > 1 else ''
    
    return metadata


def scrape_all_urls(url_list: List[str]) -> Dict[str, Dict]:
    """
    Multi-threaded scraping with rate limiting.
    
    Args:
        url_list: List of URLs to scrape
        
    Returns:
        Dict mapping URLs to their scraped content
    """
    logger.info(f"Starting to scrape {len(url_list)} URLs with {MAX_WORKERS} workers")
    logger.info(f"Rate limit: {RATE_LIMIT_DELAY}s between requests")
    
    results = {}
    completed_count = 0
    failed_count = 0
    
    # Use ThreadPoolExecutor for concurrent scraping
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        future_to_url = {
            executor.submit(scrape_single_url, url): url 
            for url in url_list
        }
        
        # Process completed tasks
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            
            try:
                result = future.result()
                results[url] = result
                
                if result['success']:
                    completed_count += 1
                    logger.info(f"✓ [{completed_count + failed_count}/{len(url_list)}] {url}")
                else:
                    failed_count += 1
                    logger.warning(f"✗ [{completed_count + failed_count}/{len(url_list)}] {url} - {result.get('error', 'Unknown error')}")
                
                # Progress update every 50 URLs
                if (completed_count + failed_count) % 50 == 0:
                    logger.info(f"Progress: {completed_count + failed_count}/{len(url_list)} URLs processed")
                
            except Exception as e:
                failed_count += 1
                logger.error(f"✗ [{completed_count + failed_count}/{len(url_list)}] {url} - Exception: {e}")
                results[url] = {
                    'url': url,
                    'success': False,
                    'error': f"Exception during processing: {e}",
                    'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
                }
            
            # Rate limiting - sleep between requests
            time.sleep(RATE_LIMIT_DELAY)
    
    logger.info(f"Scraping completed: {completed_count} successful, {failed_count} failed")
    return results


def scrape_changed_urls_only(changed_urls: List[str]) -> Dict[str, Dict]:
    """
    Incremental scraping mode for efficiency.
    
    Args:
        changed_urls: List of URLs identified by change detection
        
    Returns:
        Dict mapping URLs to their scraped content
    """
    if not changed_urls:
        logger.info("No changed URLs to scrape")
        return {}
    
    logger.info(f"Scraping {len(changed_urls)} changed URLs (incremental mode)")
    return scrape_all_urls(changed_urls)


def load_categorized_urls() -> List[str]:
    """
    Load URLs from the categorized_urls.json file.
    
    Returns:
        List of all URLs from all categories
    """
    try:
        if not CATEGORIZED_URLS_FILE.exists():
            logger.warning(f"Categorized URLs file not found: {CATEGORIZED_URLS_FILE}")
            # Fallback to reading from SDK map file
            return read_sdk_map_file()
        
        with open(CATEGORIZED_URLS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        all_urls = []
        categories = data.get('categories', {})
        
        for category, urls in categories.items():
            all_urls.extend(urls)
        
        logger.info(f"Loaded {len(all_urls)} URLs from categorized file")
        return all_urls
        
    except Exception as e:
        logger.error(f"Error loading categorized URLs: {e}")
        logger.info("Falling back to SDK map file")
        return read_sdk_map_file()


def save_scraped_content(scraped_data: Dict[str, Dict]) -> None:
    """
    Save scraped content to JSON file.
    
    Args:
        scraped_data: Dictionary of scraped content
    """
    try:
        # Ensure directory exists
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Create export data with metadata
        export_data = {
            'metadata': {
                'total_urls': len(scraped_data),
                'successful_scrapes': len([r for r in scraped_data.values() if r.get('success', False)]),
                'failed_scrapes': len([r for r in scraped_data.values() if not r.get('success', False)]),
                'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                'scraper_version': '1.0.0'
            },
            'scraped_content': scraped_data
        }
        
        # Save to file
        with open(SCRAPED_CONTENT_FILE, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved scraped content to {SCRAPED_CONTENT_FILE}")
        logger.info(f"Total: {export_data['metadata']['total_urls']} URLs")
        logger.info(f"Successful: {export_data['metadata']['successful_scrapes']} URLs")
        logger.info(f"Failed: {export_data['metadata']['failed_scrapes']} URLs")
        
    except Exception as e:
        logger.error(f"Error saving scraped content: {e}")
        raise


def update_content_hashes(scraped_data: Dict[str, Dict]) -> None:
    """
    Update content hashes after successful scraping.
    
    Args:
        scraped_data: Dictionary of scraped content
    """
    try:
        # Load existing hashes
        existing_hashes = load_existing_hashes()
        
        # Update hashes for successfully scraped content
        updated_count = 0
        for url, data in scraped_data.items():
            if data.get('success', False) and data.get('content'):
                content_hash = calculate_content_hash(data['content'])
                existing_hashes[url] = content_hash
                updated_count += 1
        
        # Save updated hashes
        save_content_hashes(existing_hashes)
        logger.info(f"Updated content hashes for {updated_count} URLs")
        
    except Exception as e:
        logger.error(f"Error updating content hashes: {e}")


def main():
    """Main function to execute the scraping workflow."""
    try:
        logger.info("X-Plane SDK Documentation Scraper")
        logger.info("=" * 50)
        
        # Load URLs to scrape
        logger.info("Loading URLs to scrape...")
        all_urls = load_categorized_urls()
        
        if not all_urls:
            logger.error("No URLs found to scrape")
            return
        
        logger.info(f"Found {len(all_urls)} URLs to process")
        
        # Option 2: Incremental scraping (use change detection)
        logger.info("Detecting changed URLs...")
        from change_detector import get_changed_urls
        changed_urls = get_changed_urls(all_urls)
        
        if not changed_urls:
            logger.info("No changed URLs detected. All content is up to date.")
            return
            
        logger.info(f"Found {len(changed_urls)} URLs that need scraping")
        scraped_data = scrape_changed_urls_only(changed_urls)
        
        # Option 1: Scrape all URLs (full scrape) - commented out for incremental mode
        # logger.info("Starting full scrape of all URLs...")
        # scraped_data = scrape_all_urls(all_urls)
        
        # Save results
        logger.info("Saving scraped content...")
        save_scraped_content(scraped_data)
        
        # Update content hashes
        logger.info("Updating content hashes...")
        update_content_hashes(scraped_data)
        
        # Final summary
        successful = len([r for r in scraped_data.values() if r.get('success', False)])
        failed = len(scraped_data) - successful
        
        logger.info("\nScraping Summary:")
        logger.info(f"  Total URLs processed: {len(scraped_data)}")
        logger.info(f"  Successful scrapes: {successful}")
        logger.info(f"  Failed scrapes: {failed}")
        logger.info(f"  Success rate: {(successful/len(scraped_data)*100):.1f}%")
        logger.info(f"  Results saved to: {SCRAPED_CONTENT_FILE}")
        
        logger.info("Scraping completed successfully!")
        
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        raise


if __name__ == "__main__":
    main()