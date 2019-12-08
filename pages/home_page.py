"""
This module will be having all the methods in the home page
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



class HomePage:
    """ Home Page Class"""

    def __init__(self, driver):
        self.driver = driver

    def start_ordering(self):
        """
        selecting the values in the home page
        and moving to food selection page
        """
        self.driver.find_element_by_xpath(HomePageLocators.select_location_text_box).click()
        logging.info('clicking on select location text box')
        time. sleep(2)
        location_list=self.driver.find_elements_by_xpath(HomePageLocators.select_location_list)
        print(len(location_list))
        select_loc = 'HAL 1st Stage'
        choose_location(location_list,select_loc)
        self.choose_date_and_time()
        self.driver.find_element_by_xpath(HomePageLocators.start_ordering_button).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FoodSelectionPageLocators.place_order_dialog_box_button))
        )
        print(element.text)
        return element.text

        
    def choose_date_and_time(self):
        self.driver.find_element_by_xpath(HomePageLocators.select_date_and_time_button).click()
        time.sleep(2)
        dates = self.driver.find_elements_by_xpath(HomePageLocators.dates_list)
        dates[1].click()
        time.sleep(2)
        hours = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,HomePageLocators.hours_list))
        )
        time.sleep(2)
        hours[1].click()
        minutes_l = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH,HomePageLocators.minutes_list))
        )
        time.sleep(2)
        minutes_l[1].click()



    def start_ordering_for_pickup(self):
            print('sel fn........')
            sel=Select(self.driver.find_element_by_id('expedOpSelect'))
            sel.select_by_visible_text('Pickup')
            self.choose_date_and_time()
            self.driver.find_element_by_xpath(HomePageLocators.start_ordering_button).click()
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FoodSelectionPageLocators.place_order_dialog_box_button))
            )
            print(element.text)
            return element.text







def choose_location(location_list, select_location):
    for location in location_list:
            if(location.text == select_location):
                location.click()
                print('Clicked on', select_location)
                break
            else:
                continue
