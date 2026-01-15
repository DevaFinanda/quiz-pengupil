"""
TC-REG-003: Register dengan Semua Field Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterAllFieldsEmpty(BaseTest):
    
    def test_register_all_fields_empty(self):
        """Test register dengan semua field kosong"""
        print("\n[TC-REG-003] Testing: Register dengan Semua Field Kosong")
        
        self.navigate_to_register()
        
        # Submit tanpa mengisi apa-apa
        self.submit_register_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error")


if __name__ == "__main__":
    import unittest
    unittest.main()
