"""
TC-LOG-001: Login dengan Kredensial Valid
Expected: PASS - User berhasil login dan redirect ke index.php
"""

from base_test import BaseTest


class TestLoginValidCredentials(BaseTest):
    
    def test_login_valid_credentials(self):
        """Test login dengan username dan password yang benar"""
        print("\n[TC-LOG-001] Testing: Login dengan Kredensial Valid")
        
        # User 'irul' dengan password '12345' sudah ada di database
        self.navigate_to_login()
        self.fill_login_form(username="irul", password="12345")
        self.submit_login_form()
        
        # Verify redirect ke index.php atau homepage
        import time
        time.sleep(2)
        current_url = self.driver.current_url
        print(f"Current URL after login: {current_url}")
        
        # Should redirect from login page
        self.assertNotIn("login.php", current_url,
                        "Should redirect away from login page after successful login")


if __name__ == "__main__":
    import unittest
    unittest.main()
