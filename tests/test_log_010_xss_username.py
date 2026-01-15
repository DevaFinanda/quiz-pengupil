"""
TC-LOG-010: Login dengan XSS Attempt di Username
Expected: Test XSS prevention
"""

from base_test import BaseTest


class TestLoginXSSUsername(BaseTest):
    
    def test_login_xss_username(self):
        """Test XSS attack attempt pada login username field"""
        print("\n[TC-LOG-010] Testing: Login dengan XSS Attempt di Username")
        
        self.navigate_to_login()
        
        # Attempt XSS
        xss_payload = "<script>alert('XSS')</script>"
        self.fill_login_form(username=xss_payload, password="test")
        self.submit_login_form()
        
        # Check if XSS is executed (it shouldn't be)
        import time
        time.sleep(1)
        
        # Try to detect alert dialog
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"⚠️ VULNERABILITY: XSS executed! Alert: {alert_text}")
            alert.dismiss()
            self.fail("XSS vulnerability detected - script was executed")
        except:
            print("✓ XSS prevented - no alert dialog appeared")
            
        # Should stay on login page
        self.assertIn("login.php", self.driver.current_url,
                     "Should stay on login page")


if __name__ == "__main__":
    import unittest
    unittest.main()
