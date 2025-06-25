#!/usr/bin/env python3
"""
X-Plane SDK Documentation Content Processor

This script processes raw scraped documentation content and converts it
into standardized formats. It handles content cleaning, formatting,
and organization for the final documentation structure.

Purpose:
- Process raw scraped documentation content
- Convert HTML to Markdown format
- Clean and standardize content formatting
- Organize content into structured directories
- Extract and process code examples
- Process and categorize SDK URLs

Usage:
    python process_content.py [options]

Dependencies:
    - markdownify: For HTML to Markdown conversion
    - beautifulsoup4: For HTML processing and cleaning
"""

import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from urllib.parse import urlparse

try:
    from bs4 import BeautifulSoup, Comment
    from markdownify import markdownify as md
except ImportError as e:
    logging.error(f"Missing required dependencies: {e}")
    logging.error("Please install: pip install beautifulsoup4 markdownify")
    raise

from change_detector import get_changed_urls, load_existing_hashes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# File paths
PROJECT_ROOT = Path(__file__).parent.parent
SDK_MAP_FILE = PROJECT_ROOT.parent / "sdk_map_optimized.txt"
RAW_DATA_DIR = PROJECT_ROOT / "raw_data"
CATEGORIZED_URLS_FILE = RAW_DATA_DIR / "categorized_urls.json"
SCRAPED_CONTENT_FILE = RAW_DATA_DIR / "scraped_content.json"
PROCESSED_CONTENT_DIR = PROJECT_ROOT / "processed_content"


