
from base_test import BaseTest


class TestLoginWrongPassword(BaseTest):
    
    def test_login_wrong_password(self):
        print("\n[TC-LOG-002] Testing: Login dengan Password Salah")
        
        self.navigate_to_login()
        self.fill_login_form(username="irul", password="wrongpassword123")
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_002_wrong_password")
        
        self.assert_on_page("login.php")
        
        print("[INFO] Note: No error message shown for wrong password (security by obscurity)")


if __name__ == "__main__":
    import unittest
    unittest.main()
