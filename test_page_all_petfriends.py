import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets(testing):
    pytest.driver.implicitly_wait(10)

    #ввод email
    pytest.driver.find_element_by_id('email').send_keys('valerygerasimova92@yandex.ru')
    #ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys('12345678')
    #Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type = "submit"]').click()
    #Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text=="PetFriends"

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0