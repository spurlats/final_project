from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_same_product_name()
        self.should_be_same_product_price()

    
    def should_be_product_url(self):
        assert 'promo=newYear' in self.browser.current_url, 'It is not product page!'

    def should_be_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, 'Product name is not the same!'
    
    def should_be_same_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == product_price_in_basket, 'Product price is not the same!'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    # Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). 
    # Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный 
    # код.

    # Нажимаем на кнопку "Добавить в корзину".
    
    # *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), 
    # который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. 
    # Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, 
    # который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, 
    # в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат

#     Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, 
#     который вы действительно добавили.
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
