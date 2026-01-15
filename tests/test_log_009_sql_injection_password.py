
from base_test import BaseTest


class TestLoginSQLInjectionPassword(BaseTest):
    
    def test_login_sql_injection_password(self):
        print("\n[TC-LOG-009] Testing: Login dengan SQL Injection di Password")
        
        self.navigate_to_login()
        
        sql_injection_pass = "' OR '1'='1' --"
        self.fill_login_form(username="irul", password=sql_injection_pass)
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_009_sql_injection_password")
        
        import time
        time.sleep(1)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        self.assertIn("login.php", current_url,
                     "SQL injection in password should be prevented")
        
        print("[OK] SQL injection prevented - password is hashed and compared safely")


if __name__ == "__main__":
    import unittest
    unittest.main()
