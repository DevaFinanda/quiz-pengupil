"""
Base Test Class untuk Quiz Pengupil Test Suite
Berisi helper functions dan setup yang digunakan oleh semua test cases
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pymysql
import os


class BaseTest(unittest.TestCase):
    
    BASE_URL = os.getenv('BASE_URL', 'http://localhost/quiz-pengupil')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASS = os.getenv('DB_PASS', '')
    DB_NAME = os.getenv('DB_NAME', 'quiz_pengupil')
    SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), 'screenshots')
    
    @classmethod
    def setUpClass(cls):
        """Setup yang dijalankan sekali sebelum semua test di class ini"""
        # Setup Chrome options
        chrome_options = Options()
        
        # Untuk CI/CD environment
        if os.getenv('CI'):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
        
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        
        cls._create_test_user_for_login()
    
    @classmethod
    def _create_test_user_for_login(cls):
        """Buat user test untuk login"""
        import bcrypt
        try:
            conn = pymysql.connect(
                host=cls.DB_HOST,
                user=cls.DB_USER,
                password=cls.DB_PASS,
                database=cls.DB_NAME
            )
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM users WHERE username = 'testuser_login'")
            
            password_hash = bcrypt.hashpw('Test@123'.encode(), bcrypt.gensalt()).decode()
            cursor.execute(
                "INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)",
                ('testuser_login', 'Test User Login', 'testlogin@example.com', password_hash)
            )
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Warning: Could not create test user: {e}")
        
    @classmethod
    def tearDownClass(cls):
        """Cleanup setelah semua test selesai"""
        cls.driver.quit()
        
    def setUp(self):
        """Setup sebelum setiap test"""
        self.driver.delete_all_cookies()
        
    def tearDown(self):
        """Cleanup setelah setiap test"""
        pass
    
    def take_screenshot(self, test_name):
        if not os.path.exists(self.SCREENSHOT_DIR):
            os.makedirs(self.SCREENSHOT_DIR)
        
        filename = f"{test_name}.png"
        filepath = os.path.join(self.SCREENSHOT_DIR, filename)
        
        self.driver.save_screenshot(filepath)
        print(f"[INFO] Screenshot saved: screenshots/{filename}")
        return filepath
    
    def get_db_connection(self):
        """Database connection helper"""
        return pymysql.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASS,
            database=self.DB_NAME,
            charset='utf8mb4'
        )
    
    def cleanup_test_user(self, username):
        """Hapus test user dari database"""
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE username = %s", (username,))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Warning: Failed to cleanup user {username}: {e}")
    
    def user_exists(self, username):
        """Cek apakah user ada di database"""
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            count = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return count > 0
        except Exception as e:
            print(f"Error checking user existence: {e}")
            return False
    
    def get_user_data(self, username):
        """Ambil data user dari database"""
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(f"Error getting user data: {e}")
            return None
    
    def create_test_user(self, username, name, email, password):
        """Buat test user di database"""
        try:
            import hashlib
            # Gunakan bcrypt yang sama seperti PHP password_hash
            import bcrypt
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)",
                (username, name, email, password_hash)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating test user: {e}")
            return False
    
    def count_users(self):
        """Hitung total users di database"""
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return count
        except Exception as e:
            print(f"Error counting users: {e}")
            return -1
    
    # ==================== SELENIUM HELPERS ====================
    
    def wait_for_element(self, by, value, timeout=10):
        """Wait untuk element muncul"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            return None
    
    def wait_for_url_contains(self, text, timeout=10):
        """Wait untuk URL berisi text tertentu"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False
    
    def get_error_message(self):
        """Ambil error message dari halaman"""
        try:
            error_element = self.driver.find_element(By.CLASS_NAME, "alert-danger")
            return error_element.text.strip()
        except NoSuchElementException:
            return ""
    
    def get_validation_message(self):
        """Ambil validation message (text-danger)"""
        try:
            elements = self.driver.find_elements(By.CLASS_NAME, "text-danger")
            if elements:
                return elements[0].text.strip()
            return ""
        except NoSuchElementException:
            return ""
    
    def is_logged_in(self):
        """Cek apakah user sudah login (session aktif)"""
        current_url = self.driver.current_url
        return "index.php" in current_url or current_url.endswith("/quiz-pengupil/")
    
    # ==================== FORM HELPERS ====================
    
    def fill_register_form(self, name="", email="", username="", password="", repassword=""):
        """Helper untuk isi form register"""
        if name:
            self.driver.find_element(By.ID, "name").send_keys(name)
        if email:
            self.driver.find_element(By.ID, "InputEmail").send_keys(email)
        if username:
            self.driver.find_element(By.ID, "username").send_keys(username)
        if password:
            self.driver.find_element(By.ID, "InputPassword").send_keys(password)
        if repassword:
            self.driver.find_element(By.ID, "InputRePassword").send_keys(repassword)
    
    def submit_register_form(self):
        """Submit form register"""
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
    
    def fill_login_form(self, username="", password=""):
        """Helper untuk isi form login"""
        if username:
            self.driver.find_element(By.ID, "username").send_keys(username)
        if password:
            self.driver.find_element(By.ID, "InputPassword").send_keys(password)
    
    def submit_login_form(self):
        """Submit form login"""
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)
    
    def navigate_to_register(self):
        """Navigate ke halaman register"""
        self.driver.get(f"{self.BASE_URL}/register.php")
        time.sleep(0.5)
    
    def navigate_to_login(self):
        """Navigate ke halaman login"""
        self.driver.get(f"{self.BASE_URL}/login.php")
        time.sleep(0.5)
    
    # ==================== ASSERTION HELPERS ====================
    
    def assert_on_page(self, page_name):
        """Assert bahwa kita ada di page tertentu"""
        current_url = self.driver.current_url
        self.assertIn(page_name, current_url, 
                     f"Expected to be on {page_name} but was on {current_url}")
    
    def assert_error_shown(self, expected_text):
        """Assert bahwa error message ditampilkan"""
        error = self.get_error_message()
        self.assertIn(expected_text, error, 
                     f"Expected error '{expected_text}' but got '{error}'")
    
    def assert_validation_shown(self, expected_text):
        """Assert bahwa validation message ditampilkan"""
        validation = self.get_validation_message()
        self.assertIn(expected_text, validation,
                     f"Expected validation '{expected_text}' but got '{validation}'")


if __name__ == "__main__":
    print("This is a base test class. Run individual test files instead.")
