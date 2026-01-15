# Selenium Automation Tests (Python)

This project contains basic Selenium automation tests written in Python using Pytest.

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- ChromeDriver
- PyCharm

## Tests Included

### Login Tests
File: `test_login.py`

- Positive login test (valid username & password)
- Negative login test (invalid password)
- Uses `WebDriverWait` for reliable element handling
- Demonstrates basic Selenium + Pytest structure

## Test Website
https://the-internet.herokuapp.com/login

1. Install dependencies:
```bash
pip install selenium pytest
```
2. Run tests:
```bash
pytest
```