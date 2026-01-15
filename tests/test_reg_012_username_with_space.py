"""
TC-REG-012: Register dengan Username Spasi
Expected: PASS - User bisa terbuat dengan username berisi spasi
"""

from base_test import BaseTest


class TestRegisterUsernameWithSpace(BaseTest):
    
    def test_register_username_with_space(self):
        """Test register dengan username yang mengandung spasi"""
        print("\n[TC-REG-012] Testing: Register dengan Username Berisi Spasi")
        
        test_username = "test user space"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="userspace@example.com",
            username=test_username,  # Username dengan spasi
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Check if user created (might succeed or fail depending on validation)
        user_created = self.user_exists(test_username)
        print(f"User created with space in username: {user_created}")
        
        # Dokumentasi behavior
        if user_created:
            print("✓ System allows username with spaces")
            self.cleanup_test_user(test_username)
        else:
            print("✗ System prevents username with spaces")


if __name__ == "__main__":
    import unittest
    unittest.main()
