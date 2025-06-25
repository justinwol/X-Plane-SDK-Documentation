#!/usr/bin/env python3
"""
X-Plane SDK Documentation Validator

This script validates the processed X-Plane SDK documentation for
completeness, accuracy, and integrity. It performs various checks
to ensure the documentation meets quality standards.

Purpose:
- Validate documentation completeness and structure
- Check for broken links and missing references
- Verify code examples and syntax
- Ensure consistent formatting and standards
- Generate validation reports and quality metrics

Usage:
    python validate_docs.py [options]

Dependencies:
    - requests: For link validation
    - beautifulsoup4: For content structure validation
    - json: For data validation
    - re: For pattern matching
    - os: For file system operations
    - pathlib: For path handling
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
import argparse

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

class ValidationError:
    """Represents a validation error with context"""
    def __init__(self, error_type: str, message: str, file_path: str = None, line_number: int = None, severity: str = "error"):
        self.error_type = error_type
        self.message = message
        self.file_path = file_path
        self.line_number = line_number
        self.severity = severity
        self.timestamp = datetime.now().isoformat()

    def __str__(self):
        location = ""
        if self.file_path:
            location = f" in {self.file_path}"
            if self.line_number:
                location += f":{self.line_number}"
        return f"[{self.severity.upper()}] {self.error_type}: {self.message}{location}"

class DocumentationValidator:
    """Main validation class for X-Plane SDK documentation"""
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path) if base_path else Path(__file__).parent.parent
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        self.stats = {
            'total_urls': 0,
            'processed_urls': 0,
            'failed_urls': 0,
            'markdown_files': 0,
            'api_functions': 0,
            'code_examples': 0,
            'cross_references': 0,
            'validation_errors': 0,
            'validation_warnings': 0
        }
        
        # File paths
        self.sdk_map_path = self.base_path.parent / "sdk_map_optimized.txt"
        self.scraped_content_path = self.base_path / "raw_data" / "scraped_content.json"
        self.processed_content_path = self.base_path / "raw_data" / "processed_content.json"
        self.categorized_urls_path = self.base_path / "raw_data" / "categorized_urls.json"
        self.context7_path = self.base_path / "context7.json"
        self.docs_path = self.base_path / "docs"

    def add_error(self, error_type: str, message: str, file_path: str = None, line_number: int = None, severity: str = "error"):
        """Add a validation error or warning"""
        error = ValidationError(error_type, message, file_path, line_number, severity)
        if severity == "warning":
            self.warnings.append(error)
            self.stats['validation_warnings'] += 1
        else:
            self.errors.append(error)
            self.stats['validation_errors'] += 1

    def validate_all_urls_processed(self) -> bool:
        """
        Validate that all URLs from sdk_map_optimized.txt were scraped and processed.
        
        Returns:
            bool: True if all URLs were processed successfully
        """
        print("🔍 Validating URL processing completeness...")
        
        # Load original URLs
        if not self.sdk_map_path.exists():
            self.add_error("FILE_MISSING", f"SDK map file not found: {self.sdk_map_path}")
            return False
            
        with open(self.sdk_map_path, 'r', encoding='utf-8') as f:
            original_urls = set(line.strip() for line in f if line.strip())
        
        self.stats['total_urls'] = len(original_urls)
        print(f"  📊 Total URLs in SDK map: {self.stats['total_urls']}")
        
        # Load scraped content
        if not self.scraped_content_path.exists():
            self.add_error("FILE_MISSING", f"Scraped content file not found: {self.scraped_content_path}")
            return False
            
        with open(self.scraped_content_path, 'r', encoding='utf-8') as f:
            scraped_data = json.load(f)
        
        scraped_urls = set(scraped_data.get('scraped_content', {}).keys())
        self.stats['processed_urls'] = len(scraped_urls)
        print(f"  📊 URLs successfully scraped: {self.stats['processed_urls']}")
        
        # Check for missing URLs
        missing_urls = original_urls - scraped_urls
        if missing_urls:
            self.stats['failed_urls'] = len(missing_urls)
            self.add_error("MISSING_URLS", f"Found {len(missing_urls)} URLs that were not scraped")
            for url in sorted(missing_urls)[:10]:  # Show first 10
                self.add_error("URL_NOT_SCRAPED", f"URL not scraped: {url}", severity="warning")
            if len(missing_urls) > 10:
                self.add_error("URL_NOT_SCRAPED", f"... and {len(missing_urls) - 10} more URLs", severity="warning")
        
        # Check for extra URLs
        extra_urls = scraped_urls - original_urls
        if extra_urls:
            self.add_error("EXTRA_URLS", f"Found {len(extra_urls)} URLs that were scraped but not in original list", severity="warning")
        
        # Validate scraped content quality
        for url, content_data in scraped_data.get('scraped_content', {}).items():
            if not content_data.get('success', False):
                self.add_error("SCRAPING_FAILED", f"Scraping failed for URL: {url}")
            elif not content_data.get('content'):
                self.add_error("EMPTY_CONTENT", f"Empty content for URL: {url}")
            elif len(content_data.get('content', '')) < 100:
                self.add_error("MINIMAL_CONTENT", f"Very short content for URL: {url}", severity="warning")
        
        success_rate = (self.stats['processed_urls'] / self.stats['total_urls']) * 100 if self.stats['total_urls'] > 0 else 0
        print(f"  ✅ URL processing success rate: {success_rate:.1f}%")
        
        return len(missing_urls) == 0

    def validate_markdown_format(self) -> bool:
        """
        Validate markdown format and structure in all generated documentation files.
        
        Returns:
            bool: True if all markdown files are properly formatted
        """
        print("🔍 Validating markdown format and structure...")
        
        if not self.docs_path.exists():
            self.add_error("DIRECTORY_MISSING", f"Documentation directory not found: {self.docs_path}")
            return False
        
        markdown_files = list(self.docs_path.rglob("*.md"))
        self.stats['markdown_files'] = len(markdown_files)
        print(f"  📊 Found {len(markdown_files)} markdown files")
        
        valid_files = 0
        
        for md_file in markdown_files:
            file_valid = True
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check frontmatter
                if content.startswith('---'):
                    frontmatter_end = content.find('---', 3)
                    if frontmatter_end == -1:
                        self.add_error("INVALID_FRONTMATTER", "Frontmatter not properly closed", str(md_file))
                        file_valid = False
                    else:
                        frontmatter = content[3:frontmatter_end]
                        # Basic YAML validation
                        if 'title:' not in frontmatter:
                            self.add_error("MISSING_TITLE", "Frontmatter missing title field", str(md_file))
                            file_valid = False
                else:
                    self.add_error("MISSING_FRONTMATTER", "File missing frontmatter", str(md_file))
                    file_valid = False
                
                # Check for proper heading hierarchy
                lines = content.split('\n')
                heading_levels = []
                in_code_block = False
                code_block_pattern = re.compile(r'^```')
                
                for i, line in enumerate(lines, 1):
                    # Track code block state
                    if code_block_pattern.match(line):
                        in_code_block = not in_code_block
                        continue
                    
                    # Only check headings outside of code blocks
                    if line.startswith('#') and not in_code_block:
                        level = len(line) - len(line.lstrip('#'))
                        heading_levels.append((level, i))
                        
                        # Check for proper heading format
                        if not line.strip().endswith('#') and '# ' not in line:
                            if not re.match(r'^#+\s+.+', line):
                                self.add_error("INVALID_HEADING", f"Malformed heading: {line.strip()}", str(md_file), i)
                                file_valid = False
                
                # Check heading hierarchy
                for i in range(1, len(heading_levels)):
                    prev_level, prev_line = heading_levels[i-1]
                    curr_level, curr_line = heading_levels[i]
                    if curr_level > prev_level + 1:
                        self.add_error("HEADING_HIERARCHY", f"Heading level jumps from {prev_level} to {curr_level}", str(md_file), curr_line, "warning")
                
                # Check for code blocks
                code_blocks = re.findall(r'```(\w+)?\n(.*?)\n```', content, re.DOTALL)
                for lang, code in code_blocks:
                    if not lang:
                        self.add_error("MISSING_LANGUAGE", "Code block missing language specification", str(md_file), severity="warning")
                    elif lang.lower() in ['c', 'cpp', 'c++'] and 'XPLM' in code:
                        # Basic C/C++ syntax check for XPLM functions
                        if not re.search(r'XPLM\w+\s*\(', code):
                            self.add_error("INVALID_API_SYNTAX", "Possible malformed XPLM API call", str(md_file), severity="warning")
                
                # Check for internal links
                internal_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                for link_text, link_url in internal_links:
                    if link_url.startswith('./') or link_url.startswith('../'):
                        # Check if referenced file exists
                        target_path = (md_file.parent / link_url).resolve()
                        if not target_path.exists():
                            self.add_error("BROKEN_LINK", f"Broken internal link: {link_url}", str(md_file))
                            file_valid = False
                
                if file_valid:
                    valid_files += 1
                    
            except Exception as e:
                self.add_error("FILE_READ_ERROR", f"Error reading file: {str(e)}", str(md_file))
                file_valid = False
        
        print(f"  ✅ Valid markdown files: {valid_files}/{len(markdown_files)}")
        return valid_files == len(markdown_files)

    def validate_context7_compliance(self) -> bool:
        """
        Validate context7.json format and schema compliance.
        
        Returns:
            bool: True if context7.json is properly configured
        """
        print("🔍 Validating Context7 compliance...")
        
        if not self.context7_path.exists():
            self.add_error("FILE_MISSING", f"Context7 config file not found: {self.context7_path}")
            return False
        
        try:
            with open(self.context7_path, 'r', encoding='utf-8') as f:
                context7_config = json.load(f)
        except json.JSONDecodeError as e:
            self.add_error("INVALID_JSON", f"Context7 config is not valid JSON: {str(e)}", str(self.context7_path))
            return False
        
        # Required fields
        required_fields = ['projectTitle', 'description', 'version', 'folders']
        for field in required_fields:
            if field not in context7_config:
                self.add_error("MISSING_FIELD", f"Context7 config missing required field: {field}", str(self.context7_path))
        
        # Validate folders exist
        for folder in context7_config.get('folders', []):
            folder_path = self.base_path / folder
            if not folder_path.exists():
                self.add_error("MISSING_FOLDER", f"Specified folder does not exist: {folder}", str(self.context7_path))
        
        # Validate exclude patterns work
        exclude_folders = context7_config.get('excludeFolders', [])
        exclude_files = context7_config.get('excludeFiles', [])
        
        # Check that excluded folders are actually excluded
        for exclude_folder in exclude_folders:
            folder_path = self.base_path / exclude_folder
            if folder_path.exists():
                print(f"  ✅ Excluded folder exists and will be ignored: {exclude_folder}")
        
        # Validate include patterns
        include_patterns = context7_config.get('includePatterns', [])
        if '*.md' not in include_patterns:
            self.add_error("MISSING_PATTERN", "Context7 config should include '*.md' pattern", str(self.context7_path), severity="warning")
        
        # Validate metadata
        metadata = context7_config.get('metadata', {})
        expected_metadata = ['sdkVersion', 'xplaneVersion', 'language', 'moduleCount']
        for field in expected_metadata:
            if field not in metadata:
                self.add_error("MISSING_METADATA", f"Context7 metadata missing field: {field}", str(self.context7_path), severity="warning")
        
        print("  ✅ Context7 configuration validated")
        return True

    def check_content_quality(self) -> bool:
        """
        Check content quality including code examples, API signatures, and cross-references.
        
        Returns:
            bool: True if content quality meets standards
        """
        print("🔍 Checking content quality...")
        
        # Load processed content
        if not self.processed_content_path.exists():
            self.add_error("FILE_MISSING", f"Processed content file not found: {self.processed_content_path}")
            return False
        
        with open(self.processed_content_path, 'r', encoding='utf-8') as f:
            processed_data = json.load(f)
        
        processed_content = processed_data.get('processed_content', {})
        cross_references = processed_data.get('cross_references', {})
        
        self.stats['cross_references'] = len(cross_references)
        
        api_function_count = 0
        code_example_count = 0
        
        for url, content in processed_content.items():
            # Check API signatures
            api_signatures = content.get('api_signatures', [])
            api_function_count += len(api_signatures)
            
            for signature in api_signatures:
                # Validate signature structure
                if 'name' not in signature:
                    self.add_error("MISSING_API_NAME", f"API signature missing name for URL: {url}")
                elif not signature['name'].startswith('XPLM'):
                    self.add_error("INVALID_API_NAME", f"API function name should start with XPLM: {signature['name']}")
                
                if 'parameters' not in signature:
                    self.add_error("MISSING_PARAMETERS", f"API signature missing parameters for: {signature.get('name', 'unknown')}")
                
                if 'description' not in signature or not signature['description']:
                    self.add_error("MISSING_DESCRIPTION", f"API signature missing description for: {signature.get('name', 'unknown')}", severity="warning")
            
            # Check code examples
            code_examples = content.get('code_examples', [])
            code_example_count += len(code_examples)
            
            for example in code_examples:
                if 'code' not in example or not example['code'].strip():
                    self.add_error("EMPTY_CODE_EXAMPLE", f"Empty code example found for URL: {url}")
                elif len(example['code']) < 20:
                    self.add_error("MINIMAL_CODE_EXAMPLE", f"Very short code example for URL: {url}", severity="warning")
                
                # Check for proper C/C++ syntax in XPLM examples
                if 'XPLM' in example.get('code', ''):
                    code = example['code']
                    if not re.search(r'XPLM\w+\s*\(', code):
                        self.add_error("INVALID_CODE_SYNTAX", f"Code example may have syntax issues for URL: {url}", severity="warning")
            
            # Check categorization
            category = content.get('category')
            if not category:
                self.add_error("MISSING_CATEGORY", f"Content missing category for URL: {url}", severity="warning")
            elif isinstance(category, str) and not category.startswith('XPLM_'):
                self.add_error("INVALID_CATEGORY", f"Category should start with XPLM_: {category}", severity="warning")
        
        self.stats['api_functions'] = api_function_count
        self.stats['code_examples'] = code_example_count
        
        print(f"  📊 API functions found: {api_function_count}")
        print(f"  📊 Code examples found: {code_example_count}")
        print(f"  📊 Cross-references: {self.stats['cross_references']}")
        
        # Quality thresholds
        if api_function_count < 50:
            self.add_error("LOW_API_COUNT", f"Low number of API functions found: {api_function_count}", severity="warning")
        
        if code_example_count < 20:
            self.add_error("LOW_EXAMPLE_COUNT", f"Low number of code examples found: {code_example_count}", severity="warning")
        
        print("  ✅ Content quality check completed")
        return True

    def generate_validation_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive validation report.
        
        Returns:
            Dict containing the complete validation report
        """
        print("📋 Generating validation report...")
        
        report = {
            'validation_summary': {
                'timestamp': datetime.now().isoformat(),
                'validator_version': '1.0.0',
                'total_errors': len(self.errors),
                'total_warnings': len(self.warnings),
                'validation_passed': len(self.errors) == 0
            },
            'statistics': self.stats,
            'errors': [
                {
                    'type': error.error_type,
                    'message': error.message,
                    'file': error.file_path,
                    'line': error.line_number,
                    'severity': error.severity,
                    'timestamp': error.timestamp
                }
                for error in self.errors
            ],
            'warnings': [
                {
                    'type': warning.error_type,
                    'message': warning.message,
                    'file': warning.file_path,
                    'line': warning.line_number,
                    'severity': warning.severity,
                    'timestamp': warning.timestamp
                }
                for warning in self.warnings
            ],
            'quality_metrics': {
                'url_processing_rate': (self.stats['processed_urls'] / self.stats['total_urls'] * 100) if self.stats['total_urls'] > 0 else 0,
                'api_function_density': self.stats['api_functions'] / max(self.stats['processed_urls'], 1),
                'code_example_density': self.stats['code_examples'] / max(self.stats['processed_urls'], 1),
                'documentation_completeness': (self.stats['markdown_files'] / 19) * 100,  # Expected 19 files
                'cross_reference_coverage': self.stats['cross_references'] / max(self.stats['processed_urls'], 1)
            },
            'recommendations': self._generate_recommendations()
        }
        
        return report

    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        if self.stats['failed_urls'] > 0:
            recommendations.append(f"Re-run scraping for {self.stats['failed_urls']} failed URLs")
        
        if self.stats['validation_errors'] > 0:
            recommendations.append("Fix validation errors before proceeding with documentation deployment")
        
        if self.stats['api_functions'] < 100:
            recommendations.append("Review content processing to ensure all API functions are extracted")
        
        if self.stats['code_examples'] < 50:
            recommendations.append("Add more code examples to improve documentation quality")
        
        if self.stats['markdown_files'] < 19:
            recommendations.append("Ensure all expected documentation files are generated")
        
        if len(self.warnings) > 10:
            recommendations.append("Review and address validation warnings to improve documentation quality")
        
        if not recommendations:
            recommendations.append("Documentation validation passed successfully - ready for deployment")
        
        return recommendations

    def run_full_validation(self) -> bool:
        """
        Run complete validation suite.
        
        Returns:
            bool: True if all validations pass
        """
        print("🚀 Starting comprehensive X-Plane SDK documentation validation...")
        print("=" * 70)
        
        validation_results = []
        
        # Run all validation checks
        validation_results.append(self.validate_all_urls_processed())
        validation_results.append(self.validate_markdown_format())
        validation_results.append(self.validate_context7_compliance())
        validation_results.append(self.check_content_quality())
        
        # Generate report
        report = self.generate_validation_report()
        
        # Save report
        report_path = self.base_path / "validation_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print("=" * 70)
        print("📊 VALIDATION SUMMARY")
        print("=" * 70)
        print(f"Total URLs: {self.stats['total_urls']}")
        print(f"Processed URLs: {self.stats['processed_urls']}")
        print(f"Failed URLs: {self.stats['failed_urls']}")
        print(f"Markdown Files: {self.stats['markdown_files']}")
        print(f"API Functions: {self.stats['api_functions']}")
        print(f"Code Examples: {self.stats['code_examples']}")
        print(f"Cross References: {self.stats['cross_references']}")
        print(f"Validation Errors: {len(self.errors)}")
        print(f"Validation Warnings: {len(self.warnings)}")
        
        print("\n📈 QUALITY METRICS")
        print("=" * 70)
        for metric, value in report['quality_metrics'].items():
            print(f"{metric.replace('_', ' ').title()}: {value:.1f}{'%' if 'rate' in metric or 'completeness' in metric else ''}")
        
        if self.errors:
            print("\n❌ VALIDATION ERRORS")
            print("=" * 70)
            for error in self.errors[:10]:  # Show first 10 errors
                print(f"  • {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more errors")
        
        if self.warnings:
            print("\n⚠️  VALIDATION WARNINGS")
            print("=" * 70)
            for warning in self.warnings[:5]:  # Show first 5 warnings
                print(f"  • {warning}")
            if len(self.warnings) > 5:
                print(f"  ... and {len(self.warnings) - 5} more warnings")
        
        print("\n💡 RECOMMENDATIONS")
        print("=" * 70)
        for rec in report['recommendations']:
            print(f"  • {rec}")
        
        print(f"\n📄 Full validation report saved to: {report_path}")
        
        overall_success = all(validation_results) and len(self.errors) == 0
        
        if overall_success:
            print("\n✅ VALIDATION PASSED - Documentation is ready for deployment!")
        else:
            print("\n❌ VALIDATION FAILED - Please address errors before proceeding")
        
        return overall_success

def main():
    """Main entry point for the validation script"""
    parser = argparse.ArgumentParser(description='Validate X-Plane SDK Documentation')
    parser.add_argument('--base-path', help='Base path for documentation project')
    parser.add_argument('--report-only', action='store_true', help='Generate report without running validations')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    validator = DocumentationValidator(args.base_path)
    
    try:
        success = validator.run_full_validation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Validation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Validation failed with error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()