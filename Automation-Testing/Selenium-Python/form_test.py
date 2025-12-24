from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")

name_input = driver.find_element(By.NAME, "firstname")
name_input.send_keys("John")

submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

driver.quit()