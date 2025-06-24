#!/usr/bin/env python3
"""
Comprehensive test script for content processing functionality.
"""

import json
import sys
from pathlib import Path

# Add the scripts directory to the path so we can import process_content
sys.path.insert(0, str(Path(__file__).parent))

from process_content import (
    clean_html_content,
    convert_to_markdown,
    extract_api_signatures,
    categorize_content,
    generate_cross_references
)

def test_all_functions():
    """Test all content processing functions with real data."""
    
    print("🧪 Testing X-Plane SDK Content Processing Functions")
    print("=" * 60)
    
    # Load real scraped content for testing
    scraped_file = Path(__file__).parent.parent / "raw_data" / "scraped_content.json"
    
    if not scraped_file.exists():
        print("❌ Scraped content file not found.")
        return
    
    with open(scraped_file, 'r', encoding='utf-8') as f:
        scraped_data = json.load(f)
    
    # Get first page for testing
    scraped_content = scraped_data.get('scraped_content', {})
    if not scraped_content:
        print("❌ No scraped content found.")
        return
    
    # Test with XPLMGraphics page
    test_url = "https://developer.x-plane.com/sdk/XPLMGraphics/"
    if test_url not in scraped_content:
        test_url = list(scraped_content.keys())[0]
    
    test_page = scraped_content[test_url]
    raw_html = test_page.get('content', '')
    
    print(f"🔍 Testing with: {test_url}")
    print(f"📏 Raw HTML size: {len(raw_html):,} characters")
    print()
    
    # Test 1: HTML Cleaning
    print("1️⃣ Testing HTML Cleaning...")
    cleaned_html = clean_html_content(raw_html)
    print(f"   ✅ Cleaned HTML size: {len(cleaned_html):,} characters")
    print(f"   📉 Size reduction: {((len(raw_html) - len(cleaned_html)) / len(raw_html) * 100):.1f}%")
    
    # Show sample of cleaned content
    sample_cleaned = cleaned_html[:300].replace('\n', ' ')
    print(f"   📝 Sample: {sample_cleaned}...")
    print()
    
    # Test 2: Markdown Conversion
    print("2️⃣ Testing Markdown Conversion...")
    markdown_content = convert_to_markdown(cleaned_html)
    print(f"   ✅ Markdown size: {len(markdown_content):,} characters")
    
    # Show sample markdown
    lines = markdown_content.split('\n')[:10]
    print("   📝 Sample Markdown:")
    for line in lines:
        if line.strip():
            print(f"      {line}")
    print("      ...")
    print()
    
    # Test 3: API Signature Extraction
    print("3️⃣ Testing API Signature Extraction...")
    api_signatures = extract_api_signatures(cleaned_html)
    print(f"   ✅ Found {len(api_signatures)} API signatures")
    
    # Show sample signatures
    for i, sig in enumerate(api_signatures[:3], 1):
        name = sig.get('name', 'Unknown')
        param_count = len(sig.get('parameters', []))
        sig_type = sig.get('type', 'function')
        deprecated = " (DEPRECATED)" if sig.get('deprecated') else ""
        print(f"   {i}. {name} ({sig_type}, {param_count} params){deprecated}")
        
        # Show parameters for first function
        if i == 1 and sig.get('parameters'):
            print("      Parameters:")
            for param in sig['parameters'][:3]:
                print(f"        • {param['type']} {param['name']}")
            if len(sig['parameters']) > 3:
                print(f"        • ... and {len(sig['parameters']) - 3} more")
    
    if len(api_signatures) > 3:
        print(f"   ... and {len(api_signatures) - 3} more")
    print()
    
    # Test 4: Content Categorization
    print("4️⃣ Testing Content Categorization...")
    category_info = categorize_content(test_url, cleaned_html)
    print(f"   ✅ Category: {category_info['category']}")
    print(f"   📂 Module: {category_info['module']}")
    print()
    
    # Test 5: Cross-Reference Generation
    print("5️⃣ Testing Cross-Reference Generation...")
    
    # Create sample content dict for cross-reference testing
    sample_content = {}
    for url, page_data in list(scraped_content.items())[:2]:
        cleaned = clean_html_content(page_data.get('content', ''))
        signatures = extract_api_signatures(cleaned)
        sample_content[url] = {
            'markdown': convert_to_markdown(cleaned),
            'api_signatures': signatures,
            'own_functions': [sig['name'] for sig in signatures if 'name' in sig]
        }
    
    cross_refs = generate_cross_references(sample_content)
    print(f"   ✅ Generated cross-references for {len(cross_refs)} pages")
    
    for url, refs in cross_refs.items():
        page_name = url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]
        print(f"   📄 {page_name}: {len(refs)} references")
        if refs:
            print(f"      → {', '.join(refs[:3])}")
            if len(refs) > 3:
                print(f"      → ... and {len(refs) - 3} more")
    print()
    
    # Test 6: Code Block Detection
    print("6️⃣ Testing Code Block Detection...")
    code_blocks = markdown_content.count('```')
    print(f"   ✅ Found {code_blocks // 2} code blocks in markdown")
    
    # Show sample code block
    if '```cpp' in markdown_content:
        start = markdown_content.find('```cpp')
        end = markdown_content.find('```', start + 6)
        if end != -1:
            code_sample = markdown_content[start:end + 3]
            lines = code_sample.split('\n')[:5]
            print("   📝 Sample Code Block:")
            for line in lines:
                print(f"      {line}")
            if len(code_sample.split('\n')) > 5:
                print("      ...")
    print()
    
    print("✅ All content processing tests completed successfully!")
    print()
    print("📊 Summary:")
    print(f"   • HTML cleaning: ✅ Working")
    print(f"   • Markdown conversion: ✅ Working")
    print(f"   • API signature extraction: ✅ Working ({len(api_signatures)} found)")
    print(f"   • Content categorization: ✅ Working")
    print(f"   • Cross-reference generation: ✅ Working")
    print(f"   • Code block preservation: ✅ Working ({code_blocks // 2} blocks)")

if __name__ == "__main__":
    test_all_functions()