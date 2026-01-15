"""
TC-LOG-006: Login dengan Password Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestLoginPasswordEmpty(BaseTest):
    
    def test_login_password_empty(self):
        """Test login dengan password kosong tapi username terisi"""
        print("\n[TC-LOG-006] Testing: Login dengan Password Kosong")
        
        self.navigate_to_login()
        self.fill_login_form(username="irul", password="")
        self.submit_login_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when password is empty")


if __name__ == "__main__":
    import unittest
    unittest.main()
