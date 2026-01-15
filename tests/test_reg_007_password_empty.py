"""
TC-REG-007: Register dengan Password Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterPasswordEmpty(BaseTest):
    
    def test_register_password_empty(self):
        """Test register dengan field password kosong"""
        print("\n[TC-REG-007] Testing: Register dengan Password Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="passempty@example.com",
            username="testuser_passempty",
            password="",  # Kosong
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when password is empty")
        
        # Cleanup
        self.cleanup_test_user("testuser_passempty")


if __name__ == "__main__":
    import unittest
    unittest.main()
