import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get('http://suninjuly.github.io/explicit_wait2.html')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    x_value = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_value)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x_value.text))
    subm_btn = browser.find_element(By.ID, 'solve')
    subm_btn.click()


finally:
    time.sleep(5)
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(5)
    browser.quit()
