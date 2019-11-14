import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#上课的conftest，用不着allure，所以标题用，除了test_allure不能用
@pytest.fixture(scope='session')
def driver():
    driver=webdriver.Chrome('../chromedirve78/chromedriver.exe')        #打开谷歌浏览器
    #调整浏览器大小最大化
    #driver.maximize_window()

    #隐士等待
    driver.implicitly_wait(5) #隐式等待，设置等待时长5
    #显示等待
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC #定义了变量EC表示expected_conditions
    #
    # WebDriverWait(driver,5,0.5).until(
    #     EC.presence_of_element_located((By.XPATH,'//*[@id="form"]/form/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div'))
    # )


    yield driver        #之后操作一下命令
    driver.close()      #关闭浏览器
