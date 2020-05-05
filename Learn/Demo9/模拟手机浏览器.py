# coding: utf-8

from selenium import webdriver
import time


# 设置
mobilesetting = {"deviceName": "iPhone 6 Plus"}
options = webdriver.ChromeOptions()  # 选项
options.add_experimental_option("mobileEmulation", mobilesetting)
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(400, 800)
driver.maximize_window()  # 全屏
driver.get("http://www.taobao.com/")
time.sleep(10)
driver.close()







