
from base_test import BaseTest


class TestLoginAllFieldsEmpty(BaseTest):
    
    def test_login_all_fields_empty(self):
        print("\n[TC-LOG-004] Testing: Login dengan Semua Field Kosong")
        
        self.navigate_to_login()
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_004_all_empty")
        
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error")


if __name__ == "__main__":
    import unittest
    unittest.main()
