"""
TC-REG-009: Register dengan Username yang Sudah Ada
Expected: PASS - Error "Username sudah terdaftar !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterDuplicateUsername(BaseTest):
    
    def test_register_duplicate_username(self):
        """Test register dengan username yang sudah terdaftar"""
        print("\n[TC-REG-009] Testing: Register dengan Username yang Sudah Ada")
        
        # Username 'irul' sudah ada di database (dari SQL dump)
        existing_username = "irul"
        
        self.navigate_to_register()
        self.fill_register_form(
            name="New User",
            email="newuser@example.com",
            username=existing_username,
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Username sudah terdaftar", error,
                     "Should show duplicate username error")


if __name__ == "__main__":
    import unittest
    unittest.main()
