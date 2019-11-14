from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    buttons=driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/button[1]/span")
    buttons.click()
    message=driver.find_element_by_xpath("//div[@role='alert']/p")
    text=message.text
    print(text)
    assert "这是一条消息" in text
    sleep(5)

def test_page_source(driver):
    driver.get("http://ui.yansl.com/")
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/div").click()
    driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()
    source=driver.page_source
    print(source)
    assert "手工关闭提示" in source
    sleep(5)