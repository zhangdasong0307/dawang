import os

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#上课的conftest，用不着allure，所以标题用，除了test_allure不能用
@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../chrome-78/chromedriver.exe'))      #打开谷歌浏览器
    #调整浏览器大小最大化
    #driver.maximize_window()

    #隐士等待
    driver.implicitly_wait(5) #隐式等待，设置等待时长5


    yield driver        #之后操作一下命令
    driver.close()      #关闭浏览器


