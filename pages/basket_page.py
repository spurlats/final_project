from .base_page import BasePage
from .locators import BasketPageLocators

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

class BasketPage(BasePage):
    def should_be_main_page(self):
        self.should_not_be_item_basket()
        self.should_be_empty_basket_text()

    def should_not_be_item_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Basket item is presented, but should not be"

    def should_be_empty_basket_text(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        for empty_text in empty_texts:
            if empty_text in text:
                return True
        return False
