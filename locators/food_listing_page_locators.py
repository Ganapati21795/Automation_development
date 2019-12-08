"""
This module will be having the locators of all the 
food listing page which comes after clicks on
start ordering button
"""
class FoodSelectionPageLocators:
    """ food selection class """
    place_order_dialog_box_button = "//button[text()='Ok! Place Order']"
    total_product_items = "//div/div/div[contains(@class, 'ProductItem')]"
    for_the_table_list = "//div/div/div[contains(@class, 'ProductItem') and contains(@category, 'For The Table')]"
    crispy_roast_duck = "//div/div/div[contains(@class, 'ProductItem') and contains(@category, 'Crispy roast duck')]"
    wet_noodles = "//div/div/div[contains(@class, 'ProductItem') and contains(@category, 'Wet Noodles')]"
    empty_cart = "//label[contains(text(),'EMPTY')]"
    add_to_cart_button_list = "//a[contains(@class, 'AddToCart')]"
    add_to_cart_sweet_potato_roll= "(//a[contains(@class, 'AddToCart')])[3]"
    add_button_for_wet_noodles = "//div/div/div[contains(@class, 'ProductItem') and contains(@category, 'Wet Noodles')]/child::div/child::a"
    wet_noodles_text = "//div/div/div[contains(@class, 'ProductItem') and contains(@category, 'Wet Noodles')]/child::div/child::div/span"
    checkout_order_button = "//button[text()='CHECKOUT' and @href='#']"
    mobile_number_text_box = "//input[@id= 'cust_phoneNo']"
    proceed_button = "//button[text()= 'PROCEED']"
    invalid_mobile_no = "//label[contains(text(),'Enter Valid Mobile Number')]"
    your_name_text_box = "//input[@id= 'cust_userName']"
    your_email_id_text_box = "//input[@id= 'cust_useremail']"
    invalid_email_id = "//label[contains(text(),'Enter Valid Email ID')]"
    proceed_button_2 = "(//button[text()= 'PROCEED'])[2]"
    category_side_bar = "//a[contains(@sidecat, 'category')]"
    