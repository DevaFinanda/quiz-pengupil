"""
TC-LOG-003: Login dengan Username Tidak Terdaftar
Expected: PASS (but misleading error) - Error "Register User Gagal !!" ditampilkan
"""

from base_test import BaseTest


class TestLoginNonexistentUser(BaseTest):
    
    def test_login_nonexistent_user(self):
        """Test login dengan username yang tidak ada di database"""
        print("\n[TC-LOG-003] Testing: Login dengan Username Tidak Terdaftar")
        
        self.navigate_to_login()
        self.fill_login_form(username="usernotexist999", password="anypassword")
        self.submit_login_form()
        
        # Verify error message (misleading)
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Register User Gagal", error,
                     "Shows error message (but misleading)")
        
        print("⚠️ ISSUE: Error message is misleading - should say 'Username atau Password salah'")


if __name__ == "__main__":
    import unittest
    unittest.main()
