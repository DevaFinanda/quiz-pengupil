"""
TC-LOG-012: Login dengan Very Long Username
Expected: Test behavior dengan input panjang
"""

from base_test import BaseTest


class TestLoginLongUsername(BaseTest):
    
    def test_login_very_long_username(self):
        """Test login dengan username yang sangat panjang"""
        print("\n[TC-LOG-012] Testing: Login dengan Very Long Username")
        
        self.navigate_to_login()
        
        # Username yang sangat panjang (> 50 karakter, limit di database)
        long_username = "a" * 100
        self.fill_login_form(username=long_username, password="test")
        self.submit_login_form()
        
        import time
        time.sleep(1)
        
        # Should handle gracefully (tidak crash)
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")
        
        self.assertIn("login.php", current_url,
                     "Should stay on login page with very long username")
        
        print("✓ System handles very long username without crashing")


if __name__ == "__main__":
    import unittest
    unittest.main()
