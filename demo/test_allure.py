import allure


@allure.feature("一级分类")
@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http://www.baidu.com",'bug')
@allure.testcase("http://www.baidu.com",'用例')
def test_report(driver):
    url="http://ui.yansl.com/#/checkbox"   #登录网站
    with allure.step("打开网页:{}".format(url)):pass  #with，插入、allure.step，测试步骤的标题、pass。表示到此结束，下面没有代码
    driver.get(url)   #打开网址
    with allure.step("点击多选框:{}".format('//*[@id="form"]/form/div[1]/div/input[1]')):  #.format 赋值
        allure.attach(driver.get_screenshot_as_png(),'图片1',allure.attachment_type.PNG)   #allure.attach，引入文件#driver.get_screenshot_as_png()，附件内容、''，附件名字、allure.attachment_type.PNG，附件类型
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[1]').click()   #定位xpath
    with allure.step("点击多选框:{}".format('//*[@id="form"]/form/div[1]/div/input[2]')):
        allure.attach(driver.get_screenshot_as_png(),'图片2',allure.attachment_type.PNG)
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[2]').click()