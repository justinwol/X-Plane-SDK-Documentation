#!/usr/bin/env python3
"""
Generate statistics for the documentation organization step.
"""

import os
import json
from pathlib import Path

def main():
    # Load processed content to get total URLs
    with open('raw_data/processed_content.json', encoding='utf-8') as f:
        data = json.load(f)

    total_urls = len(data['processed_content'])
    print(f'Total URLs processed: {total_urls}')

    # Count generated files
    docs_dir = Path('docs')
    api_files = list((docs_dir / 'api').glob('*.md'))
    widget_files = list((docs_dir / 'widgets').glob('*.md'))
    module_files = list((docs_dir / 'modules').glob('*.md'))

    api_docs = [f for f in api_files if f.name != 'README.md']
    widget_docs = [f for f in widget_files if f.name != 'README.md']
    module_docs = [f for f in module_files if f.name != 'README.md']

    print(f'API documentation files: {len(api_docs)}')
    print(f'Widget documentation files: {len(widget_docs)}')
    print(f'Module documentation files: {len(module_docs)}')

    # Calculate total file sizes
    total_size = 0
    file_count = 0
    
    print('\nFile sizes:')
    for file_path in api_docs + widget_docs + module_docs:
        size = file_path.stat().st_size
        total_size += size
        file_count += 1
        print(f'  {file_path.name}: {size:,} bytes')

    print(f'\nSummary:')
    print(f'Total documentation files: {file_count}')
    print(f'Total documentation size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)')
    print(f'Average file size: {total_size/file_count:,.0f} bytes')
    
    # Check for content quality indicators
    print(f'\nContent Quality Indicators:')
    
    # Sample a few files to check for API signatures, code blocks, etc.
    sample_files = api_docs[:3] + widget_docs[:1] + module_docs[:1]
    
    total_api_functions = 0
    total_code_blocks = 0
    
    for file_path in sample_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Count API function signatures (### headers)
        api_functions = content.count('### ')
        total_api_functions += api_functions
        
        # Count code blocks
        code_blocks = content.count('```cpp')
        total_code_blocks += code_blocks
        
        print(f'  {file_path.name}: {api_functions} API functions, {code_blocks} code blocks')
    
    print(f'\nEstimated total API functions documented: ~{total_api_functions * (file_count / len(sample_files)):.0f}')
    print(f'Estimated total code blocks: ~{total_code_blocks * (file_count / len(sample_files)):.0f}')

if __name__ == '__main__':
    main()