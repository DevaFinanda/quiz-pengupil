"""
TC-LOG-009: Login dengan SQL Injection di Password
Expected: PASS - SQL injection dicegah
"""

from base_test import BaseTest


class TestLoginSQLInjectionPassword(BaseTest):
    
    def test_login_sql_injection_password(self):
        """Test SQL injection attempt pada login password field"""
        print("\n[TC-LOG-009] Testing: Login dengan SQL Injection di Password")
        
        self.navigate_to_login()
        
        # Attempt SQL injection di password
        sql_injection_pass = "' OR '1'='1' --"
        self.fill_login_form(username="irul", password=sql_injection_pass)
        self.submit_login_form()
        
        # Should NOT be able to login
        import time
        time.sleep(1)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        # Should stay on login page
        self.assertIn("login.php", current_url,
                     "SQL injection in password should be prevented")
        
        print("✓ SQL injection prevented - password is hashed and compared safely")


if __name__ == "__main__":
    import unittest
    unittest.main()
