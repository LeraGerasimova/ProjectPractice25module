import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets_have_name_age_gender(path_to_pets):
    '''Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''
    css_locator = 'tbody>tr'
    data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

    all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
    statistics_pets = all_statistics[1].split(" ")
    all_my_pets = int(statistics_pets[-1])
    assert len(data_my_pets) == all_my_pets