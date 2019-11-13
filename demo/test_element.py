from time import sleep

import autoit
from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    input = driver.find_element_by_xpath("//input[@name='t1']")
#清空
    input.clear()
#输入
    input.send_keys("写什么？读什么？怎么读？")
    sleep(2)

def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    radio=driver.find_element_by_xpath("//input[@name='sex'][2]")
#点击click
    radio.click()
    sleep(2)



def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select=driver.find_element_by_xpath("(//input[@placeholder='请选择'])[1]")
#点击
    select.click()
    sleep(2)

    option = driver.find_element_by_xpath("(//span[text()='龙须面'])[last()]")
    actions=ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)



def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)
    input = driver.find_element_by_xpath("//input[@placeholder='选择时间']")
#清空
    input.clear()
#输入
    input.send_keys("18:00:00")
    sleep(2)


def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    file = driver.find_element_by_xpath("//label[@class='el-form-item__label']/../div//input")
    # 清空
    file.clear()
    # 输入
    file.send_keys('C:\\Users\\guoy\\Desktop\\login.png')
    sleep(2)

def test_upload(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    upload =driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")
    upload.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoy\\Desktop\\login.png")
    sleep(2)
    autoit.control_click("打开", "Button1")

    sleep(10)

    print('nihao')