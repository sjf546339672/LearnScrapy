# coding: utf-8

import selenium.webdriver
import time
from constant import chromedriver_path

options = selenium.webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values": {"images": 2}}
options.add_experimental_option("prefs", prefs)  # 不加载图片
driver = selenium.webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)
driver.get("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D2%FC%B3%C9&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111")

time.sleep(10)
driver.close()









