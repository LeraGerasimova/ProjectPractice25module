import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r'C:/Users/Public/Driver/chromedriver.exe')
    pytest.driver.get("http://petfriends1.herokuapp.com/login")

    yield

    pytest.driver.quit()

@pytest.fixture()
def path_to_pets():
    # ввод email
    pytest.driver.find_element_by_id('email').send_keys('valerygerasimova92@yandex.ru')

    # ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys('12345678')

    # нажимаем на кнопку ВХОД
    pytest.driver.find_element_by_css_selector('button[type = "submit"]').click()

    # нажимаем на вкладку Мои питомцы
    pytest.driver.find_element_by_link_text("Мои питомцы").click()