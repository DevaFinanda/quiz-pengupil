"""
TC-LOG-007: Login dengan Username Whitespace
Expected: Test behavior dengan username yang hanya spasi
"""

from base_test import BaseTest


class TestLoginUsernameWhitespace(BaseTest):
    
    def test_login_username_whitespace(self):
        """Test login dengan username hanya berisi spasi"""
        print("\n[TC-LOG-007] Testing: Login dengan Username Whitespace")
        
        self.navigate_to_login()
        self.fill_login_form(username="   ", password="SomePassword")
        self.submit_login_form()
        
        # Verify behavior - should treat as empty after trim()
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        # trim() di PHP akan membuat ini kosong
        self.assertIn("Data tidak boleh kosong", error,
                     "Should detect whitespace-only username as empty")


if __name__ == "__main__":
    import unittest
    unittest.main()
