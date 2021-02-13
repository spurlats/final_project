from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time



def test_guest_can_add_product_to_basket(browser):
    
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    
    page.solve_quiz_and_get_code()

    page.should_be_product_url()
    
    page.should_be_same_product_name()
    
    page.should_be_same_product_price()






# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s: pytest -s test_product_page.py