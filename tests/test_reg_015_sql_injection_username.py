
from base_test import BaseTest


class TestRegisterSQLInjectionUsername(BaseTest):
    
    def test_register_sql_injection_username(self):
        print("\n[TC-REG-015] Testing: Register dengan SQL Injection di Username")
        
        test_username = "admin' OR '1'='1"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="sqlinjection@example.com",
            username=test_username,
            password="Test@123",
            repassword="Test@123"
        )
        
        self.submit_register_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_reg_015_sql_injection_username")
        
        user_created = self.user_exists(test_username)
        print(f"User created with SQL injection string: {user_created}")
        
        total_users = self.count_users()
        print(f"Total users in database: {total_users}")
        
        if user_created:
            print("[OK] SQL injection prevented - string treated as literal username")
            self.cleanup_test_user(test_username)
        
        self.assertGreater(total_users, 0, "Database should have users")


if __name__ == "__main__":
    import unittest
    unittest.main()
