#!/usr/bin/env python3
"""
X-Plane SDK Documentation Integration Testing Framework

This script provides comprehensive integration testing for the X-Plane SDK
documentation system, including context7 integration, documentation retrieval,
performance benchmarks, and end-to-end workflow validation.

Purpose:
- Test context7.json configuration loading and validation
- Verify documentation structure and accessibility
- Test folder inclusion/exclusion patterns
- Validate metadata and schema compliance
- Benchmark performance metrics
- Test sample queries and retrieval scenarios

Usage:
    python test_integration.py [options]

Dependencies:
    - json: For configuration validation
    - time: For performance benchmarking
    - psutil: For memory usage monitoring
    - pathlib: For file system operations
    - requests: For context7 integration testing (optional)
"""

import json
import os
import sys
import time
import traceback
import psutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
import argparse
import logging

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class IntegrationTestResult:
    """Represents the result of an integration test"""
    def __init__(self, test_name: str, success: bool, message: str = "", 
                 duration: float = 0.0, memory_usage: float = 0.0, details: Dict = None):
        self.test_name = test_name
        self.success = success
        self.message = message
        self.duration = duration
        self.memory_usage = memory_usage
        self.details = details or {}
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def __str__(self):
        status = "✅ PASS" if self.success else "❌ FAIL"
        return f"{status} {self.test_name}: {self.message} ({self.duration:.3f}s)"

class PerformanceBenchmark:
    """Performance benchmarking utilities"""
    def __init__(self):
        self.process = psutil.Process()
        self.start_time = None
        self.start_memory = None

    def start(self):
        """Start performance monitoring"""
        self.start_time = time.time()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB

    def stop(self) -> Tuple[float, float]:
        """Stop monitoring and return (duration, memory_delta)"""
        duration = time.time() - self.start_time if self.start_time else 0.0
        current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        memory_delta = current_memory - (self.start_memory or 0)
        return duration, memory_delta

