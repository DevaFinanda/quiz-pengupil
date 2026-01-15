# Quiz Pengupil Test Suite

Automated testing untuk aplikasi Quiz Pengupil menggunakan Selenium WebDriver dan PyMySQL.

## Test Coverage

### Register Module (7 test cases)
- TC-REG-001: Register dengan data valid (bug detection: field name empty)
- TC-REG-002: Register dengan password mismatch
- TC-REG-003: Register dengan semua field kosong
- TC-REG-004: Register dengan field name kosong
- TC-REG-009: Register dengan username duplikat
- TC-REG-010: Register dengan email format invalid
- TC-REG-015: Register dengan SQL injection attempt

### Login Module (7 test cases)
- TC-LOG-001: Login dengan kredensial valid
- TC-LOG-002: Login dengan password salah
- TC-LOG-003: Login dengan user tidak ada
- TC-LOG-004: Login dengan semua field kosong
- TC-LOG-008: Login dengan SQL injection di username
- TC-LOG-009: Login dengan SQL injection di password
- TC-LOG-010: Login dengan XSS attempt di username

## Requirements

```
selenium==4.17.2
pymysql==1.1.0
bcrypt==4.1.2
webdriver-manager==4.0.1
```

## Installation

```bash
cd tests
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
python run_all_tests.py
```

Run specific test:
```bash
python test_reg_001_valid_data.py
```

## Screenshots

Test screenshots disimpan di folder `screenshots/` dengan format nama:
- `test_reg_001_valid_data.png`
- `test_log_001_valid_credentials.png`
- etc.

## CI/CD

GitHub Actions workflow: `.github/workflows/main.yml`
