"""
TC-REG-008: Register dengan Re-Password Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterRePasswordEmpty(BaseTest):
    
    def test_register_repassword_empty(self):
        """Test register dengan field re-password kosong"""
        print("\n[TC-REG-008] Testing: Register dengan Re-Password Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="repassempty@example.com",
            username="testuser_repassempty",
            password="Test@123",
            repassword=""  # Kosong
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when re-password is empty")
        
        # Cleanup
        self.cleanup_test_user("testuser_repassempty")


if __name__ == "__main__":
    import unittest
    unittest.main()
