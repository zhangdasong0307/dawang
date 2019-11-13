from time import sleep

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome('../chrome-78/chromedriver.exe')
    sleep(2)

#调整浏览器窗口大小
    driver.maximize_window()
    sleep(2)
    yield driver
    driver.quit()
