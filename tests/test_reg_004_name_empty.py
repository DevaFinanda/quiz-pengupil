"""
TC-REG-004: Register dengan Name Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterNameEmpty(BaseTest):
    
    def test_register_name_empty(self):
        """Test register dengan field name kosong"""
        print("\n[TC-REG-004] Testing: Register dengan Name Kosong")
        
        self.navigate_to_register()
        self.fill_register_form(
            name="",  # Kosong
            email="nameempty@example.com",
            username="testuser_nameempty",
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error when name is empty")
        
        # Cleanup
        self.cleanup_test_user("testuser_nameempty")


if __name__ == "__main__":
    import unittest
    unittest.main()
