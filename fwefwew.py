from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.common.exceptions import NoAlertPresentException # в начале файла


link = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'

browser = webdriver.Chrome()
browser.get(link)
time.sleep(10)
# browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket').click()

# def solve_quiz_and_get_code():
#     alert = browser.switch_to.alert
#     x = alert.text.split(" ")[2]
#     answer = str(math.log(abs((12 * math.sin(float(x))))))
#     alert.send_keys(answer)
#     alert.accept()
#     try:
#         alert = browser.switch_to.alert
#         alert_text = alert.text
#         print(f"Your code: {alert_text}")
#         alert.accept()
#     except NoAlertPresentException:
#         print("No second alert presented")

# solve_quiz_and_get_code()

a = browser.find_element(By.CSS_SELECTOR, '#content_inner p').text
print(a)
# b = browser.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main .price_color').text
# print(b)
# c = browser.find_element(By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong').text
# print(c)
# d = browser.find_element(By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong').text
# print(d)