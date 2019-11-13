from time import sleep

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")   #fixture函数
def driver():
    driver = webdriver.Chrome('../chrome-78/chromedriver.exe') #在谷歌浏览器中打开网页
    sleep(2)

#调整浏览器窗口大小
    driver.maximize_window()
    sleep(2)
    yield driver   #运行完其他的之后，再运行以下的内容
    driver.quit()
