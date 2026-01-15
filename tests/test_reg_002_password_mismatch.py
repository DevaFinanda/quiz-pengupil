
from base_test import BaseTest


class TestRegisterPasswordMismatch(BaseTest):
    
    def test_register_password_mismatch(self):
        print("\n[TC-REG-002] Testing: Register dengan Password Tidak Sama")
        
        test_username = "testuser_passmismatch"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="passmismatch@example.com",
            username=test_username,
            password="Password123",
            repassword="Password456"
        )
        
        self.submit_register_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_reg_002_password_mismatch")
        
        validation = self.get_validation_message()
        print(f"Validation message: {validation}")
        
        self.assertIn("Password tidak sama", validation,
                     "Should show password mismatch error")
        
        self.assertFalse(self.user_exists(test_username),
                        "User should NOT be created with mismatched passwords")
        
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
