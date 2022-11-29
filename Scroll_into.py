import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
driver.get(link)

# Elements:

x_value = driver.find_element(By.CSS_SELECTOR, '#input_value')
answer = driver.find_element(By.CSS_SELECTOR, '#answer')
checkbox = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
rad_btn = driver.find_element(By.CSS_SELECTOR, '#robotsRule')
submit_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


result = calc(str(x_value.text))


try:
    driver.execute_script("return arguments[0].scrollIntoView(true);", x_value)
    answer.send_keys(result)
    checkbox.click()
    rad_btn.click()
    submit_btn.click()

finally:
    time.sleep(10)
    print(driver.switch_to.alert.text.split()[-1])
    time.sleep(10)
    driver.quit()



