#!/usr/bin/python
#-*- coding:UTF-8 -*-
from selenium import  webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import  Keys

import sys

reload(sys)

sys.setdefaultencoding("utf8")
print sys.getdefaultencoding()

# #账号登陆：https://passport.baidu.com/v2/?login
driverOptions=webdriver.ChromeOptions()
driverOptions.add_argument('--no-sandbox')
driverOptions.add_argument("start-maximized")
driverOptions.add_argument("disable-infobars")
driverOptions.add_argument("--disable-extensions")
driverOptions.add_argument("--disable-gpu")
driverOptions.add_argument("--disable-dev-shm-usage")


driverOptions.add_argument('--headless')#在不打开浏览器的模式下进行
driverOptions.add_argument(r"user-data-dir=C:\Users\shasha.yan\AppData\Local\Google\Chrome\User Data")
driver=webdriver.Chrome("chromedriver",0,driverOptions)
# driver=webdriver.Chrome(chrome_options=driverOptions)
# driver=webdriver.Chrome()
def login():
    login_url="https://passport.baidu.com/v2/?login"
    driver.get(login_url)
    login_btn=driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn")
    login_btn.click()
    user_ele=driver.find_element_by_id("TANGRAM__PSP_3__userName")
    user_ele.send_keys("13917408993")
    password_ele=driver.find_element_by_id("TANGRAM__PSP_3__password")
    submit_ele=driver.find_element_by_id("TANGRAM__PSP_3__submit")
    password_ele.send_keys("yss135792")
    submit_ele.click()
def reply(num):
    url="http://tieba.baidu.com/f?kw=%D1%EE%D7%CF&fr=ala0&loc=rec&traceid="
    url1="http://tieba.baidu.com/p/6205980376?pn=2"

    driver.get(url1)
    # num=unicode(num,'utf-8')
    #p=driver.find_elements_by_partial_link_text("紫因有你")  #找到符合这个要求的文本，然后再进行处
    wb1=driver.find_element_by_id("ueditor_replace")
    wb2=driver.find_element_by_link_text("发 表")
    # wb3=driver.find_element_by_link_text("用户名登陆")
    text=u"杨紫中餐厅3"

    # text.decode().encode("gbk")
    wb1.send_keys(text)
    wb2.click()


    # ActionChains(driver).key_down(Keys.ENTER,"CTRL").perform()
    # time.sleep(2)
    # print num,
    # driver.quit()
if __name__ == '__main__':
    # string=u"被绯闻、被非议、被黑幕，从未辩解，无需辩解。今夜华筵终散场，功成名遂，满目荒唐。"
    # string=" wohenxihuanni"
    # for count in string:
    #
    #     reply(count)
    reply("test")
