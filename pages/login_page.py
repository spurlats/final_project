from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        assert 'login' in self.browser.current_url, 'Login word is not presented in URL'
    
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина #login_form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице #register_form
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'