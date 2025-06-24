#!/usr/bin/env python3
"""
Demo script to display processed content in a readable format.
"""

import json
import sys
from pathlib import Path

def display_processed_content():
    """Display processed content in a readable format."""
    
    # Load processed content
    processed_file = Path(__file__).parent.parent / "raw_data" / "processed_content.json"
    
    if not processed_file.exists():
        print("❌ Processed content file not found. Run content processing first.")
        return
    
    with open(processed_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("🔧 X-Plane SDK Content Processing Results")
    print("=" * 60)
    
    # Display metadata
    metadata = data['metadata']
    stats = metadata['statistics']
    
    print(f"📊 Processing Statistics:")
    print(f"   • Total pages: {stats['total_pages']}")
    print(f"   • Successful: {stats['successful_processing']}")
    print(f"   • Failed: {stats['failed_processing']}")
    print(f"   • Categories: {len(stats['categories'])}")
    print()
    
    # Display categories
    print("📂 Categories Found:")
    for category, count in stats['categories'].items():
        print(f"   • {category}: {count} pages")
    print()
    
    # Display sample content for each URL
    processed_content = data['processed_content']
    
    for i, (url, content) in enumerate(processed_content.items(), 1):
        print(f"📄 Page {i}: {content['title']}")
        print(f"🔗 URL: {url}")
        print(f"📁 Category: {content['category']['category']}")
        print(f"🔧 API Functions Found: {len(content['api_signatures'])}")
        
        # Show first few API signatures
        if content['api_signatures']:
            print("   📋 API Functions:")
            for j, sig in enumerate(content['api_signatures'][:3], 1):
                name = sig.get('name', 'Unknown')
                param_count = len(sig.get('parameters', []))
                deprecated = " (DEPRECATED)" if sig.get('deprecated') else ""
                print(f"      {j}. {name}({param_count} params){deprecated}")
            
            if len(content['api_signatures']) > 3:
                print(f"      ... and {len(content['api_signatures']) - 3} more")
        
        # Show markdown preview
        markdown = content.get('markdown', '')
        if markdown:
            preview = markdown[:200].replace('\n', ' ')
            print(f"📝 Markdown Preview: {preview}...")
        
        print()
    
    print("✅ Content processing demonstration complete!")

if __name__ == "__main__":
    display_processed_content()