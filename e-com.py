from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1️⃣ Open Website
driver.get("https://www.saucedemo.com/")
time.sleep(1)

# 2️⃣ Verify Login Page
wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
print("Login Page Verified")
time.sleep(1)

# 3️⃣ Enter Credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)


# 4️⃣ Click Login
driver.find_element(By.ID, "login-button").click()
time.sleep(1)


# 5️⃣ Verify Home Page (Products page)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
print("Login Successful - Home Page Verified")
time.sleep(2)


# 6️⃣ Select a Product (Simulating search)
driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
print("Product Selected Successfully")

time.sleep(5)

driver.quit()