from selenium import webdriver

driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
driver.get("https://www.google.com")
print(driver.title)
driver.quit()