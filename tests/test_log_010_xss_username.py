
from base_test import BaseTest


class TestLoginXSSUsername(BaseTest):
    
    def test_login_xss_username(self):
        print("\n[TC-LOG-010] Testing: Login dengan XSS Attempt di Username")
        
        self.navigate_to_login()
        
        xss_payload = "<script>alert('XSS')</script>"
        self.fill_login_form(username=xss_payload, password="test")
        
        self.submit_login_form()
        
        import time
        time.sleep(1)
        self.take_screenshot("test_log_010_xss_username")
        
        import time
        time.sleep(1)
        
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"[WARNING]️ VULNERABILITY: XSS executed! Alert: {alert_text}")
            alert.dismiss()
            self.fail("XSS vulnerability detected - script was executed")
        except:
            print("[OK] XSS prevented - no alert dialog appeared")
            
        self.assertIn("login.php", self.driver.current_url,
                     "Should stay on login page")


if __name__ == "__main__":
    import unittest
    unittest.main()
