from pages.main_page import MainPage
from pages.login_page import LoginPage

# def test_guest_can_go_to_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/'
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

# def test_guest_should_see_login_link(browser):
#     link = 'http://selenium1py.pythonanywhere.com/'
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open() # Гость открывает главную страницу 
    page.go_to_basket() # Переходит в корзину по кнопке в шапке сайта
    page.should_not_be_item_basket()
    page.should_be_empty_basket_text()

# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста 

# pytest -v --tb=line --language=en test_main_page.py
# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s: pytest -s test_main_page.py
