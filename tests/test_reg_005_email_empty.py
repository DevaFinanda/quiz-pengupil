"""
TC-REG-005: Register dengan Email Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterEmailEmpty(BaseTest):
    
    def test_register_email_empty(self):
        """Test register dengan field email kosong"""
        print("\n[TC-REG-005] Testing: Register dengan Email Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="",  # Kosong
            username="testuser_emailempty",
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when email is empty")
        
        # Cleanup
        self.cleanup_test_user("testuser_emailempty")


if __name__ == "__main__":
    import unittest
    unittest.main()
