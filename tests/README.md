# Quiz Pengupil - Test Suite

## Test Cases (28 Tests Total)

### Register Tests (15 tests)
- `test_reg_001_valid_data.py` - Register dengan data valid (detects BUG)
- `test_reg_002_password_mismatch.py` - Password tidak sama
- `test_reg_003_all_empty.py` - Semua field kosong
- `test_reg_004_name_empty.py` - Name kosong
- `test_reg_005_email_empty.py` - Email kosong
- `test_reg_006_username_empty.py` - Username kosong
- `test_reg_007_password_empty.py` - Password kosong
- `test_reg_008_repassword_empty.py` - Re-password kosong
- `test_reg_009_duplicate_username.py` - Username sudah terdaftar
- `test_reg_010_invalid_email.py` - Email format invalid
- `test_reg_011_email_no_domain.py` - Email tanpa domain
- `test_reg_012_username_with_space.py` - Username dengan spasi
- `test_reg_013_username_special_chars.py` - Username dengan special characters
- `test_reg_014_short_password.py` - Password terlalu pendek
- `test_reg_015_sql_injection_username.py` - SQL injection di username

### Login Tests (13 tests)
- `test_log_001_valid_credentials.py` - Login dengan kredensial valid
- `test_log_002_wrong_password.py` - Password salah
- `test_log_003_nonexistent_user.py` - User tidak terdaftar (misleading error)
- `test_log_004_all_empty.py` - Semua field kosong
- `test_log_005_username_empty.py` - Username kosong
- `test_log_006_password_empty.py` - Password kosong
- `test_log_007_username_whitespace.py` - Username hanya spasi
- `test_log_008_sql_injection_username.py` - SQL injection di username
- `test_log_009_sql_injection_password.py` - SQL injection di password
- `test_log_010_xss_username.py` - XSS attack di username
- `test_log_011_case_sensitivity.py` - Case sensitivity test
- `test_log_012_long_username.py` - Username sangat panjang
- `test_log_013_special_chars_password.py` - Password dengan special characters

## Running Tests

### Install Dependencies
```bash
cd tests
pip install -r requirements.txt
```

### Run All Tests
```bash
python run_all_tests.py
```

### Run Single Test
```bash
python test_reg_001_valid_data.py
python test_log_001_valid_credentials.py
```

### Run Specific Category
```bash
# Register tests only
python -m unittest discover -s . -p "test_reg_*.py" -v

# Login tests only
python -m unittest discover -s . -p "test_log_*.py" -v
```

## CI/CD
Tests run automatically via GitHub Actions on push/PR to main/develop branches.

## Known Issues
🐛 **BUG-001**: Field 'name' empty in database (register.php line 35)
⚠️ **ISSUE-001**: Misleading error message in login (login.php line 32)
