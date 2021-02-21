from conftest import browser
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time



# def test_guest_can_add_product_to_basket(browser):
    
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
    
#     page.solve_quiz_and_get_code()

#     # page.should_be_product_url()
    
#     page.should_be_same_product_name()
    
#     page.should_be_same_product_price()


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open() # Открываем страницу товара 
#     page.add_to_basket() # Добавляем товар в корзину 
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open() # Открываем страницу товара 
#     page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)    
#     page.open() # Открываем страницу товара
#     page.add_to_basket() # Добавляем товар в корзину
#     page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_disappeared


# def test_guest_can_see_login_link_on_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     page.should_be_login_url()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open() # Гость открывает главную страницу 
#     page.go_to_basket() # Переходит в корзину по кнопке в шапке сайта
#     page.should_not_be_item_basket()
#     page.should_be_empty_basket_text()

class TestUserAddToBasketFromProductPage():
    def should_be_tested(self):
        self.test_user_cant_see_success_message()
        self.test_user_can_add_product_to_basket()
    
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'pt9u0tghwetnq9ur'
        
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()

        login_page.register_new_user(browser, email, password)
        login_page_opened = LoginPage(browser, browser.current_url)
        login_page_opened.should_be_authorized_user()        

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open() # Открываем страницу товара 
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_same_product_name()
        page.should_be_same_product_price()

# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s: pytest -s test_product_page.py