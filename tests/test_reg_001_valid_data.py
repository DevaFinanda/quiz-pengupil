"""
TC-REG-001: Register dengan Data Valid
Expected: FAIL - Bug detected (field name kosong di database)
"""

from base_test import BaseTest


class TestRegisterValidData(BaseTest):
    
    def test_register_valid_data_bug_detection(self):
        """
        Test register dengan semua data valid
        BUG: Field 'name' di database akan kosong karena variable mismatch ($nama vs $name)
        """
        print("\n[TC-REG-001] Testing: Register dengan Data Valid")
        
        test_data = {
            "username": "testuser_valid",
            "name": "Test User Valid",
            "email": "testvalid@example.com",
            "password": "Test@123"
        }
        
        # Cleanup
        self.cleanup_test_user(test_data["username"])
        
        # Navigate dan isi form
        self.navigate_to_register()
        self.fill_register_form(
            name=test_data["name"],
            email=test_data["email"],
            username=test_data["username"],
            password=test_data["password"],
            repassword=test_data["password"]
        )
        self.submit_register_form()
        
        # Verify user terbuat di database
        self.assertTrue(self.user_exists(test_data["username"]), 
                       "User should be created in database")
        
        # BUG DETECTION: Cek field 'name' di database
        user_data = self.get_user_data(test_data["username"])
        print(f"Database name field: '{user_data['name']}'")
        print(f"Expected name: '{test_data['name']}'")
        
        # Ini akan FAIL karena bug
        self.assertNotEqual(user_data['name'], "", 
                          "🐛 BUG DETECTED: Field 'name' is empty! Variable mismatch $nama vs $name in register.php line 35")
        
        self.assertEqual(user_data['name'], test_data['name'],
                        f"Name should be '{test_data['name']}' but got '{user_data['name']}'")
        
        # Cleanup
        self.cleanup_test_user(test_data["username"])


if __name__ == "__main__":
    import unittest
    unittest.main()
