"""
module will be having functionality of place order 
page
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
from locators.home_page_locators import HomePageLocators
from locators.food_listing_page_locators import FoodSelectionPageLocators


class PlaceOrder:
    def __init__(self, driver):
        self.driver = driver
    
    
    def add_new_address_and_place_order(self):
        self.driver.find_element_by_id('comments').send_keys('Testing purpose adding new address')
        time.sleep(2)
        self.driver.find_element_by_('addAddressButton').click()
        address_label = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((
                By.ID, 'addrLabel'
            ))
        )
        address_label.send_keys('Testing address')
        full_address = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((
                By.ID, 'addrFull'
            ))
        )
        full_address.send_keys('# test test1 test2')
        time.sleep(2)
        self.driver.find_element_by_id('pinCode').send_keys('123456')
        time.sleep(2)
        self.driver.find_element_by_id('addrlandMark').send_keys('xxxxx')
        time.sleep(2)
        self.driver.find_element_by_id('saveAddress').click()
        time.sleep(2)
        self.driver.find_element_by_id('placeOrderButton').click()

    def select_saved_address(self):
        time.sleep(2)
        self.driver.find_element_by_id('placeOrderButton').click()
        


