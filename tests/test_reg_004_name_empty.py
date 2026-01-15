
from base_test import BaseTest


class TestRegisterNameEmpty(BaseTest):
    
    def test_register_name_empty(self):
        print("\n[TC-REG-004] Testing: Register dengan Name Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="",
            email="nameempty@example.com",
            username="testuser_nameempty",
            password="Test@123",
            repassword="Test@123"
        )
        
        self.submit_register_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_reg_004_name_empty")
        
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when name is empty")
        
        self.cleanup_test_user("testuser_nameempty")


if __name__ == "__main__":
    import unittest
    unittest.main()
