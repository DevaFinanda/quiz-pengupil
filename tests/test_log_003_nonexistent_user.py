
from base_test import BaseTest


class TestLoginNonexistentUser(BaseTest):
    
    def test_login_nonexistent_user(self):
        print("\n[TC-LOG-003] Testing: Login dengan Username Tidak Terdaftar")
        
        self.navigate_to_login()
        self.fill_login_form(username="usernotexist999", password="anypassword")
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_003_nonexistent_user")
        
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Register User Gagal", error,
                     "Shows error message (but misleading)")
        
        print("[WARNING] ISSUE: Error message is misleading - should say 'Username atau Password salah'")


if __name__ == "__main__":
    import unittest
    unittest.main()
