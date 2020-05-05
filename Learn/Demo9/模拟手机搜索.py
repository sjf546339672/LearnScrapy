# coding: utf-8

from selenium import webdriver
import time
from constant import chromedriver_path


def shoujisousuo():
    mobilesetting = {"deviceName": "iPhone 6 Plus"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobilesetting)
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path)
    driver.set_window_size(400, 700)
    driver.maximize_window()
    driver.get("http://www.baidu.com/")
    time.sleep(1)
    elem = driver.find_element_by_id("index-kw")
    elem.send_keys(u"韩红")
    time.sleep(3)
    button = driver.find_element_by_id("index-bn")
    button.click()

    time.sleep(10)
    driver.close()


shoujisousuo()






