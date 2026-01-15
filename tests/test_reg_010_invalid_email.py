"""
TC-REG-010: Register dengan Email Format Invalid
Expected: PASS - HTML5 validation atau tetap di halaman register
"""

from base_test import BaseTest


class TestRegisterInvalidEmail(BaseTest):
    
    def test_register_invalid_email_format(self):
        """Test register dengan format email yang tidak valid"""
        print("\n[TC-REG-010] Testing: Register dengan Email Format Invalid")
        
        test_username = "testuser_invalidemail"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="invalidemail",  # Email tanpa @
            username=test_username,
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # HTML5 validation akan prevent submit, atau jika tersubmit user tidak terbuat
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        # Should stay on register page
        self.assertIn("register.php", current_url,
                     "Should stay on register page with invalid email")
        
        # User tidak boleh terbuat
        self.assertFalse(self.user_exists(test_username),
                        "User should not be created with invalid email")
        
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
