import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_positive(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    success_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "You logged into a secure area!" in success_message

def test_login_negative(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    success_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your password is invalid!" in success_message
