# Automated login test using Selenium + Python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()



# Locate elements
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Enter INVALID credentials
username.send_keys("tomsmith")
password.send_keys("WrongPassword!")
login_button.click()

time.sleep(2)


# ASSERT error message is displayed
# Verify error message for invalid password
error_message = driver.find_element(By.ID, "flash").text
assert "Your password is invalid!" in error_message

time.sleep(3)
driver.quit()