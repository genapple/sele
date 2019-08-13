#-*- coding:UTF-8 -*-
from selenium import  webdriver
import  time
driver=webdriver.Chrome()
driver.implicity_wait(10)
driver.get("http://www.baidu.com")
#获得百度搜索窗口句柄
search_windows=driver.current_window_handle()
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()
#h获得当前所有打开窗口的句柄
all_handles=driver.window_handles
#进入注册窗口
for handle in all_handles:
    if handle!=search_windows:
        driver.switch_to.window(handle)
        print ("now register window!")
        driver.find_element_by_name("account").send_keys("13917408993")
        driver.find_element_by_name("password").send_keys("yss135792")
        time.sleep(2)
        

