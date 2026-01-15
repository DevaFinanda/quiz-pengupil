
from base_test import BaseTest


class TestRegisterAllFieldsEmpty(BaseTest):
    
    def test_register_all_fields_empty(self):
        print("\n[TC-REG-003] Testing: Register dengan Semua Field Kosong")
        
        self.navigate_to_register()
        
        self.submit_register_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_reg_003_all_empty")
        
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error")


if __name__ == "__main__":
    import unittest
    unittest.main()
