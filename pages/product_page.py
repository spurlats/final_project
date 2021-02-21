from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators

import math

empty_texts = ["سلة التسوق فارغة",
"La seva cistella està buida.",
"Váš košík je prázdný.",
"Din indkøbskurv er tom.",
"Ihr Warenkorb ist leer.",
"Your basket is empty.",
"Το καλάθι σας είναι άδειο.",
"Tu carrito esta vacío.",
"Korisi on tyhjä",
"Votre panier est vide.",
"Il tuo carrello è vuoto.",
"장바구니가 비었습니다.",
"Je winkelmand is leeg",
"Twój koszyk jest pusty.",
"O carrinho está vazio.",
"Sua cesta está vazia.",
"Cosul tau este gol.",
"Ваша корзина пуста",
"Váš košík je prázdny",
"Ваш кошик пустий.",
"Your basket is empty."]


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_same_product_name()
        self.should_be_same_product_price()
        self.add_to_basket()
        self.should_not_be_success_message()
        self.should_not_be_item_basket()
        self.solve_quiz_and_get_code()
    
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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_item_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Basket item is presented, but should not be"

    def should_be_empty_basket_text(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        for empty_text in empty_texts:
            if empty_text in text:
                return True
        return False


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

