#!/usr/bin/env python3
"""
Test script to validate the content processing fixes.
"""

import sys
import os
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from process_content import extract_api_signatures, extract_code_examples, clean_html_content, convert_to_markdown

def test_define_processing():
    """Test that #define statements are properly handled."""
    print("Testing #define statement processing...")
    
    # Sample HTML with #define statements
    sample_html = '''
    <div class="api">
        <h3>XPLM_MSG_DATAREFS_ADDED</h3>
        <pre><code>#define XPLM_MSG_DATAREFS_ADDED 114</code></pre>
        <p>This message is sent when datarefs are added.</p>
        
        <h3>XPLMSetGraphicsState</h3>
        <pre><code>XPLM_API void XPLMSetGraphicsState(int inEnableFog);</code></pre>
        <p>This function sets the graphics state.</p>
    </div>
    '''
    
    # Test API signature extraction
    signatures = extract_api_signatures(sample_html)
    print(f"Extracted {len(signatures)} API signatures:")
    for sig in signatures:
        print(f"  - {sig.get('name', 'Unknown')}: {sig.get('type', 'function')}")
    
    # Test code example extraction
    examples = extract_code_examples(sample_html)
    print(f"Extracted {len(examples)} code examples:")
    for example in examples:
        print(f"  - {example['type']}: {example['line_count']} lines")
    
    # Test markdown conversion
    cleaned = clean_html_content(sample_html)
    markdown = convert_to_markdown(cleaned)
    print(f"Markdown conversion successful: {len(markdown)} characters")
    
    # Check that #define is in code blocks
    if '```cpp\n#define XPLM_MSG_DATAREFS_ADDED 114\n```' in markdown:
        print("✓ #define statements are properly formatted in code blocks")
    else:
        print("✗ #define statements are not properly formatted")
        print("Markdown content:")
        print(markdown)
    
    return len(signatures) > 0 and len(examples) > 0

def test_frontmatter():
    """Test that frontmatter is properly added."""
    print("\nTesting frontmatter...")
    
    examples_readme = Path(__file__).parent.parent / "docs" / "examples" / "README.md"
    
    if examples_readme.exists():
        with open(examples_readme, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---\n'):
            print("✓ Examples README.md has frontmatter")
            return True
        else:
            print("✗ Examples README.md missing frontmatter")
            return False
    else:
        print("✗ Examples README.md not found")
        return False

def main():
    """Run all tests."""
    print("Running content processing fixes validation...")
    print("=" * 50)
    
    test1_passed = test_define_processing()
    test2_passed = test_frontmatter()
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print(f"  #define processing: {'PASS' if test1_passed else 'FAIL'}")
    print(f"  Frontmatter: {'PASS' if test2_passed else 'FAIL'}")
    
    if test1_passed and test2_passed:
        print("\n✓ All tests passed! Content processing fixes are working.")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())