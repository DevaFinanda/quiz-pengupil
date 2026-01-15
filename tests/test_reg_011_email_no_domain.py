"""
TC-REG-011: Register dengan Email Tanpa Domain
Expected: PASS - HTML5 validation atau error
"""

from base_test import BaseTest


class TestRegisterEmailNoDomain(BaseTest):
    
    def test_register_email_without_domain(self):
        """Test register dengan email tanpa domain (user@)"""
        print("\n[TC-REG-011] Testing: Register dengan Email Tanpa Domain")
        
        test_username = "testuser_nodomain"
        
        self.cleanup_test_user(test_username)
        
        self.navigate_to_register()
        self.fill_register_form(
            name="Test User",
            email="user@",  # Email tanpa domain
            username=test_username,
            password="Test@123",
            repassword="Test@123"
        )
        self.submit_register_form()
        
        # Should stay on register page
        self.assert_on_page("register.php")
        
        # User tidak boleh terbuat
        self.assertFalse(self.user_exists(test_username),
                        "User should not be created with incomplete email")
        
        self.cleanup_test_user(test_username)


if __name__ == "__main__":
    import unittest
    unittest.main()
