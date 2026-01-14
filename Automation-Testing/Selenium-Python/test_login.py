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

def test_login_negative(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    import time  # add this at the TOP once

    time.sleep(1)
    error_message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in error_message