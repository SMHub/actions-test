# Import library
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Start browser
driver = webdriver.Chrome()

# Go to the Application
url = "http://127.0.0.1:5000/sign-up"
driver.get(url)
sleep(2)
print('Page Loaded:', driver.title)

# Actions
sign_up_locator = "//button[contains(.,'Sign Up')]"
su_ele = driver.find_element(By.XPATH, sign_up_locator)
su_ele.click()

# Assert
err_msg_locator = "//div[@role='alert']"
err_msg_ele = driver.find_element(By.XPATH, err_msg_locator)
err_msg = err_msg_ele.text
print(err_msg)
sleep(2)

driver.quit()

