
from base_test import BaseTest


class TestRegisterDuplicateUsername(BaseTest):
    
    def test_register_duplicate_username(self):
        print("\n[TC-REG-009] Testing: Register dengan Username yang Sudah Ada")
        
        existing_username = "testuser_login"
        
        self.navigate_to_register()
        self.fill_register_form(
            name="New User",
            email="newuser@example.com",
            username=existing_username,
            password="Test@123",
            repassword="Test@123"
        )
        
        self.submit_register_form()
        
        import time
        time.sleep(2)
        self.take_screenshot("test_reg_009_duplicate_username")
        
        error = self.get_error_message()
        print(f"Error message: '{error}'")
        
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        self.assertIn("register.php", current_url,
                     "Should stay on register page with duplicate username")
        
        if error:
            self.assertIn("Username sudah terdaftar", error,
                         "Should show duplicate username error")
        else:
            print("[WARNING] No error message displayed, but stayed on register page")


if __name__ == "__main__":
    import unittest
    unittest.main()
