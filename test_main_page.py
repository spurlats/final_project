from selenium.webdriver.common.by import By
import time

# def test_find_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     browser.get(link)
#     time.sleep(10)
#     item = browser.find_element(By.CSS_SELECTOR, (".btn.btn-lg.btn-primary.btn-add-to-basket"))
#     assert item is not None, "No such element Exception"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# pytest -v --tb=line --language=en test_main_page.py
