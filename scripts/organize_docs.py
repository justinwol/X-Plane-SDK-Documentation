#!/usr/bin/env python3
"""
Script to organize X-Plane SDK documentation into structured markdown files.
This implements Task 6: Documentation Organization from the processing plan.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

def load_processed_content(file_path: str) -> Dict[str, Any]:
    """Load the processed content from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_categorized_urls(file_path: str) -> Dict[str, Any]:
    """Load the categorized URLs from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_frontmatter(title: str, description: str, category: str) -> str:
    """Create YAML frontmatter for markdown files."""
    return f"""---
title: "{title}"
description: "{description}"
category: "{category}"
date: "{datetime.now().isoformat()}"
---

"""

def format_api_signature(api_sig: Dict[str, Any]) -> str:
    """Format an API signature into markdown."""
    markdown = ""
    
    # Function name and signature
    if 'signature' in api_sig:
        markdown += f"### {api_sig['name']}\n\n"
        markdown += f"```cpp\n{api_sig['signature']}\n```\n\n"
    elif 'type' in api_sig and api_sig['type'] == 'enum':
        markdown += f"### {api_sig['name']} (Enum)\n\n"
    else:
        markdown += f"### {api_sig['name']}\n\n"
    
    # Description
    if 'description' in api_sig:
        markdown += f"{api_sig['description']}\n\n"
    
    # Parameters
    if 'parameters' in api_sig and api_sig['parameters']:
        markdown += "**Parameters:**\n\n"
        for param in api_sig['parameters']:
            markdown += f"- `{param['name']}` ({param['type']}): {param.get('description', 'No description available')}\n"
        markdown += "\n"
    
    # Enum values
    if 'values' in api_sig:
        markdown += "**Values:**\n\n"
        markdown += "| Name | Value | Description |\n"
        markdown += "|------|-------|-------------|\n"
        for value in api_sig['values']:
            desc = value.get('description', 'No description available')
            markdown += f"| {value['name']} | {value['value']} | {desc} |\n"
        markdown += "\n"
    
    # Deprecation notice
    if api_sig.get('deprecated', False):
        markdown += "**⚠️ DEPRECATED:** This function is deprecated and should not be used in new code.\n\n"
    
    markdown += "---\n\n"
    return markdown

def create_module_markdown(category: str, content_data: List[Dict[str, Any]], 
                          category_urls: List[str]) -> str:
    """Create markdown content for a module category."""
    
    # Map category names to readable titles
    category_titles = {
        'XPLM_Camera': 'Camera APIs',
        'XPLM_DataAccess': 'Data Access APIs', 
        'XPLM_Display': 'Display APIs',
        'XPLM_Graphics': 'Graphics APIs',
        'XPLM_Navigation': 'Navigation APIs',
        'XPLM_Sound': 'Sound APIs',
        'XPLM_Utilities': 'Utilities APIs',
        'XPLM_Processing': 'Processing APIs',
        'XPLM_Plugin': 'Plugin APIs',
        'XPLM_Planes': 'Planes APIs',
        'XPLM_Scenery': 'Scenery APIs',
        'XPLM_Instance': 'Instance APIs',
        'XPLM_Map': 'Map APIs',
        'XPLM_Menus': 'Menus APIs',
        'Widget_System': 'Widget System',
        'Other_APIs': 'Other/Miscellaneous APIs'
    }
    
    title = category_titles.get(category, category.replace('_', ' '))
    description = f"X-Plane SDK {title} documentation"
    
    markdown = create_frontmatter(title, description, category)
    markdown += f"# {title}\n\n"
    
    if content_data:
        # We have processed content for this category
        for content in content_data:
            if 'markdown' in content:
                # Use the processed markdown content
                markdown += content['markdown'] + "\n\n"
            elif 'api_signatures' in content:
                # Generate markdown from API signatures
                for api_sig in content['api_signatures']:
                    markdown += format_api_signature(api_sig)
    else:
        # No processed content, create placeholder with URL list
        markdown += f"This section contains {len(category_urls)} API endpoints and definitions.\n\n"
        markdown += "## Available APIs\n\n"
        markdown += "The following APIs are available in this category:\n\n"
        
        for url in category_urls[:10]:  # Show first 10 URLs
            api_name = url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]
            markdown += f"- [{api_name}]({url})\n"
        
        if len(category_urls) > 10:
            markdown += f"\n... and {len(category_urls) - 10} more APIs.\n"
        
        markdown += "\n**Note:** Detailed documentation for these APIs will be available once the content processing is complete.\n\n"
    
    return markdown

def organize_documentation():
    """Main function to organize documentation into structured markdown files."""
    
    # Paths
    base_dir = Path(__file__).parent.parent
    processed_content_path = base_dir / 'raw_data' / 'processed_content.json'
    categorized_urls_path = base_dir / 'raw_data' / 'categorized_urls.json'
    docs_dir = base_dir / 'docs'
    
    # Load data
    print("Loading processed content...")
    processed_data = load_processed_content(processed_content_path)
    
    print("Loading categorized URLs...")
    categorized_data = load_categorized_urls(categorized_urls_path)
    
    # Create directory structure
    api_dir = docs_dir / 'api'
    widgets_dir = docs_dir / 'widgets'
    modules_dir = docs_dir / 'modules'
    
    api_dir.mkdir(parents=True, exist_ok=True)
    widgets_dir.mkdir(parents=True, exist_ok=True)
    modules_dir.mkdir(parents=True, exist_ok=True)
    
    # Category to file mapping
    category_files = {
        'XPLM_Camera': api_dir / 'xplm-camera.md',
        'XPLM_DataAccess': api_dir / 'xplm-dataaccess.md',
        'XPLM_Display': api_dir / 'xplm-display.md',
        'XPLM_Graphics': api_dir / 'xplm-graphics.md',
        'XPLM_Navigation': api_dir / 'xplm-navigation.md',
        'XPLM_Sound': api_dir / 'xplm-sound.md',
        'XPLM_Utilities': api_dir / 'xplm-utilities.md',
        'XPLM_Processing': api_dir / 'xplm-processing.md',
        'XPLM_Plugin': api_dir / 'xplm-plugin.md',
        'XPLM_Planes': api_dir / 'xplm-planes.md',
        'XPLM_Scenery': api_dir / 'xplm-scenery.md',
        'XPLM_Instance': api_dir / 'xplm-instance.md',
        'XPLM_Map': api_dir / 'xplm-map.md',
        'XPLM_Menus': api_dir / 'xplm-menus.md',
        'Widget_System': widgets_dir / 'widget-system.md',
        'Other_APIs': modules_dir / 'other-apis.md'
    }
    
    # Process each category
    categories = categorized_data.get('categories', {})
    processed_content = processed_data.get('processed_content', {})
    
    for category, urls in categories.items():
        print(f"Processing category: {category}")
        
        # Find processed content for this category
        category_content = []
        for url, content in processed_content.items():
            if content.get('category', {}).get('category') == category:
                category_content.append(content)
        
        # Generate markdown
        markdown_content = create_module_markdown(category, category_content, urls)
        
        # Write to file
        output_file = category_files.get(category)
        if output_file:
            print(f"Writing {output_file}")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
        else:
            print(f"Warning: No output file defined for category {category}")
    
    # Create index files
    create_index_files(docs_dir, categories)
    
    print("Documentation organization complete!")

def create_index_files(docs_dir: Path, categories: Dict[str, List[str]]):
    """Create index files for each directory."""
    
    # API index
    api_index = create_frontmatter("API Documentation", "X-Plane SDK API Documentation", "index")
    api_index += "# X-Plane SDK API Documentation\n\n"
    api_index += "This section contains the core X-Plane SDK APIs organized by functionality.\n\n"
    api_index += "## Available API Modules\n\n"
    
    api_categories = [cat for cat in categories.keys() if cat.startswith('XPLM_')]
    for category in sorted(api_categories):
        title = category.replace('XPLM_', '').replace('_', ' ')
        filename = f"xplm-{category.lower().replace('xplm_', '').replace('_', '-')}.md"
        api_index += f"- [{title}](./{filename})\n"
    
    with open(docs_dir / 'api' / 'README.md', 'w', encoding='utf-8') as f:
        f.write(api_index)
    
    # Widgets index
    widgets_index = create_frontmatter("Widget System", "X-Plane SDK Widget System Documentation", "widgets")
    widgets_index += "# X-Plane SDK Widget System\n\n"
    widgets_index += "The Widget System provides UI components for X-Plane plugins.\n\n"
    widgets_index += "## Available Documentation\n\n"
    widgets_index += "- [Widget System](./widget-system.md)\n"
    
    with open(docs_dir / 'widgets' / 'README.md', 'w', encoding='utf-8') as f:
        f.write(widgets_index)
    
    # Modules index
    modules_index = create_frontmatter("Other Modules", "X-Plane SDK Other Modules Documentation", "modules")
    modules_index += "# X-Plane SDK Other Modules\n\n"
    modules_index += "This section contains miscellaneous APIs and utilities.\n\n"
    modules_index += "## Available Documentation\n\n"
    modules_index += "- [Other APIs](./other-apis.md)\n"
    
    with open(docs_dir / 'modules' / 'README.md', 'w', encoding='utf-8') as f:
        f.write(modules_index)

if __name__ == '__main__':
    organize_documentation()