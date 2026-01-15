"""
TC-LOG-004: Login dengan Semua Field Kosong
Expected: PASS - Error "Data tidak boleh kosong !!" ditampilkan
"""

from base_test import BaseTest


class TestLoginAllFieldsEmpty(BaseTest):
    
    def test_login_all_fields_empty(self):
        """Test login dengan username dan password kosong"""
        print("\n[TC-LOG-004] Testing: Login dengan Semua Field Kosong")
        
        self.navigate_to_login()
        
        # Submit tanpa mengisi apa-apa
        self.submit_login_form()
        
        # Verify error message
        error = self.get_error_message()
        print(f"Error message: {error}")
        
        self.assertIn("Data tidak boleh kosong", error,
                     "Should show empty data error")


if __name__ == "__main__":
    import unittest
    unittest.main()
