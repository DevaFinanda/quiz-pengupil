"""
TC-LOG-002: Login dengan Password Salah
Expected: PASS - Tetap di halaman login
"""

from base_test import BaseTest


class TestLoginWrongPassword(BaseTest):
    
    def test_login_wrong_password(self):
        """Test login dengan password yang salah"""
        print("\n[TC-LOG-002] Testing: Login dengan Password Salah")
        
        self.navigate_to_login()
        self.fill_login_form(username="irul", password="wrongpassword123")
        self.submit_login_form()
        
        # Should stay on login page
        self.assert_on_page("login.php")
        
        # Note: Kode tidak menampilkan error untuk wrong password
        print("ℹ️ Note: No error message shown for wrong password (security by obscurity)")


if __name__ == "__main__":
    import unittest
    unittest.main()
