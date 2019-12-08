"""
This module will be having all the functions in the
order status page
"""

import time
import logging
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from locators.order_status_page_locators import OrderStatusPageLocators


class OrderStatus:
    """
    order status class
    """
    def __init__(self, driver):
        self.driver = driver
    
    def is_order_id_present(self):
        """
        method to check whether order id is present or not
        """
        order_id_with_msg = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, OrderStatusPageLocators.order_id_text))
        )
        print(order_id_with_msg.text)
        order_id = order_id_with_msg.text[16:]
        print(order_id)
        if order_id != " ":
            return True
        else:
            return False