def read_sdk_map_file() -> List[str]:
    """
    Read and parse the sdk_map_optimized.txt file to extract all URLs.
    
    Returns:
        List[str]: List of valid URLs from the file
        
    Raises:
        FileNotFoundError: If sdk_map_optimized.txt is not found
        Exception: For other file reading errors
    """
    try:
        if not SDK_MAP_FILE.exists():
            raise FileNotFoundError(f"SDK map file not found: {SDK_MAP_FILE}")
            
        urls = []
        with open(SDK_MAP_FILE, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Clean whitespace and skip empty lines
                url = line.strip()
                if not url:
                    continue
                    
                # Basic URL validation
                if validate_url_format(url):
                    urls.append(url)
                else:
                    logger.warning(f"Invalid URL format at line {line_num}: {url}")
                    
        logger.info(f"Successfully read {len(urls)} URLs from {SDK_MAP_FILE}")
        return urls
        
    except FileNotFoundError:
        logger.error(f"SDK map file not found: {SDK_MAP_FILE}")
        raise
    except Exception as e:
        logger.error(f"Error reading SDK map file: {e}")
        raise


def validate_url_format(url: str) -> bool:
    """
    Validate that a URL is properly formatted and is an X-Plane SDK URL.
    
    Args:
        url: URL string to validate
        
    Returns:
        bool: True if URL is valid, False otherwise
    """
    try:
        parsed = urlparse(url)
        
        # Check basic URL structure
        if not all([parsed.scheme, parsed.netloc]):
            return False
            
        # Check if it's an X-Plane SDK URL
        if not parsed.netloc == "developer.x-plane.com":
            return False
            
        # Check if it's in the SDK documentation path
        if not parsed.path.startswith("/sdk/"):
            return False
            
        return True
        
    except Exception:
        return False


def categorize_urls_by_module(urls: List[str]) -> Dict[str, List[str]]:
    """
    Categorize URLs by SDK module based on URL patterns and function names.
    
    Args:
        urls: List of URLs to categorize
        
    Returns:
        Dict[str, List[str]]: Dictionary mapping category names to URL lists
    """
    categories = {
        "XPLM_Camera": [],
        "XPLM_DataAccess": [],
        "XPLM_Display": [],
        "XPLM_Graphics": [],
        "XPLM_Navigation": [],
        "XPLM_Sound": [],
        "XPLM_Utilities": [],
        "XPLM_Instance": [],
        "XPLM_Map": [],
        "XPLM_Menus": [],
        "XPLM_Planes": [],
        "XPLM_Plugin": [],
        "XPLM_Processing": [],
        "XPLM_Scenery": [],
        "Widget_System": [],
        "Widget_Defs": [],
        "Other_APIs": []
    }
    
    # Define patterns for categorization
    patterns = {
        "XPLM_Camera": [
            r"XPLMCamera", r"camera", r"view", r"perspective"
        ],
        "XPLM_DataAccess": [
            r"XPLMDataAccess", r"XPLMData", r"dataref", r"GetData", r"SetData"
        ],
        "XPLM_Display": [
            r"XPLMDisplay", r"window", r"screen", r"draw", r"render", r"texture",
            r"XPLMGetScreen", r"XPLMGetWindow", r"XPLMSetWindow", r"XPLMCreateWindow"
        ],
        "XPLM_Graphics": [
            r"XPLMGraphics", r"graphics", r"OpenGL", r"GL", r"vertex", r"shader"
        ],
        "XPLM_Navigation": [
            r"XPLMNavigation", r"nav", r"GPS", r"FMS", r"waypoint", r"airport",
            r"METAR", r"weather", r"magnetic"
        ],
        "XPLM_Sound": [
            r"XPLMSound", r"audio", r"FMOD", r"sound", r"speaker"
        ],
        "XPLM_Utilities": [
            r"XPLMUtilities", r"GetSystem", r"GetPrefs", r"GetLanguage", r"GetVersions",
            r"GetMyID", r"keyboard", r"mouse", r"hotkey"
        ],
        "XPLM_Instance": [
            r"XPLMInstance", r"instance", r"object", r"model"
        ],
        "XPLM_Map": [
            r"XPLMMap", r"map", r"layer", r"projection"
        ],
        "XPLM_Menus": [
            r"XPLMMenus", r"menu", r"item", r"check"
        ],
        "XPLM_Planes": [
            r"XPLMPlanes", r"aircraft", r"plane", r"model"
        ],
        "XPLM_Plugin": [
            r"XPLMPlugin", r"plugin", r"enable", r"disable", r"message"
        ],
        "XPLM_Processing": [
            r"XPLMProcessing", r"flight", r"loop", r"callback", r"timer"
        ],
        "XPLM_Scenery": [
            r"XPLMScenery", r"scenery", r"terrain", r"probe", r"object"
        ],
        "Widget_System": [
            r"XP.*Widget", r"widget", r"button", r"text.*field", r"scroll.*bar",
            r"progress", r"caption", r"window.*type"
        ],
        "Widget_Defs": [
            r"Widget.*Properties", r"Widget.*Messages", r"Widget.*Types", r"Widget.*Values",
            r"Button.*", r"Caption.*", r"Main.*Window", r"Sub.*Window", r"Text.*Field",
            r"Scroll.*Bar", r"Progress.*Indicator"
        ]
    }
    
    for url in urls:
        # Extract the function/page name from URL
        url_path = urlparse(url).path
        page_name = url_path.split('/')[-1] if url_path.split('/')[-1] else url_path.split('/')[-2]
        
        categorized = False
        
        # Try to match against patterns
        for category, category_patterns in patterns.items():
            for pattern in category_patterns:
                if re.search(pattern, page_name, re.IGNORECASE):
                    categories[category].append(url)
                    categorized = True
                    break
            if categorized:
                break
                
        # If no pattern matched, put in Other_APIs
        if not categorized:
            categories["Other_APIs"].append(url)
    
    # Log categorization results
    for category, category_urls in categories.items():
        if category_urls:
            logger.info(f"{category}: {len(category_urls)} URLs")
    
    return categories


def filter_valid_urls(urls: List[str]) -> List[str]:
    """
    Filter out invalid or non-documentation URLs.
    
    Args:
        urls: List of URLs to filter
        
    Returns:
        List[str]: List of valid documentation URLs
    """
    valid_urls = []
    invalid_count = 0
    
    for url in urls:
        if validate_url_format(url):
            # Additional checks for documentation URLs
            parsed = urlparse(url)
            
            # Skip certain non-documentation paths
            skip_patterns = [
                r"/sdk/$",  # Just the base SDK page
                r"/sdk/index",  # Index pages
                r"/sdk/search",  # Search pages
            ]
            
            should_skip = False
            for pattern in skip_patterns:
                if re.search(pattern, parsed.path):
                    should_skip = True
                    break
                    
            if not should_skip:
                valid_urls.append(url)
            else:
                invalid_count += 1
        else:
            invalid_count += 1
    
    logger.info(f"Filtered URLs: {len(valid_urls)} valid, {invalid_count} invalid/skipped")
    return valid_urls


def export_categorized_urls(categorized_urls: Dict[str, List[str]], total_urls: int) -> None:
    """
    Export categorized URL list as JSON with metadata.
    
    Args:
        categorized_urls: Dictionary of categorized URLs
        total_urls: Total number of URLs processed
    """
    try:
        # Ensure raw_data directory exists
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Create export data structure
        export_data = {
            "metadata": {
                "total_urls": total_urls,
                "categories_count": len([cat for cat, urls in categorized_urls.items() if urls]),
                "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                "source_file": str(SDK_MAP_FILE.name),
                "processing_version": "1.0.0"
            },
            "categories": categorized_urls,
            "summary": {
                category: len(urls) for category, urls in categorized_urls.items() if urls
            }
        }
        
        # Save to JSON file
        with open(CATEGORIZED_URLS_FILE, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, sort_keys=True)
            
        logger.info(f"Exported categorized URLs to {CATEGORIZED_URLS_FILE}")
        logger.info(f"Total categories with URLs: {len(export_data['summary'])}")
        
    except Exception as e:
        logger.error(f"Error exporting categorized URLs: {e}")
        raise


def process_urls_for_change_detection(urls: List[str]) -> List[str]:
    """
    Prepare URL list for change detection processing.
    
    Args:
        urls: List of URLs to process
        
    Returns:
        List[str]: List of URLs that need processing (new or changed)
    """
    try:
        # Get URLs that need reprocessing
        changed_urls = get_changed_urls(urls)
        
        logger.info(f"Change detection results:")
        logger.info(f"  Total URLs: {len(urls)}")
        logger.info(f"  URLs needing processing: {len(changed_urls)}")
        logger.info(f"  URLs unchanged: {len(urls) - len(changed_urls)}")
        
        return changed_urls
        
    except Exception as e:
        logger.error(f"Error in change detection processing: {e}")
        # Return all URLs if change detection fails
        logger.warning("Falling back to processing all URLs")
        return urls


def main():
    """Main function to execute URL processing workflow."""
    try:
        logger.info("Starting X-Plane SDK URL Processing")
        logger.info("=" * 50)
        
        # Step 1: Read URLs from sdk_map_optimized.txt
        logger.info("Step 1: Reading URLs from sdk_map_optimized.txt")
        all_urls = read_sdk_map_file()
        
        # Step 2: Validate and filter URLs
        logger.info("Step 2: Validating and filtering URLs")
        valid_urls = filter_valid_urls(all_urls)
        
        # Step 3: Categorize URLs by SDK module
        logger.info("Step 3: Categorizing URLs by SDK module")
        categorized_urls = categorize_urls_by_module(valid_urls)
        
        # Step 4: Export categorized URLs as JSON
        logger.info("Step 4: Exporting categorized URLs to JSON")
        export_categorized_urls(categorized_urls, len(valid_urls))
        
        # Step 5: Prepare for change detection
        logger.info("Step 5: Processing URLs for change detection")
        changed_urls = process_urls_for_change_detection(valid_urls)
        
        # Summary
        logger.info("\nURL Processing Summary:")
        logger.info(f"  Total URLs read: {len(all_urls)}")
        logger.info(f"  Valid URLs: {len(valid_urls)}")
        logger.info(f"  URLs needing processing: {len(changed_urls)}")
        
        non_empty_categories = {cat: urls for cat, urls in categorized_urls.items() if urls}
        logger.info(f"  Categories with URLs: {len(non_empty_categories)}")
        
        for category, urls in non_empty_categories.items():
            logger.info(f"    {category}: {len(urls)} URLs")
            
        logger.info(f"\nCategorized URLs exported to: {CATEGORIZED_URLS_FILE}")
        logger.info("URL processing completed successfully!")
        
    except Exception as e:
        logger.error(f"URL processing failed: {e}")
        raise


def clean_html_content(html: str) -> str:
    """
    Remove navigation, ads, and irrelevant content from HTML.
    Clean up HTML while preserving important structural elements.
    
    Args:
        html: Raw HTML content to clean
        
    Returns:
        str: Cleaned HTML content
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove unwanted elements
        unwanted_selectors = [
            'script', 'style', 'nav', 'header', 'footer',
            '.site-header', '.site-footer', '.site-colophon',
            '.banner', '.widget-area', '.sidebar-1',
            '.cs-loader', '.search-nav', '.menu-main-menu-container',
            '.social-icons', '.email-container', '.gdpr',
            '.subscribe-form', '.footer-nav', '#secondary',
            '#primary', '.right-nav', '.api-breadcrumbs'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()
        
        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        
        # Remove empty elements
        for element in soup.find_all():
            if not element.get_text(strip=True) and not element.find_all(['img', 'br', 'hr']):
                element.decompose()
        
        # Find the main content area
        main_content = soup.find('article', class_='page')
        if main_content:
            return str(main_content)
        
        # Fallback to finding content by common patterns
        content_selectors = ['.std_docs', '.api', '.main-section']
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                return str(content)
        
        # If no specific content area found, return cleaned body
        body = soup.find('body')
        if body:
            return str(body)
        
        return str(soup)
        
    except Exception as e:
        logger.error(f"Error cleaning HTML content: {e}")
        return html


def convert_to_markdown(html: str) -> str:
    """
    Convert cleaned HTML to well-formatted Markdown.
    Use markdownify library with custom rules for code blocks.
    
    Args:
        html: Cleaned HTML content to convert
        
    Returns:
        str: Markdown formatted content
    """
    try:
        # Custom conversion options
        markdown_options = {
            'heading_style': 'ATX',  # Use # for headings
            'bullets': '-',  # Use - for bullet points
            'code_language': 'cpp',  # Default language for code blocks
            'wrap': True,
            'wrap_width': 80,
            'escape_asterisks': False,
            'escape_underscores': False,
        }
        
        # Convert HTML to Markdown
        markdown_content = md(html, **markdown_options)
        
        # Post-process the markdown
        markdown_content = _post_process_markdown(markdown_content)
        
        return markdown_content
        
    except Exception as e:
        logger.error(f"Error converting HTML to Markdown: {e}")
        return html


def _post_process_markdown(markdown: str) -> str:
    """
    Post-process markdown content to improve formatting.
    
    Args:
        markdown: Raw markdown content
        
    Returns:
        str: Processed markdown content
    """
    # Fix code block language tags
    markdown = re.sub(r'```\s*language-cpp', '```cpp', markdown)
    markdown = re.sub(r'```\s*language-c', '```c', markdown)
    
    # Clean up excessive whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    # Fix table formatting
    markdown = re.sub(r'\|\s*\|\s*\|', '| |', markdown)
    
    # Ensure proper spacing around headings
    markdown = re.sub(r'(\n#{1,6}\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', markdown)
    
    # Fix link formatting
    markdown = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'[{m.group(1).strip()}]({m.group(2).strip()})', markdown)
    
    return markdown.strip()


def extract_api_signatures(content: str) -> List[Dict[str, Any]]:
    """
    Parse function signatures and parameters from content.
    Identify C/C++ function declarations and definitions.
    
    Args:
        content: Content to parse for API signatures
        
    Returns:
        List[Dict]: List of API function information
    """
    try:
        signatures = []
        
        # Parse HTML content for structured API information
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find function definitions using multiple patterns
        functions = soup.find_all(['div', 'section'], class_='function')
        
        for func_div in functions:
            signature_info = {}
            
            # Extract function name
            func_name_elem = func_div.find(['h3', 'h2'], class_='sdk-api-function')
            if func_name_elem:
                func_name = func_name_elem.get_text(strip=True)
                signature_info['name'] = func_name
                
                # Extract function signature from code block
                code_block = func_div.find('pre')
                if code_block:
                    signature_text = code_block.get_text(strip=True)
                    signature_info['signature'] = signature_text
                    
                    # Parse parameters from signature
                    parameters = _parse_function_parameters(signature_text)
                    signature_info['parameters'] = parameters
                
                # Extract description
                description_elem = func_div.find('p')
                if description_elem:
                    signature_info['description'] = description_elem.get_text(strip=True)
                
                # Check if deprecated
                if 'XPLM_DEPRECATED' in func_div.get('class', []):
                    signature_info['deprecated'] = True
                
                signatures.append(signature_info)
        
        # Also look for enum definitions
        enums = soup.find_all(['div', 'section'], class_='enum')
        for enum_div in enums:
            enum_info = {}
            
            enum_name_elem = enum_div.find(['h3', 'h2'], class_='sdk-api-enum')
            if enum_name_elem:
                enum_name = enum_name_elem.get_text(strip=True)
                enum_info['name'] = enum_name
                enum_info['type'] = 'enum'
                
                # Extract enum values
                enum_values = []
                enum_table = enum_div.find('table')
                if enum_table:
                    rows = enum_table.find_all('tr')[1:]  # Skip header
                    for row in rows:
                        cells = row.find_all('td')
                        if len(cells) >= 3:
                            value_info = {
                                'name': cells[0].get_text(strip=True),
                                'value': cells[1].get_text(strip=True),
                                'description': cells[2].get_text(strip=True)
                            }
                            enum_values.append(value_info)
                
                enum_info['values'] = enum_values
                signatures.append(enum_info)
        
        # Enhanced extraction: Look for function signatures in code blocks
        code_blocks = soup.find_all('pre')
        for code_block in code_blocks:
            code_text = code_block.get_text(strip=True)
            
            # Look for C/C++ function signatures
            function_patterns = [
                r'XPLM_API\s+(\w+)\s+(\w+)\s*\([^)]*\)',  # XPLM_API functions
                r'(\w+)\s+(\w+)\s*\([^)]*\)\s*;',         # Standard C functions
                r'typedef\s+(\w+)\s*\([^)]*\)\s*(\w+)',   # Function typedefs
            ]
            
            for pattern in function_patterns:
                matches = re.finditer(pattern, code_text, re.MULTILINE)
                for match in matches:
                    if len(match.groups()) >= 2:
                        func_info = {
                            'name': match.group(2) if 'XPLM_API' in match.group(0) else match.group(1),
                            'signature': match.group(0),
                            'type': 'function',
                            'source': 'code_block_extraction'
                        }
                        
                        # Avoid duplicates
                        if not any(sig.get('name') == func_info['name'] for sig in signatures):
                            signatures.append(func_info)
            
            # Look for #define statements (constants and macros)
            define_pattern = r'#define\s+(\w+)\s+(.+)'
            define_matches = re.finditer(define_pattern, code_text, re.MULTILINE)
            for match in define_matches:
                define_info = {
                    'name': match.group(1),
                    'value': match.group(2).strip(),
                    'type': 'define',
                    'signature': match.group(0),
                    'source': 'code_block_extraction'
                }
                
                # Avoid duplicates
                if not any(sig.get('name') == define_info['name'] for sig in signatures):
                    signatures.append(define_info)
        
        return signatures
        
    except Exception as e:
        logger.error(f"Error extracting API signatures: {e}")
        return []


def _parse_function_parameters(signature: str) -> List[Dict[str, str]]:
    """
    Parse function parameters from C/C++ function signature.
    
    Args:
        signature: Function signature string
        
    Returns:
        List[Dict]: List of parameter information
    """
    parameters = []
    
    try:
        # Extract parameter list from signature
        param_match = re.search(r'\((.*?)\);?$', signature, re.DOTALL)
        if not param_match:
            return parameters
        
        param_string = param_match.group(1).strip()
        if not param_string or param_string == 'void':
            return parameters
        
        # Split parameters by comma, but be careful with nested types
        param_parts = []
        paren_depth = 0
        current_param = ""
        
        for char in param_string:
            if char == '(' or char == '[':
                paren_depth += 1
            elif char == ')' or char == ']':
                paren_depth -= 1
            elif char == ',' and paren_depth == 0:
                param_parts.append(current_param.strip())
                current_param = ""
                continue
            
            current_param += char
        
        if current_param.strip():
            param_parts.append(current_param.strip())
        
        # Parse each parameter
        for param in param_parts:
            param = param.strip()
            if not param:
                continue
            
            # Remove comments
            param = re.sub(r'/\*.*?\*/', '', param).strip()
            
            # Split into type and name
            parts = param.split()
            if len(parts) >= 2:
                param_name = parts[-1].strip('*&')
                param_type = ' '.join(parts[:-1])
                
                parameters.append({
                    'name': param_name,
                    'type': param_type,
                    'full_declaration': param
                })
        
        return parameters
        
    except Exception as e:
        logger.error(f"Error parsing function parameters: {e}")
        return []


def extract_code_examples(content: str) -> List[Dict[str, Any]]:
    """
    Extract code examples from content for Context7 usefulness.
    
    Args:
        content: Content to parse for code examples
        
    Returns:
        List[Dict]: List of code examples with metadata
    """
    try:
        examples = []
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all code blocks
        code_blocks = soup.find_all('pre')
        
        for i, code_block in enumerate(code_blocks):
            code_text = code_block.get_text(strip=True)
            
            # Skip very short code snippets (likely just single definitions)
            if len(code_text.split('\n')) < 2 and len(code_text) < 50:
                continue
            
            # Determine language from context or content
            language = 'cpp'  # Default for X-Plane SDK
            
            # Look for language hints in parent elements
            parent = code_block.parent
            if parent:
                parent_text = parent.get_text().lower()
                if 'javascript' in parent_text or 'js' in parent_text:
                    language = 'javascript'
                elif 'python' in parent_text:
                    language = 'python'
                elif 'c++' in parent_text or 'cpp' in parent_text:
                    language = 'cpp'
                elif 'c' in parent_text and 'c++' not in parent_text:
                    language = 'c'
            
            # Extract context (surrounding text)
            context = ""
            if parent:
                # Get preceding paragraph or heading
                prev_sibling = code_block.find_previous_sibling(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                if prev_sibling:
                    context = prev_sibling.get_text(strip=True)[:200]  # First 200 chars
            
            # Categorize the code example
            example_type = 'snippet'
            if len(code_text.split('\n')) > 10:
                example_type = 'example'
            if 'main(' in code_text or 'int main' in code_text:
                example_type = 'complete_program'
            if '#include' in code_text and len(code_text.split('\n')) > 5:
                example_type = 'example'
            
            example_info = {
                'id': f'example_{i}',
                'code': code_text,
                'language': language,
                'type': example_type,
                'context': context,
                'line_count': len(code_text.split('\n')),
                'char_count': len(code_text)
            }
            
            examples.append(example_info)
        
        return examples
        
    except Exception as e:
        logger.error(f"Error extracting code examples: {e}")
        return []


def categorize_content(url: str, content: str) -> Dict[str, str]:
    """
    Assign content to appropriate SDK module based on URL patterns.
    Use the existing categorization logic from URL processing.
    
    Args:
        url: URL of the content
        content: Content to categorize
        
    Returns:
        Dict: Category information
    """
    try:
        # Use existing categorization logic
        categorized_urls = categorize_urls_by_module([url])
        
        # Find which category this URL belongs to
        for category, urls in categorized_urls.items():
            if url in urls:
                return {
                    'category': category,
                    'url': url,
                    'module': category.replace('_', ' ').title()
                }
        
        # Default category if not found
        return {
            'category': 'Other_APIs',
            'url': url,
            'module': 'Other APIs'
        }
        
    except Exception as e:
        logger.error(f"Error categorizing content for {url}: {e}")
        return {
            'category': 'Other_APIs',
            'url': url,
            'module': 'Other APIs'
        }


def generate_cross_references(content_dict: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Create links between related functions and modules.
    Identify function references within documentation.
    
    Args:
        content_dict: Dictionary of processed content
        
    Returns:
        Dict: Cross-reference mapping
    """
    try:
        cross_refs = {}
        
        # Extract all function names from all content
        all_functions = set()
        for url, content_info in content_dict.items():
            if 'api_signatures' in content_info:
                for sig in content_info['api_signatures']:
                    if 'name' in sig:
                        all_functions.add(sig['name'])
        
        # Find cross-references in each piece of content
        for url, content_info in content_dict.items():
            refs = []
            content_text = content_info.get('markdown', '')
            
            # Look for function references in the content
            for func_name in all_functions:
                if func_name in content_text and func_name not in content_info.get('own_functions', []):
                    refs.append(func_name)
            
            # Look for XPLM module references
            xplm_modules = [
                'XPLMCamera', 'XPLMDataAccess', 'XPLMDisplay', 'XPLMGraphics',
                'XPLMNavigation', 'XPLMSound', 'XPLMUtilities', 'XPLMInstance',
                'XPLMMap', 'XPLMMenus', 'XPLMPlanes', 'XPLMPlugin',
                'XPLMProcessing', 'XPLMScenery'
            ]
            
            for module in xplm_modules:
                if module in content_text and module not in url:
                    refs.append(module)
            
            cross_refs[url] = list(set(refs))
        
        return cross_refs
        
    except Exception as e:
        logger.error(f"Error generating cross-references: {e}")
        return {}


def process_scraped_content() -> Dict[str, Any]:
    """
    Process raw scraped content and convert to structured format.
    
    Returns:
        Dict: Processed content data
    """
    try:
        # Load scraped content
        if not SCRAPED_CONTENT_FILE.exists():
            raise FileNotFoundError(f"Scraped content file not found: {SCRAPED_CONTENT_FILE}")
        
        with open(SCRAPED_CONTENT_FILE, 'r', encoding='utf-8') as f:
            scraped_data = json.load(f)
        
        processed_content = {}
        processing_stats = {
            'total_pages': 0,
            'successful_processing': 0,
            'failed_processing': 0,
            'categories': {}
        }
        
        scraped_content = scraped_data.get('scraped_content', {})
        processing_stats['total_pages'] = len(scraped_content)
        
        logger.info(f"Processing {len(scraped_content)} scraped pages...")
        
        for url, page_data in scraped_content.items():
            try:
                logger.info(f"Processing: {url}")
                
                # Extract content from page data
                raw_html = page_data.get('content', '')
                if not raw_html:
                    logger.warning(f"No content found for {url}")
                    continue
                
                # Process the content
                cleaned_html = clean_html_content(raw_html)
                markdown_content = convert_to_markdown(cleaned_html)
                api_signatures = extract_api_signatures(cleaned_html)
                code_examples = extract_code_examples(cleaned_html)
                category_info = categorize_content(url, cleaned_html)
                
                # Store processed content
                processed_content[url] = {
                    'url': url,
                    'title': page_data.get('metadata', {}).get('title', ''),
                    'cleaned_html': cleaned_html,
                    'markdown': markdown_content,
                    'api_signatures': api_signatures,
                    'code_examples': code_examples,
                    'category': category_info,
                    'own_functions': [sig['name'] for sig in api_signatures if 'name' in sig],
                    'processing_timestamp': datetime.now(timezone.utc).isoformat()
                }
                
                # Update stats
                processing_stats['successful_processing'] += 1
                category = category_info['category']
                processing_stats['categories'][category] = processing_stats['categories'].get(category, 0) + 1
                
            except Exception as e:
                logger.error(f"Error processing {url}: {e}")
                processing_stats['failed_processing'] += 1
        
        # Generate cross-references
        logger.info("Generating cross-references...")
        cross_references = generate_cross_references(processed_content)
        
        # Add cross-references to processed content
        for url in processed_content:
            processed_content[url]['cross_references'] = cross_references.get(url, [])
        
        # Create final output structure
        output_data = {
            'metadata': {
                'processing_timestamp': datetime.now(timezone.utc).isoformat(),
                'processor_version': '1.0.0',
                'source_file': str(SCRAPED_CONTENT_FILE.name),
                'statistics': processing_stats
            },
            'processed_content': processed_content,
            'cross_references': cross_references
        }
        
        logger.info("Content processing completed successfully!")
        logger.info(f"Processed: {processing_stats['successful_processing']} pages")
        logger.info(f"Failed: {processing_stats['failed_processing']} pages")
        logger.info(f"Categories: {len(processing_stats['categories'])}")
        
        return output_data
        
    except Exception as e:
        logger.error(f"Error processing scraped content: {e}")
        raise


def save_processed_content(processed_data: Dict[str, Any]) -> None:
    """
    Save processed content to JSON file.
    
    Args:
        processed_data: Processed content data to save
    """
    try:
        # Ensure output directory exists
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        output_file = RAW_DATA_DIR / "processed_content.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2, sort_keys=True, ensure_ascii=False)
        
        logger.info(f"Processed content saved to: {output_file}")
        
    except Exception as e:
        logger.error(f"Error saving processed content: {e}")
        raise


def test_content_processing() -> None:
    """
    Test content processing functions with sample data.
    """
    try:
        logger.info("Testing content processing functions...")
        
        # Test with sample HTML
        sample_html = '''
        <article class="page">
            <div class="std_docs">
                <div class="api">
                    <h1 class="sdk-api-title">XPLMGraphics API</h1>
                    <p>This is a test description.</p>
                    <div class="function">
                        <h3 class="sdk-api-function">XPLMSetGraphicsState</h3>
                        <pre class="language-cpp">
                            <code>XPLM_API void XPLMSetGraphicsState(int inEnableFog);</code>
                        </pre>
                        <p>This function sets graphics state.</p>
                    </div>
                </div>
            </div>
        </article>
        '''
        
        # Test cleaning
        cleaned = clean_html_content(sample_html)
        logger.info("✓ HTML cleaning test passed")
        
        # Test markdown conversion
        markdown = convert_to_markdown(cleaned)
        logger.info("✓ Markdown conversion test passed")
        
        # Test API signature extraction
        signatures = extract_api_signatures(cleaned)
        logger.info(f"✓ API signature extraction test passed - found {len(signatures)} signatures")
        
        # Test categorization
        category = categorize_content("https://developer.x-plane.com/sdk/XPLMGraphics/", cleaned)
        logger.info(f"✓ Content categorization test passed - category: {category['category']}")
        
        logger.info("All content processing tests passed!")
        
    except Exception as e:
        logger.error(f"Content processing test failed: {e}")
        raise

def main_content_processing():
    """Main function for content processing workflow."""
    try:
        logger.info("Starting X-Plane SDK Content Processing")
        logger.info("=" * 50)
        
        # Test content processing functions
        logger.info("Step 1: Testing content processing functions")
        test_content_processing()
        
        # Process scraped content
        logger.info("Step 2: Processing scraped content")
        processed_data = process_scraped_content()
        
        # Save processed content
        logger.info("Step 3: Saving processed content")
        save_processed_content(processed_data)
        
        # Summary
        stats = processed_data['metadata']['statistics']
        logger.info("\nContent Processing Summary:")
        logger.info(f"  Total pages processed: {stats['total_pages']}")
        logger.info(f"  Successful: {stats['successful_processing']}")
        logger.info(f"  Failed: {stats['failed_processing']}")
        logger.info(f"  Categories found: {len(stats['categories'])}")
        
        for category, count in stats['categories'].items():
            logger.info(f"    {category}: {count} pages")
        
        logger.info("\nContent processing completed successfully!")
        
    except Exception as e:
        logger.error(f"Content processing failed: {e}")
        raise


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "process":
        main_content_processing()
    else:
        main()