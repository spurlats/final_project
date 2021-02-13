from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')

    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong')

    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong')