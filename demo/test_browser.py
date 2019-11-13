from time import sleep

#from selenium import webdriver
# #打开浏览器
# driver = webdriver.Chrome('../chrome-78/chromedriver.exe')
#
# sleep(2)
#
# #调整浏览器窗口大小
# driver.maximize_window()
# sleep(2)
#
# #driver.minimize_window()
# #sleep(10)

def test_browser(driver):
#打开网址
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.get("http://www.jd.com")
    sleep(2)

    #后退
    driver.back()
    sleep(2)

    #前进
    driver.forward()
    sleep(2)
    #刷新
    driver.refresh()
    sleep(2)



    #关闭浏览器，不退出driver
    #driver.close()


    #关闭浏览器，并退出driver
    #driver.quit()



    #driver.maximize_window()