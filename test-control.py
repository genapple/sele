#-*- coding:UTF-8 -*-
from selenium import  webdriver
import time
def driver_control():
    driver=webdriver.Chrome()
    driver.get("http://m.mail.10086.cn")
    print (u"设置浏览器宽489、高800 显示")
    driver.set_window_size(480,800)
    # driver.maximize_window()
    #模拟浏览器刷新
    driver.refresh()
    time.sleep(2)
    driver.quit()
def driver_youdao():
    driver=webdriver.Chrome()
    driver.get("https://www.youdao.com/")
    driver.find_element_by_id('query').send_keys("hello")
    #提交输入框的内容
    driver.find_element_by_id("query").click()
    driver.quit()
def driver_baidu():
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    size=driver.find_element_by_id("kw").size
    print size

    #返回百度页面底部备案信息
    text=driver.find_element_by_id("cp").text
    print  text
    #返回元素的属性值。可以是id，name,type或其他任意属性
    attribute=driver.find_element_by_id("kw").get_attribute("type")
    print attribute
    #返回元素是否可见，返回结果是True or False
    result=driver.find_element_by_id("kw").is_displayed()
    print result
    driver.quit()

driver_baidu()





