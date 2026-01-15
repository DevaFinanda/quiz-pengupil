"""
TC-REG-013: Register dengan Special Characters di Username
Expected: Test behavior dengan karakter khusus
"""

from base_test import BaseTest


class TestRegisterUsernameSpecialChars(BaseTest):
    
    def test_register_username_special_characters(self):
        """Test register dengan username mengandung karakter khusus"""
        print("\n[TC-REG-013] Testing: Register dengan Special Characters di Username")
        
        test_username = "test@user#123!"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="specialchars@example.com",
            username=test_username,  # Username dengan special chars
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Check behavior
        user_created = self.user_exists(test_username)
        print(f"User created with special characters: {user_created}")
        
        if user_created:
            print("✓ System allows special characters in username")
            self.cleanup_test_user(test_username)
        else:
            print("✗ System prevents special characters in username")


if __name__ == "__main__":
    import unittest
    unittest.main()
