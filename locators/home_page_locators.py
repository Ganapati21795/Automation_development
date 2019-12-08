"""
This module have all the web elements in the 
home page
"""
class HomePageLocators:
    """ Home Page Class """
    """Xpaths for Home Page """
    select_location_text_box = "//input[@placeholder='Select Location']"
    select_location_list = "//label[@class = 'localityName']"
    select_date_and_time_button = "//button[contains(@id, 'laterButton')]"
    select_time_button = "//input[text()='Select Time']"
    calender_table = "ui-datepicker-calendar"
    dates_list = "//tbody/tr/td/a"
    hours_list = "//tbody/tr/td/button[contains(@id, 'h') and contains(@class, 'validhour')]"
    minutes_list = "//tbody/tr/td/button[contains(@id, 'm') and contains(@class, 'validminute')]"
    start_ordering_button = "//button[text() = 'Start Ordering']"
    place_order_dialog_box_button = "//button[text()='Ok! Place Order']"
