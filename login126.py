#-*- coding:UTF-8 -*-
from selenium import  webdriver
import  time
# from selenium.webdriver.commom.by import  By
driver=webdriver.Chrome()
driver.get("http://www.126.com")
driver.find_element_by_id("switchAccountLogin").click()
#iframe嵌套的元素定位不到，所以必须先切换到iframe 里面去
iframe=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
username= driver.find_element_by_name("email")
username.send_keys("xxxx")
password=driver.find_element_by_name("password")
password.send_keys("xxxx")
driver.find_element_by_id("dologin").click()
