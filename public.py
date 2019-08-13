#-*- coding:UTF-8 -*-
from selenium  import  webdriver
#登陆
class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_id("switchAccountLogin").click()
        iframe=driver.find_element_by_tag_name("iframe")
        driver.switch_to_frame(iframe)
        driver.find_element_by_name("email").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("dologin").click()

    def logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()
# driver=webdriver.Chrome()
# driver.get("http://mail.163.com/")
# driver.implicitly_wait(2)
# loginTest=Login()
# loginTest.user_login(driver)
# loginTest.logout(driver)