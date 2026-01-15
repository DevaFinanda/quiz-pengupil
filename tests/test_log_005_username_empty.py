"""
TC-LOG-005: Login dengan Username Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestLoginUsernameEmpty(BaseTest):
    
    def test_login_username_empty(self):
        """Test login dengan username kosong tapi password terisi"""
        print("\n[TC-LOG-005] Testing: Login dengan Username Kosong")
        
        self.navigate_to_login()
        self.fill_login_form(username="", password="SomePassword123")
        self.submit_login_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when username is empty")


if __name__ == "__main__":
    import unittest
    unittest.main()
