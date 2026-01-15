from base_test import BaseTest


class TestLoginValidCredentials(BaseTest):
    
    def test_login_valid_credentials(self):
        print("\n[TC-LOG-001] Testing: Login dengan Kredensial Valid")
        
        self.navigate_to_login()
        self.fill_login_form(username="testuser_login", password="Test@123")
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_001_valid_credentials")
        
        import time
        time.sleep(2)
        current_url = self.driver.current_url
        print(f"Current URL after login: {current_url}")
        
        self.assertNotIn("login.php", current_url,
                        "Should redirect away from login page after successful login")


if __name__ == "__main__":
    import unittest
    unittest.main()
