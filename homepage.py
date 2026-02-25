from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    page_title = (By.CLASS_NAME, "title")
    product = (By.XPATH, "//div[text()='Sauce Labs Backpack']")

    # Actions
    def verify_home_page(self):
        self.wait.until(EC.visibility_of_element_located(self.page_title))

    def select_product(self):
        self.driver.find_element(*self.product).click()
