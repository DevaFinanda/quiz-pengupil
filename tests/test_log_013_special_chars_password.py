"""
TC-LOG-013: Login dengan Special Characters di Password
Expected: Test bahwa password bisa mengandung special characters
"""

from base_test import BaseTest


class TestLoginSpecialCharactersPassword(BaseTest):
    
    def test_login_special_characters_password(self):
        """Test login dengan password yang mengandung karakter khusus"""
        print("\n[TC-LOG-013] Testing: Login dengan Special Characters di Password")
        
        # Create test user dengan password yang mengandung special chars
        test_username = "testuser_specialpass"
        special_password = "P@ssw0rd!#$%"
        
        self.cleanup_test_user(test_username)
        
        # Create user via database
        created = self.create_test_user(
            username=test_username,
            name="Test User",
            email="specialpass@example.com",
            password=special_password
        )
        
        if not created:
            self.skipTest("Could not create test user")
        
        # Try login dengan special characters password
        self.navigate_to_login()
        self.fill_login_form(username=test_username, password=special_password)
        self.submit_login_form()
        
        import time
        time.sleep(1)
        
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        # Should be able to login
        self.assertNotIn("login.php", current_url,
                        "Should be able to login with special characters in password")
        
        print("✓ System supports special characters in password")
        
        # Cleanup
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
