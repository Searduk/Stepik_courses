from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Проверка на первой форме регистрации
    # link = "http://suninjuly.github.io/registration1.html"

    # Проверка на второй форме регистрации
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    field_1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
    field_2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
    field_3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')

    field_1.send_keys("Обязательное имя")
    field_2.send_keys("Обязательное отчество")
    field_3.send_keys("Обязательная фамилия")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
