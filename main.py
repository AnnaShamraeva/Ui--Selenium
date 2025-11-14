import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--window-size=1200,600') # добавили ещё настройку —-window-size запускает браузер с заданным разрешением экрана.
    # Полезно, когда нужно протестировать интерфейс в системе с определённым разрешением.
service = Service(r'C:\WebDriver\bin\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://ya.ru')
time.sleep(1000)
