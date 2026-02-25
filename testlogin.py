from driversetup import get_driver
from loginpage import LoginPage
from homepage import HomePage
import time

driver = get_driver()

login = LoginPage(driver)
home = HomePage(driver)

# Test Steps
login.verify_login_page()
login.login("standard_user", "secret_sauce")

home.verify_home_page()
home.select_product()

print("Test Executed Successfully")

time.sleep(5)
driver.quit()