#-*- coding:UTF-8 -*-
from selenium import  webdriver
driver=webdriver.Chrome()
driver.get("http://www.youdao.com")
#获得cookie 信息
# cookie=driver.get_cookies()
#将获得cookie 的信息打印
# print cookie
#向浏览器中写入cookie信息
driver.add_cookie({'name':'key-aaa','value':'value-bbbb'})
#遍历cookies中的name和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print ("%s -> %s" %(cookie['name'],cookie['value']))
driver.quit()
