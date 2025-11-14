import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators

# session, module, class, function
@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--window-size=1200,600') # добавили ещё настройку —-window-size запускает браузер с заданным разрешением экрана.
    # Полезно, когда нужно протестировать интерфейс в системе с определённым разрешением.
    service = Service("C:\WebDriver\bin\chromedriver.exe") # Путь до нужного драйвера
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(main_site)
    yield browser
    browser.quit()