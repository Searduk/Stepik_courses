import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
driver.get(link)

num_1 = driver.find_element(By.CSS_SELECTOR, '#num1')
num_2 = driver.find_element(By.CSS_SELECTOR, '#num2')
check = Select(driver.find_element(By.TAG_NAME, 'select'))
button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default')

try:
    Sum = (int(num_1.text) + int(num_2.text))
    check.select_by_value(str(Sum))
    button.click()

finally:
    print(driver.switch_to.alert.text.split()[-1])
    time.sleep(30)
    driver.quit()