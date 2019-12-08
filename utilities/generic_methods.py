from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def click_element(self, By, locator, locatortype):
    """wait_handler class"""
    try:
        if locatortype == 'xpath':
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            element.click()
        else:
            print('xpath error', locator)

    except Exception as exc:
        print('Unable to click on', str(element))