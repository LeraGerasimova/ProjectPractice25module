import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# проверяем что на странице со списком питомцев пользователя есть все питомцы

def test_all_pets_are_present(path_to_pets):
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    ## Сохраняем в переменную all_pets элементы статистики
    all_pets = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector(".table.table-hover tbody tr")

    # Получаем количество питомцев из данных статистики
    number = all_pets[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получаем количество карточек питомцев
    number_of_pets = len(pets)

    # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets