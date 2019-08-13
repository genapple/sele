#-*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains  import  ActionChains
import  time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#鼠标悬停在设置按钮

link=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()
#打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
save=driver.find_element_by_class_name("prefpanelgo")
#为什么放在那个位置就会看不到这个按钮呢
driver.maximize_window()
save.click()
time.sleep(2)
#接受警告框
driver.switch_to_alert().accept()

driver.quit()