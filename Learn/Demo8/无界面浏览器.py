# coding: utf-8

import selenium
import selenium.webdriver
import time

path = r"E:\ruanjanfolder\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver = selenium.webdriver.PhantomJS(path)
driver.get("http://www.qq.com")
time.sleep(2)
driver.save_screenshot("qq.jpg")
print(driver.title)  # 标题
print(driver.page_source)  # 网页源码
driver.close()

