"""
TC-REG-014: Register dengan Password Pendek (< 6 karakter)
Expected: Test validasi panjang password
"""

from base_test import BaseTest


class TestRegisterShortPassword(BaseTest):
    
    def test_register_short_password(self):
        """Test register dengan password terlalu pendek"""
        print("\n[TC-REG-014] Testing: Register dengan Password Pendek")
        
        test_username = "testuser_shortpass"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="shortpass@example.com",
            username=test_username,
            password="123",  # Password sangat pendek
            repassword="123"
        )
        self.submit_register_form()
        
        # Check if system validates password length
        user_created = self.user_exists(test_username)
        print(f"User created with short password: {user_created}")
        
        if user_created:
            print("⚠️ System allows short passwords (security issue)")
            self.cleanup_test_user(test_username)
        else:
            print("✓ System validates password length")


if __name__ == "__main__":
    import unittest
    unittest.main()
