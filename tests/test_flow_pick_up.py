"""
this module will have test cases of home page
"""
import sys
import unittest
import logging
import HtmlTestRunner
import xlrd
from selenium import webdriver
sys.path.append('..')
from pages.home_page import HomePage
from pages.food_listing import FoodSelectionPage
from pages.place_order import PlaceOrder
from pages.order_status import OrderStatus
from configparser import ConfigParser



class TestPickUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('In test case 1.....')
        # cls.excel_file = pd.ExcelFile('')
        cls.config = ConfigParser()
        cls.config.read('./../utilities/Config.cfg')
        print(cls.config.get('environment_variables', 'base_url'))
        # logging.basicConfig(filename=cls.config.get('environment_variables', 'log_path'),
        #             format='%(asctime)s %(message)s',
        #             filemode='w')
        browser_path = cls.config.get('environment_variables', 'browser_path')
        cls.driver = webdriver.Chrome(executable_path = browser_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        url=cls.config.get('environment_variables', 'base_url')
        cls.driver.get(url)
        # cls.logger = logging.getLogger()
        # cls.logger.setLevel(logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        logging.info('Completed test case 1...')
        cls.driver.close()
        cls.driver.quit()

    def test_home_page(self):
        logging.debug('started first test case')
        print('Inside test home page')
        home_page_obj = HomePage(self.driver)
        next_page_obj_str = home_page_obj.start_ordering_for_pickup()
        assert next_page_obj_str == 'Ok! Place Order'

    def test_validate_food_selection(self):
        print('started second test case')
        food_sel_obj = FoodSelectionPage(self.driver)
        # is_empty = food_sel_obj.check_cart_is_empty()
        next_page_obj_str = food_sel_obj.add_food_to_cart_and_login()
        
        #validation whether items are added into the cart
        """assert is_empty == 'CART EMPTY'
        food_sel_obj.validate_food_list()
        is_not_empty = FoodSelectionPage(self.driver)
        print(is_not_empty)
        assert is_not_empty != 'CART EMPTY'"""
    
    def test_validate_order_food(self):
        place_order_obj = PlaceOrder(self.driver)
        place_order_obj.select_saved_address()

    def test_validate_order_status(self):
        order_status_obj = OrderStatus(self.driver)
        order_status=order_status_obj.is_order_id_present()
        assert order_status == True




if __name__ == '__main__':
    testrunner=HtmlTestRunner.HTMLTestRunner(output='./../outputs')
    unittest.main(testRunner=testrunner)

    
    


