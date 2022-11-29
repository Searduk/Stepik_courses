from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
driver.get(link)


# Elements:

first_name = driver.find_element(By.CSS_SELECTOR, '[name="firstname"]')
last_name = driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')
email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
file = driver.find_element(By.CSS_SELECTOR, '#file')
submit_btn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')


try:
    first_name.send_keys('Name')
    last_name.send_keys('Lastname')
    email.send_keys('email@domain.ru')
    file.send_keys(file_path)
    submit_btn.click()


finally:
    time.sleep(10)
    print(driver.switch_to.alert.text.split()[-1])
    time.sleep(5)
    driver.quit()
