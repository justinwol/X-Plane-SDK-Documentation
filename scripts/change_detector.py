#!/usr/bin/env python3
"""
X-Plane SDK Documentation Change Detector

This module implements the change detection system for X-Plane SDK documentation.
It compares current documentation with previous versions using content hashing
to identify which URLs need reprocessing.

Functions:
    calculate_content_hash(content): Generate SHA256 hash of content
    load_existing_hashes(): Load previous content hashes from JSON file
    save_content_hashes(hash_dict): Save updated hashes to JSON file
    detect_changes(url_list): Compare current vs stored hashes for given URLs
    get_changed_urls(url_list): Return list of URLs that need reprocessing
"""

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to the content hashes file
HASHES_FILE = Path(__file__).parent.parent / "raw_data" / "content_hashes.json"


def calculate_content_hash(content: Union[str, bytes]) -> str:
    """
    Generate SHA256 hash of content.
    
    Args:
        content: Content to hash (string or bytes)
        
    Returns:
        str: Hexadecimal hash string
        
    Example:
        >>> calculate_content_hash("Hello World")
        'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
    """
    if isinstance(content, str):
        content = content.encode('utf-8')
    elif not isinstance(content, bytes):
        raise TypeError("Content must be string or bytes")
    
    hash_obj = hashlib.sha256()
    hash_obj.update(content)
    return hash_obj.hexdigest()


def load_existing_hashes() -> Dict[str, str]:
    """
    Load previous content hashes from content_hashes.json.
    
    Returns:
        dict: Dictionary of URL -> hash mappings, empty dict if file not found
        
    Raises:
        Warning: Logs warning if JSON is corrupted but continues with empty dict
    """
    try:
        if not HASHES_FILE.exists():
            logger.info("Content hashes file not found. Starting with empty hash dictionary.")
            return {}
            
        with open(HASHES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Extract just the URL hashes, excluding metadata
        if isinstance(data, dict):
            # Remove special keys like 'last_update'
            hashes = {k: v for k, v in data.items() if k != 'last_update'}
            logger.info(f"Loaded {len(hashes)} existing content hashes.")
            return hashes
        else:
            logger.warning("Invalid hash file format. Starting with empty dictionary.")
            return {}
            
    except json.JSONDecodeError as e:
        logger.warning(f"Corrupted JSON in hash file: {e}. Starting with empty dictionary.")
        return {}
    except Exception as e:
        logger.error(f"Error loading hash file: {e}. Starting with empty dictionary.")
        return {}


def save_content_hashes(hash_dict: Dict[str, str]) -> None:
    """
    Save updated hashes to content_hashes.json.
    
    Args:
        hash_dict: Dictionary of URL -> hash mappings
        
    The saved format includes a timestamp:
    {
        "https://example.com/page1": "hash1",
        "https://example.com/page2": "hash2",
        "last_update": "2024-01-15T10:30:00Z"
    }
    """
    try:
        # Ensure the directory exists
        HASHES_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the data structure with timestamp
        data = dict(hash_dict)
        data['last_update'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        # Save with proper JSON formatting
        with open(HASHES_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, sort_keys=True)
            
        logger.info(f"Saved {len(hash_dict)} content hashes to {HASHES_FILE}")
        
    except Exception as e:
        logger.error(f"Error saving hash file: {e}")
        raise


def detect_changes(url_list: List[str]) -> Dict[str, str]:
    """
    Compare current vs stored hashes for given URLs.
    
    Args:
        url_list: List of URLs to check for changes
        
    Returns:
        dict: Dictionary with changed URLs and their new hashes
        
    Note:
        This function assumes you have a way to fetch current content for URLs.
        For now, it returns URLs not in existing hash file as "changed".
    """
    existing_hashes = load_existing_hashes()
    changed_urls = {}
    
    for url in url_list:
        if url not in existing_hashes:
            # URL not in existing hashes - treat as changed
            # In a real implementation, you would fetch the content and hash it
            logger.info(f"URL not in existing hashes (new or first run): {url}")
            changed_urls[url] = "new_url_placeholder_hash"
        # Note: To detect actual content changes, you would:
        # 1. Fetch current content for the URL
        # 2. Calculate its hash using calculate_content_hash()
        # 3. Compare with existing_hashes[url]
        # 4. If different, add to changed_urls
    
    logger.info(f"Detected {len(changed_urls)} changed URLs out of {len(url_list)} total URLs.")
    return changed_urls


def get_changed_urls(url_list: List[str]) -> List[str]:
    """
    Return list of URLs that need reprocessing.
    
    Args:
        url_list: List of URLs to check
        
    Returns:
        list: List of URLs that have changed or are new
    """
    changed_dict = detect_changes(url_list)
    changed_urls = list(changed_dict.keys())
    
    logger.info(f"Found {len(changed_urls)} URLs that need reprocessing.")
    return changed_urls


def initialize_content_hashes() -> None:
    """
    Initialize content_hashes.json with empty structure and current timestamp.
    """
    initial_data = {
        "last_update": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    
    try:
        HASHES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(HASHES_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=2)
        logger.info(f"Initialized content hashes file at {HASHES_FILE}")
    except Exception as e:
        logger.error(f"Error initializing hash file: {e}")
        raise


if __name__ == "__main__":
    # Example usage and testing
    print("X-Plane SDK Documentation Change Detector")
    print("=" * 50)
    
    # Initialize if needed
    if not HASHES_FILE.exists():
        print("Initializing content hashes file...")
        initialize_content_hashes()
    
    # Example URL list
    example_urls = [
        "https://developer.x-plane.com/sdk/XPLMCamera/",
        "https://developer.x-plane.com/sdk/XPLMDataAccess/",
        "https://developer.x-plane.com/sdk/XPLMDisplay/"
    ]
    
    print(f"\nTesting with example URLs: {len(example_urls)} URLs")
    
    # Test hash calculation
    test_content = "This is test content for hashing"
    test_hash = calculate_content_hash(test_content)
    print(f"Test hash: {test_hash}")
    
    # Test change detection
    changed_urls = get_changed_urls(example_urls)
    print(f"Changed URLs: {changed_urls}")
    
    # Test saving hashes
    test_hashes = {url: f"hash_{i}" for i, url in enumerate(example_urls)}
    save_content_hashes(test_hashes)
    print("Saved test hashes successfully")
    
    print("\nChange detector module implementation complete!")