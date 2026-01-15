"""
TC-REG-002: Register dengan Password Tidak Sama
Expected: PASS - Error "Password tidak sama !!" ditampilkan
"""

from base_test import BaseTest


class TestRegisterPasswordMismatch(BaseTest):
    
    def test_register_password_mismatch(self):
        """Test register dengan password dan re-password berbeda"""
        print("\n[TC-REG-002] Testing: Register dengan Password Tidak Sama")
        
        test_username = "testuser_passmismatch"
        
        # Cleanup
        self.cleanup_test_user(test_username)
        
        # Navigate dan isi form dengan password berbeda
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="passmismatch@example.com",
            username=test_username,
            password="Password123",
            repassword="Password456"  # Berbeda
        )
        self.submit_register_form()
        
        # Verify error message
        validation = self.get_validation_message()
        print(f"Validation message: {validation}")
        
        self.assertIn("Password tidak sama", validation,
                     "Should show password mismatch error")
        
        # Verify user tidak terbuat
        self.assertFalse(self.user_exists(test_username),
                        "User should NOT be created with mismatched passwords")
        
        # Cleanup
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
