
from base_test import BaseTest


class TestRegisterInvalidEmail(BaseTest):
    
    def test_register_invalid_email_format(self):
        print("\n[TC-REG-010] Testing: Register dengan Email Format Invalid")
        
        test_username = "testuser_invalidemail"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="invalidemail",
            username=test_username,
            password="Test@123",
            repassword="Test@123"
        )
        
        self.submit_register_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_reg_010_invalid_email")
        
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        self.assertIn("register.php", current_url,
                     "Should stay on register page with invalid email")
        
        self.assertFalse(self.user_exists(test_username),
                        "User should not be created with invalid email")
        
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
