"""
Test Runner - Menjalankan semua test cases
Run dengan: python run_all_tests.py
"""

import unittest
import sys
import os
from datetime import datetime


def run_all_tests():
    """Jalankan semua test cases"""
    
    print("=" * 70)
    print("QUIZ PENGUPIL - AUTOMATED TEST SUITE")
    print("=" * 70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Discover semua test files
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Count tests
    test_count = suite.countTestCases()
    print(f"Found {test_count} test cases")
    print()
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 70)
    print("TEST EXECUTION SUMMARY")
    print("=" * 70)
    print(f"Total Tests: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print("=" * 70)
    
    # Known issues
    print("\nKNOWN ISSUES:")
    print("🐛 BUG-001: TC-REG-001 will FAIL - Field 'name' empty in database")
    print("   Location: register.php line 35 (variable $nama vs $name)")
    print("⚠️  ISSUE-001: TC-LOG-003 misleading error message")
    print("   Shows 'Register User Gagal !!' for login failures")
    print("=" * 70)
    
    print(f"\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