class XPlaneSDKIntegrationTester:
    """Main integration testing class for X-Plane SDK documentation system"""
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path) if base_path else Path(__file__).parent.parent
        self.test_results: List[IntegrationTestResult] = []
        self.benchmark = PerformanceBenchmark()
        
        # File paths
        self.context7_path = self.base_path / "context7.json"
        self.docs_path = self.base_path / "docs"
        self.raw_data_path = self.base_path / "raw_data"
        self.scripts_path = self.base_path / "scripts"
        self.processed_content_path = self.raw_data_path / "processed_content.json"
        self.scraped_content_path = self.raw_data_path / "scraped_content.json"
        
        # Test configuration
        self.sample_queries = [
            {
                "name": "XPLMCamera Functions",
                "query": "XPLMCamera",
                "expected_modules": ["xplm-camera.md"],
                "expected_functions": ["XPLMControlCamera", "XPLMReadCameraPosition"]
            },
            {
                "name": "Widget System",
                "query": "widget",
                "expected_modules": ["widget-system.md"],
                "expected_functions": ["XPCreateWidget", "XPDestroyWidget"]
            },
            {
                "name": "Graphics API",
                "query": "XPLMGraphics",
                "expected_modules": ["xplm-graphics.md"],
                "expected_functions": ["XPLMSetGraphicsState", "XPLMBindTexture2d"]
            },
            {
                "name": "Data Access",
                "query": "XPLMDataAccess",
                "expected_modules": ["xplm-dataaccess.md"],
                "expected_functions": ["XPLMFindDataRef", "XPLMGetDatai"]
            }
        ]

    def add_test_result(self, result: IntegrationTestResult):
        """Add a test result to the collection"""
        self.test_results.append(result)
        logger.info(str(result))

    def test_context7_configuration(self) -> IntegrationTestResult:
        """Test context7.json configuration loading and validation"""
        self.benchmark.start()
        
        try:
            # Test file existence
            if not self.context7_path.exists():
                duration, memory = self.benchmark.stop()
                return IntegrationTestResult(
                    "Context7 Configuration", False, 
                    f"context7.json not found at {self.context7_path}",
                    duration, memory
                )
            
            # Test JSON loading
            with open(self.context7_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Validate required fields
            required_fields = ['projectTitle', 'description', 'version', 'folders', 'metadata']
            missing_fields = [field for field in required_fields if field not in config]
            
            if missing_fields:
                duration, memory = self.benchmark.stop()
                return IntegrationTestResult(
                    "Context7 Configuration", False,
                    f"Missing required fields: {missing_fields}",
                    duration, memory
                )
            
            # Validate folder structure
            folders = config.get('folders', [])
            missing_folders = []
            for folder in folders:
                folder_path = self.base_path / folder
                if not folder_path.exists():
                    missing_folders.append(folder)
            
            # Validate exclude patterns
            exclude_folders = config.get('excludeFolders', [])
            exclude_files = config.get('excludeFiles', [])
            include_patterns = config.get('includePatterns', [])
            
            # Test metadata completeness
            metadata = config.get('metadata', {})
            expected_metadata = ['sdkVersion', 'xplaneVersion', 'language', 'moduleCount']
            missing_metadata = [field for field in expected_metadata if field not in metadata]
            
            duration, memory = self.benchmark.stop()
            
            details = {
                'config_size': len(json.dumps(config)),
                'folders_count': len(folders),
                'exclude_folders_count': len(exclude_folders),
                'exclude_files_count': len(exclude_files),
                'include_patterns_count': len(include_patterns),
                'missing_folders': missing_folders,
                'missing_metadata': missing_metadata,
                'metadata_completeness': (len(expected_metadata) - len(missing_metadata)) / len(expected_metadata) * 100
            }
            
            if missing_folders:
                return IntegrationTestResult(
                    "Context7 Configuration", False,
                    f"Missing folders: {missing_folders}",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Context7 Configuration", True,
                f"Configuration valid with {len(folders)} folders configured",
                duration, memory, details
            )
            
        except json.JSONDecodeError as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Context7 Configuration", False,
                f"Invalid JSON format: {str(e)}",
                duration, memory
            )
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Context7 Configuration", False,
                f"Unexpected error: {str(e)}",
                duration, memory
            )

    def test_documentation_structure(self) -> IntegrationTestResult:
        """Test documentation structure and file accessibility"""
        self.benchmark.start()
        
        try:
            if not self.docs_path.exists():
                duration, memory = self.benchmark.stop()
                return IntegrationTestResult(
                    "Documentation Structure", False,
                    f"Documentation directory not found: {self.docs_path}",
                    duration, memory
                )
            
            # Expected structure
            expected_dirs = ['api', 'widgets', 'modules', 'examples']
            missing_dirs = []
            existing_dirs = []
            
            for dir_name in expected_dirs:
                dir_path = self.docs_path / dir_name
                if dir_path.exists():
                    existing_dirs.append(dir_name)
                else:
                    missing_dirs.append(dir_name)
            
            # Count markdown files
            markdown_files = list(self.docs_path.rglob("*.md"))
            api_files = list((self.docs_path / "api").glob("*.md")) if (self.docs_path / "api").exists() else []
            widget_files = list((self.docs_path / "widgets").glob("*.md")) if (self.docs_path / "widgets").exists() else []
            
            # Test file accessibility
            accessible_files = 0
            inaccessible_files = []
            
            for md_file in markdown_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if len(content) > 0:
                            accessible_files += 1
                        else:
                            inaccessible_files.append(str(md_file))
                except Exception as e:
                    inaccessible_files.append(f"{md_file}: {str(e)}")
            
            duration, memory = self.benchmark.stop()
            
            details = {
                'total_markdown_files': len(markdown_files),
                'api_files': len(api_files),
                'widget_files': len(widget_files),
                'accessible_files': accessible_files,
                'inaccessible_files': len(inaccessible_files),
                'existing_directories': existing_dirs,
                'missing_directories': missing_dirs,
                'accessibility_rate': (accessible_files / len(markdown_files) * 100) if markdown_files else 0
            }
            
            if missing_dirs:
                return IntegrationTestResult(
                    "Documentation Structure", False,
                    f"Missing directories: {missing_dirs}",
                    duration, memory, details
                )
            
            if inaccessible_files:
                return IntegrationTestResult(
                    "Documentation Structure", False,
                    f"{len(inaccessible_files)} files inaccessible",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Documentation Structure", True,
                f"Structure valid: {len(markdown_files)} files accessible",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Documentation Structure", False,
                f"Error testing structure: {str(e)}",
                duration, memory
            )

    def test_folder_patterns(self) -> IntegrationTestResult:
        """Test folder inclusion/exclusion patterns"""
        self.benchmark.start()
        
        try:
            # Load context7 config
            with open(self.context7_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            include_folders = config.get('folders', [])
            exclude_folders = config.get('excludeFolders', [])
            exclude_files = config.get('excludeFiles', [])
            include_patterns = config.get('includePatterns', [])
            
            # Test inclusion patterns
            included_files = []
            for folder in include_folders:
                folder_path = self.base_path / folder
                if folder_path.exists():
                    for pattern in include_patterns:
                        files = list(folder_path.rglob(pattern))
                        included_files.extend(files)
            
            # Test exclusion patterns
            excluded_folders_found = []
            for exclude_folder in exclude_folders:
                folder_path = self.base_path / exclude_folder
                if folder_path.exists():
                    excluded_folders_found.append(exclude_folder)
            
            # Test file exclusion patterns
            all_files = list(self.base_path.rglob("*"))
            excluded_files_count = 0
            
            for file_path in all_files:
                if file_path.is_file():
                    for exclude_pattern in exclude_files:
                        if file_path.match(exclude_pattern):
                            excluded_files_count += 1
                            break
            
            duration, memory = self.benchmark.stop()
            
            details = {
                'included_files_count': len(included_files),
                'excluded_folders_found': len(excluded_folders_found),
                'excluded_files_count': excluded_files_count,
                'include_patterns': include_patterns,
                'exclude_folders': exclude_folders,
                'exclude_files': exclude_files,
                'pattern_effectiveness': (excluded_files_count / len(all_files) * 100) if all_files else 0
            }
            
            if len(included_files) == 0:
                return IntegrationTestResult(
                    "Folder Patterns", False,
                    "No files matched inclusion patterns",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Folder Patterns", True,
                f"Patterns working: {len(included_files)} included, {excluded_files_count} excluded",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Folder Patterns", False,
                f"Error testing patterns: {str(e)}",
                duration, memory
            )

    def test_metadata_compliance(self) -> IntegrationTestResult:
        """Test metadata and schema compliance"""
        self.benchmark.start()
        
        try:
            # Load and validate context7 metadata
            with open(self.context7_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            metadata = config.get('metadata', {})
            
            # Required metadata fields
            required_fields = {
                'sdkVersion': str,
                'xplaneVersion': str,
                'language': str,
                'platform': str,
                'lastUpdated': str,
                'moduleCount': int,
                'apiCategories': list
            }
            
            missing_fields = []
            invalid_types = []
            
            for field, expected_type in required_fields.items():
                if field not in metadata:
                    missing_fields.append(field)
                elif not isinstance(metadata[field], expected_type):
                    invalid_types.append(f"{field}: expected {expected_type.__name__}, got {type(metadata[field]).__name__}")
            
            # Validate API categories
            api_categories = metadata.get('apiCategories', [])
            expected_categories = [
                "Camera", "Data Access", "Display", "Graphics", "Instance",
                "Map", "Menus", "Navigation", "Planes", "Plugin",
                "Processing", "Scenery", "Sound", "Utilities"
            ]
            
            missing_categories = [cat for cat in expected_categories if cat not in api_categories]
            extra_categories = [cat for cat in api_categories if cat not in expected_categories]
            
            # Validate structure metadata
            structure = config.get('structure', {})
            expected_structure_keys = ['api', 'widgets', 'modules', 'examples']
            missing_structure = [key for key in expected_structure_keys if key not in structure]
            
            duration, memory = self.benchmark.stop()
            
            details = {
                'metadata_fields_count': len(metadata),
                'missing_fields': missing_fields,
                'invalid_types': invalid_types,
                'api_categories_count': len(api_categories),
                'missing_categories': missing_categories,
                'extra_categories': extra_categories,
                'structure_completeness': (len(expected_structure_keys) - len(missing_structure)) / len(expected_structure_keys) * 100,
                'metadata_completeness': (len(required_fields) - len(missing_fields)) / len(required_fields) * 100
            }
            
            if missing_fields or invalid_types:
                return IntegrationTestResult(
                    "Metadata Compliance", False,
                    f"Metadata issues: {len(missing_fields)} missing, {len(invalid_types)} invalid types",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Metadata Compliance", True,
                f"Metadata compliant: {len(api_categories)} categories, {len(structure)} structure elements",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Metadata Compliance", False,
                f"Error validating metadata: {str(e)}",
                duration, memory
            )

    def test_sample_queries(self) -> IntegrationTestResult:
        """Test sample queries for documentation retrieval"""
        self.benchmark.start()
        
        try:
            # Load processed content if available
            processed_content = {}
            if self.processed_content_path.exists():
                with open(self.processed_content_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    processed_content = data.get('processed_content', {})
            
            query_results = []
            
            for query_config in self.sample_queries:
                query_name = query_config['name']
                query_term = query_config['query']
                expected_modules = query_config['expected_modules']
                expected_functions = query_config['expected_functions']
                
                # Search in documentation files
                found_modules = []
                found_functions = []
                
                # Search markdown files
                for md_file in self.docs_path.rglob("*.md"):
                    try:
                        with open(md_file, 'r', encoding='utf-8') as f:
                            content = f.read().lower()
                            
                        if query_term.lower() in content:
                            found_modules.append(md_file.name)
                            
                        # Search for expected functions
                        for func in expected_functions:
                            if func.lower() in content:
                                found_functions.append(func)
                                
                    except Exception:
                        continue
                
                # Search in processed content
                for url, content_data in processed_content.items():
                    api_signatures = content_data.get('api_signatures', [])
                    for signature in api_signatures:
                        func_name = signature.get('name', '')
                        if query_term.lower() in func_name.lower():
                            if func_name not in found_functions:
                                found_functions.append(func_name)
                
                query_result = {
                    'query': query_name,
                    'term': query_term,
                    'found_modules': list(set(found_modules)),
                    'found_functions': list(set(found_functions)),
                    'expected_modules': expected_modules,
                    'expected_functions': expected_functions,
                    'module_match_rate': len(set(found_modules) & set(expected_modules)) / len(expected_modules) * 100 if expected_modules else 0,
                    'function_match_rate': len(set(found_functions) & set(expected_functions)) / len(expected_functions) * 100 if expected_functions else 0
                }
                
                query_results.append(query_result)
            
            duration, memory = self.benchmark.stop()
            
            # Calculate overall success metrics
            total_queries = len(self.sample_queries)
            successful_queries = sum(1 for result in query_results if result['module_match_rate'] > 0 or result['function_match_rate'] > 0)
            
            details = {
                'total_queries': total_queries,
                'successful_queries': successful_queries,
                'query_results': query_results,
                'success_rate': (successful_queries / total_queries * 100) if total_queries else 0,
                'average_module_match': sum(r['module_match_rate'] for r in query_results) / total_queries if total_queries else 0,
                'average_function_match': sum(r['function_match_rate'] for r in query_results) / total_queries if total_queries else 0
            }
            
            if successful_queries == 0:
                return IntegrationTestResult(
                    "Sample Queries", False,
                    "No queries returned results",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Sample Queries", True,
                f"{successful_queries}/{total_queries} queries successful",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Sample Queries", False,
                f"Error testing queries: {str(e)}",
                duration, memory
            )

    def test_performance_benchmarks(self) -> IntegrationTestResult:
        """Test performance benchmarks for documentation loading and search"""
        self.benchmark.start()
        
        try:
            benchmarks = {}
            
            # Benchmark 1: Context7 config loading
            start_time = time.time()
            with open(self.context7_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            config_load_time = time.time() - start_time
            benchmarks['config_load_time'] = config_load_time
            
            # Benchmark 2: Documentation file enumeration
            start_time = time.time()
            markdown_files = list(self.docs_path.rglob("*.md"))
            file_enum_time = time.time() - start_time
            benchmarks['file_enumeration_time'] = file_enum_time
            benchmarks['files_enumerated'] = len(markdown_files)
            
            # Benchmark 3: Documentation loading
            start_time = time.time()
            total_content_size = 0
            loaded_files = 0
            
            for md_file in markdown_files[:10]:  # Test first 10 files
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        total_content_size += len(content)
                        loaded_files += 1
                except Exception:
                    continue
            
            doc_load_time = time.time() - start_time
            benchmarks['doc_load_time'] = doc_load_time
            benchmarks['loaded_files'] = loaded_files
            benchmarks['total_content_size'] = total_content_size
            
            # Benchmark 4: Search performance
            start_time = time.time()
            search_results = 0
            search_term = "XPLM"
            
            for md_file in markdown_files[:5]:  # Search in first 5 files
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if search_term in content:
                            search_results += 1
                except Exception:
                    continue
            
            search_time = time.time() - start_time
            benchmarks['search_time'] = search_time
            benchmarks['search_results'] = search_results
            
            # Benchmark 5: Processed content loading
            if self.processed_content_path.exists():
                start_time = time.time()
                with open(self.processed_content_path, 'r', encoding='utf-8') as f:
                    processed_data = json.load(f)
                processed_load_time = time.time() - start_time
                benchmarks['processed_content_load_time'] = processed_load_time
                benchmarks['processed_content_size'] = len(json.dumps(processed_data))
            
            duration, memory = self.benchmark.stop()
            
            # Performance thresholds (in seconds)
            thresholds = {
                'config_load_time': 0.1,
                'file_enumeration_time': 1.0,
                'doc_load_time': 2.0,
                'search_time': 1.0,
                'processed_content_load_time': 0.5
            }
            
            performance_issues = []
            for metric, threshold in thresholds.items():
                if metric in benchmarks and benchmarks[metric] > threshold:
                    performance_issues.append(f"{metric}: {benchmarks[metric]:.3f}s > {threshold}s")
            
            details = {
                'benchmarks': benchmarks,
                'performance_issues': performance_issues,
                'total_test_duration': duration,
                'memory_usage': memory,
                'throughput_files_per_second': loaded_files / doc_load_time if doc_load_time > 0 else 0,
                'throughput_bytes_per_second': total_content_size / doc_load_time if doc_load_time > 0 else 0
            }
            
            if performance_issues:
                return IntegrationTestResult(
                    "Performance Benchmarks", False,
                    f"{len(performance_issues)} performance issues detected",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "Performance Benchmarks", True,
                f"All benchmarks within thresholds (total: {duration:.3f}s)",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "Performance Benchmarks", False,
                f"Error running benchmarks: {str(e)}",
                duration, memory
            )

    def test_end_to_end_workflow(self) -> IntegrationTestResult:
        """Test end-to-end workflow integration"""
        self.benchmark.start()
        
        try:
            workflow_steps = []
            
            # Step 1: Load configuration
            try:
                with open(self.context7_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                workflow_steps.append(("Load Configuration", True, "Configuration loaded successfully"))
            except Exception as e:
                workflow_steps.append(("Load Configuration", False, str(e)))
            
            # Step 2: Validate documentation structure
            try:
                docs_exist = self.docs_path.exists()
                markdown_files = list(self.docs_path.rglob("*.md")) if docs_exist else []
                workflow_steps.append(("Validate Structure", docs_exist, f"Found {len(markdown_files)} markdown files"))
            except Exception as e:
                workflow_steps.append(("Validate Structure", False, str(e)))
            
            # Step 3: Test content accessibility
            try:
                accessible_count = 0
                for md_file in markdown_files[:5]:  # Test first 5 files
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if len(content) > 0:
                            accessible_count += 1
                workflow_steps.append(("Content Access", accessible_count > 0, f"{accessible_count} files accessible"))
            except Exception as e:
                workflow_steps.append(("Content Access", False, str(e)))
            
            # Step 4: Test processed content integration
            try:
                if self.processed_content_path.exists():
                    with open(self.processed_content_path, 'r', encoding='utf-8') as f:
                        processed_data = json.load(f)
                    api_count = sum(len(content.get('api_signatures', [])) for content in processed_data.get('processed_content', {}).values())
                    workflow_steps.append(("Processed Content", True, f"Found {api_count} API signatures"))
                else:
                    workflow_steps.append(("Processed Content", False, "Processed content file not found"))
            except Exception as e:
                workflow_steps.append(("Processed Content", False, str(e)))
            
            # Step 5: Test search functionality
            try:
                search_results = 0
                search_term = "XPLM"
                for md_file in markdown_files[:3]:  # Search in first 3 files
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if search_term in content:
                            search_results += 1
                workflow_steps.append(("Search Functionality", search_results > 0, f"Found {search_results} matches"))
            except Exception as e:
                workflow_steps.append(("Search Functionality", False, str(e)))
            
            duration, memory = self.benchmark.stop()
            
            successful_steps = sum(1 for _, success, _ in workflow_steps if success)
            total_steps = len(workflow_steps)
            
            details = {
                'workflow_steps': workflow_steps,
                'successful_steps': successful_steps,
                'total_steps': total_steps,
                'success_rate': (successful_steps / total_steps * 100) if total_steps else 0,
                'workflow_duration': duration
            }
            
            if successful_steps < total_steps:
                failed_steps = [step for step, success, _ in workflow_steps if not success]
                return IntegrationTestResult(
                    "End-to-End Workflow", False,
                    f"{len(failed_steps)} workflow steps failed: {failed_steps}",
                    duration, memory, details
                )
            
            return IntegrationTestResult(
                "End-to-End Workflow", True,
                f"All {total_steps} workflow steps successful",
                duration, memory, details
            )
            
        except Exception as e:
            duration, memory = self.benchmark.stop()
            return IntegrationTestResult(
                "End-to-End Workflow", False,
                f"Workflow error: {str(e)}",
                duration, memory
            )

    def run_all_tests(self) -> Dict[str, Any]:
        """Run all integration tests and return comprehensive results"""
        print("🚀 Starting X-Plane SDK Documentation Integration Tests")
        print("=" * 70)
        
        # Run all test categories
        test_methods = [
            self.test_context7_configuration,
            self.test_documentation_structure,
            self.test_folder_patterns,
            self.test_metadata_compliance,
            self.test_sample_queries,
            self.test_performance_benchmarks,
            self.test_end_to_end_workflow
        ]
        
        for test_method in test_methods:
            try:
                result = test_method()
                self.add_test_result(result)
            except Exception as e:
                error_result = IntegrationTestResult(
                    test_method.__name__, False,
                    f"Test execution error: {str(e)}",
                    0.0, 0.0
                )
                self.add_test_result(error_result)
        
        # Generate comprehensive report
        return self.generate_integration_report()

    def generate_integration_report(self) -> Dict[str, Any]:
        """Generate comprehensive integration test report"""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result.success)
        failed_tests = total_tests - passed_tests
        
        total_duration = sum(result.duration for result in self.test_results)
        total_memory = sum(result.memory_usage for result in self.test_results)
        
        report = {
            'integration_test_summary': {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'tester_version': '1.0.0',
                'total_tests': total_tests,
                'passed_tests': passed_tests,
                'failed_tests': failed_tests,
                'success_rate': (passed_tests / total_tests * 100) if total_tests else 0,
                'total_duration': total_duration,
                'total_memory_usage': total_memory,
                'tests_passed': failed_tests == 0
            },
            'test_results': [
                {
                    'test_name': result.test_name,
                    'success': result.success,
                    'message': result.message,
                    'duration': result.duration,
                    'memory_usage': result.memory_usage,
                    'timestamp': result.timestamp,
                    'details': result.details
                }
                for result in self.test_results
            ],
            'performance_summary': {
                'fastest_test': min(self.test_results, key=lambda x: x.duration).test_name if self.test_results else None,
                'slowest_test': max(self.test_results, key=lambda x: x.duration).test_name if self.test_results else None,
                'average_duration': total_duration / total_tests if total_tests else 0,
                'memory_efficient_test': min(self.test_results, key=lambda x: x.memory_usage).test_name if self.test_results else None,
                'memory_intensive_test': max(self.test_results, key=lambda x: x.memory_usage).test_name if self.test_results else None,
                'average_memory_usage': total_memory / total_tests if total_tests else 0
            },
            'recommendations': self._generate_integration_recommendations()
        }
        
        return report

    def _generate_integration_recommendations(self) -> List[str]:
        """Generate recommendations based on integration test results"""
        recommendations = []
        
        failed_tests = [result for result in self.test_results if not result.success]
        
        if failed_tests:
            recommendations.append(f"Fix {len(failed_tests)} failing integration tests before deployment")
            
            # Specific recommendations based on failed tests
            for result in failed_tests:
                if "Context7 Configuration" in result.test_name:
                    recommendations.append("Review and fix context7.json configuration issues")
                elif "Documentation Structure" in result.test_name:
                    recommendations.append("Ensure all required documentation directories and files exist")
                elif "Sample Queries" in result.test_name:
                    recommendations.append("Improve content processing to ensure searchable content")
                elif "Performance" in result.test_name:
                    recommendations.append("Optimize system performance for better response times")
        
        # Performance recommendations
        slow_tests = [result for result in self.test_results if result.duration > 5.0]
        if slow_tests:
            recommendations.append(f"Optimize {len(slow_tests)} slow-performing tests")
        
        memory_intensive = [result for result in self.test_results if result.memory_usage > 100.0]
        if memory_intensive:
            recommendations.append(f"Optimize memory usage for {len(memory_intensive)} memory-intensive tests")
        
        if not failed_tests and not slow_tests:
            recommendations.append("All integration tests passing - system ready for production use")
        
        return recommendations

def main():
    """Main entry point for integration testing"""
    parser = argparse.ArgumentParser(description='X-Plane SDK Documentation Integration Tester')
    parser.add_argument('--base-path', type=str, help='Base path for documentation system')
    parser.add_argument('--output', type=str, default='integration_test_report.json',
                       help='Output file for test report')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--test', type=str, help='Run specific test only')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        tester = XPlaneSDKIntegrationTester(args.base_path)
        
        if args.test:
            # Run specific test
            test_methods = {
                'context7': tester.test_context7_configuration,
                'structure': tester.test_documentation_structure,
                'patterns': tester.test_folder_patterns,
                'metadata': tester.test_metadata_compliance,
                'queries': tester.test_sample_queries,
                'performance': tester.test_performance_benchmarks,
                'workflow': tester.test_end_to_end_workflow
            }
            
            if args.test in test_methods:
                result = test_methods[args.test]()
                tester.add_test_result(result)
                report = tester.generate_integration_report()
            else:
                print(f"❌ Unknown test: {args.test}")
                print(f"Available tests: {', '.join(test_methods.keys())}")
                return 1
        else:
            # Run all tests
            report = tester.run_all_tests()
        
        # Save report
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Print summary
        print("\n" + "=" * 70)
        print("📊 INTEGRATION TEST SUMMARY")
        print("=" * 70)
        
        summary = report['integration_test_summary']
        print(f"Total Tests: {summary['total_tests']}")
        print(f"Passed: {summary['passed_tests']}")
        print(f"Failed: {summary['failed_tests']}")
        print(f"Success Rate: {summary['success_rate']:.1f}%")
        print(f"Total Duration: {summary['total_duration']:.3f}s")
        print(f"Memory Usage: {summary['total_memory_usage']:.1f}MB")
        
        if summary['tests_passed']:
            print("\n✅ All integration tests PASSED!")
        else:
            print(f"\n❌ {summary['failed_tests']} integration tests FAILED!")
            print("\nFailed tests:")
            for result in tester.test_results:
                if not result.success:
                    print(f"  - {result.test_name}: {result.message}")
        
        print(f"\n📄 Detailed report saved to: {output_path}")
        
        # Print recommendations
        recommendations = report['recommendations']
        if recommendations:
            print("\n💡 RECOMMENDATIONS:")
            for i, rec in enumerate(recommendations, 1):
                print(f"  {i}. {rec}")
        
        return 0 if summary['tests_passed'] else 1
        
    except Exception as e:
        print(f"❌ Integration testing failed: {str(e)}")
        if args.verbose:
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())