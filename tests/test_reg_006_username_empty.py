"""
TC-REG-006: Register dengan Username Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterUsernameEmpty(BaseTest):
    
    def test_register_username_empty(self):
        """Test register dengan field username kosong"""
        print("\n[TC-REG-006] Testing: Register dengan Username Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="usernameempty@example.com",
            username="",  # Kosong
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when username is empty")


if __name__ == "__main__":
    import unittest
    unittest.main()
