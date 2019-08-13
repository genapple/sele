
#-*- coding:UTF-8 -*-
from selenium import  webdriver
from selnium.webdriver.common.action_chains import  ActionChains
#引入ActionChains 类
webdriver.get("http://yunpan.360.cn")
#定位到要右击的元素
right_click=driver.find_elemeny_by_id("quc_account_387044760")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
