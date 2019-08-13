#-*- coding:UTf-8 -*-
import time
from time import  sleep
from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.DEBUG)
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
def  obviouswait():
    element = WebDriverWait(driver, 10,0.5).until(
            EC.presence_of_element_located((By.ID, "kw")))
    element.send_keys('selenium')
    time.sleep(1)
    driver.quit()
def implicitly_wait1():
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
def execute_script():
#设置窗口浏览器大小
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    time.sleep(2)
    #通过kavascript设置浏览器窗口的滚动条位置
    js="window.scrollTo(100,450)"
    driver.execute_script(js)
    time.sleep(3)
    driver.quit()
def screenshot():
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(2)
    #截取当前窗口，并指定或截图图片的保存位置
    driver.get_screenshot_as_file(r"C:\Users\shasha.yan\Pictures\baidu_img.png")
    driver.quit()
screenshot()

