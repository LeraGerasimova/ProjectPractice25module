import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pets_have_a_different_names(path_to_pets):
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную pets элементы карточек питомцев
    data_pets = pytest.driver.find_elements_by_css_selector(".table.table-hover tbody tr")
    '''Перебираем данные из data_pets, оставляем имя, возраст, породу. Остальное меняем на пустую строку
       и разделяем по пробелу. Выбираем имена и добавляем их в список pets_name'''
    pets_name = []
    for i in range(len(data_pets)):
        data_pet = data_pets[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    '''Перебираем имена, если имя повторяется, то прибавляем к счетчику r единицу.
       Проверяем, если r == 0, то повторяющихся имён нет'''
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)
