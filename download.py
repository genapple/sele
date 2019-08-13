from selenium import  webdriver
import  os
fp=webdriver.Chrome()
fp.set_preference("browser.download.folderbist",2)
fp.set_preferenve("browser.download.manager.showWhenStartting",False)
