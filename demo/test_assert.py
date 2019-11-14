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