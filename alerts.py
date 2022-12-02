import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/alert_accept.html'
link_2 = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link_2)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Elements:

magick_btn = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')


try:
    magick_btn.click()
    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # alert=browser.switch_to.alert
    # alert.accept()
    # calc(x_value.text)
    x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x_value.text))
    just_btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    just_btn.click()

finally:
    time.sleep(10)
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(5)
    browser.quit()
