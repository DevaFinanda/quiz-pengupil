"""
TC-LOG-008: Login dengan SQL Injection di Username
Expected: PASS - SQL injection dicegah
"""

from base_test import BaseTest


class TestLoginSQLInjectionUsername(BaseTest):
    
    def test_login_sql_injection_username(self):
        """Test SQL injection attempt pada login username field"""
        print("\n[TC-LOG-008] Testing: Login dengan SQL Injection di Username")
        
        self.navigate_to_login()
        
        # Attempt SQL injection
        sql_injection = "admin' OR '1'='1"
        self.fill_login_form(username=sql_injection, password="anything")
        self.submit_login_form()
        
        # Should NOT be able to login
        import time
        time.sleep(1)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        # Should stay on login page (injection failed)
        self.assertIn("login.php", current_url,
                     "SQL injection should be prevented - stayed on login page")
        
        print("✓ SQL injection prevented by mysqli_real_escape_string")


if __name__ == "__main__":
    import unittest
    unittest.main()
