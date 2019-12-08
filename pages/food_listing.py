"""
this module will have all the method in the food listing 
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
from locators.place_order_page_locators import PlaceOrderPageLocators
from utilities.generic_methods import click_element


class FoodSelectionPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_food_to_cart_and_login(self):
        self.driver.find_element_by_xpath(
            FoodSelectionPageLocators.place_order_dialog_box_button
        ).click()
        time.sleep(2)
        add_wet_noodles  = self.driver.find_elements_by_xpath(
            FoodSelectionPageLocators.add_button_for_wet_noodles
        )
        print('getting the items from the wet noodles')
        try:
            time.sleep(3)
            add_wet_noodles[0].click()
            # print('clicking on random element')
            time.sleep(3)
            add_wet_noodles[3].click()
        except IndexError:
            print('Please select valid item..')
        self.driver.find_element_by_xpath(
            FoodSelectionPageLocators.checkout_order_button
        ).click()
        time.sleep(3)
        # print('Enter mobile number')
        elm = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                By.XPATH, FoodSelectionPageLocators.mobile_number_text_box
            ))
        )
        elm.click()
        elm.send_keys('1234567890')
        time.sleep(3)
        self.driver.find_element_by_xpath(
            FoodSelectionPageLocators.proceed_button
        ).click()
        time.sleep(4)
        name_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                By.XPATH, FoodSelectionPageLocators.your_name_text_box
            ))
        )
        name_box.click()
        name_box.clear()
        name_box.send_keys('Tester')
        email_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((
                By.XPATH, FoodSelectionPageLocators.your_email_id_text_box
            ))
        )
        email_box.clear()
        email_box.click()
        email_box.send_keys('unknown@gmail.com')
        time.sleep(2)
        self.driver.find_element_by_xpath(FoodSelectionPageLocators.proceed_button_2).click()
        address_val = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((
                By.XPATH, PlaceOrderPageLocators.address_payment_box
            ))
        )
        if address_val:
            print("Place order page")
        else:
            print("something went wrong....")
        






    def check_cart_is_empty(self):
        elm = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FoodSelectionPageLocators.empty_cart))
        )
        if elm:
            return elm.text
        else:
            return 'items are added to the cart'

    