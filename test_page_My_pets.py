import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#тест, что мы находимся на странице мои питомцы. Испол. перед каждой проверкой явное ожидание
def test_page_my_pets(testing):
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    #ввод email
    pytest.driver.find_element_by_id('email').send_keys('valerygerasimova92@yandex.ru')

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys('12345678')

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    #нажимаем на кнопку ВХОД
    pytest.driver.find_element_by_css_selector('button[type = "submit"]').click()

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    #нажимаем на вкладку Мои питомцы
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    #проверяем, что мы на вкладке Мои питомцы
    assert pytest.driver.current_url == 'http://petfriends1.herokuapp.com/my_pets'