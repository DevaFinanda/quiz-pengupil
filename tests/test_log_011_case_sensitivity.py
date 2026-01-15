"""
TC-LOG-011: Login dengan Case Sensitivity Test
Expected: Test apakah username case-sensitive
"""

from base_test import BaseTest


class TestLoginCaseSensitivity(BaseTest):
    
    def test_login_case_sensitivity(self):
        """Test apakah username case-sensitive (IRUL vs irul)"""
        print("\n[TC-LOG-011] Testing: Login Case Sensitivity")
        
        # User 'irul' ada di database (lowercase)
        # Try dengan uppercase
        self.navigate_to_login()
        self.fill_login_form(username="IRUL", password="12345")
        self.submit_login_form()
        
        import time
        time.sleep(1)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        if "login.php" in current_url:
            print("✓ Username is case-sensitive (IRUL != irul)")
        else:
            print("ℹ️ Username is case-insensitive (IRUL == irul)")


if __name__ == "__main__":
    import unittest
    unittest.main()
