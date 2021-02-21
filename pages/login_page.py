from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        assert 'login' in self.browser.current_url, 'Login word is not presented in URL'
    
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина #login_form
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице #register_form
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, browser, email, password):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        self.browser.find_element(By.CSS_SELECTOR, '[name="registration-email"]').send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '[name="registration-password1"]').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '[name="registration-password2"]').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '[name="registration_submit"]').click()

