# coding: utf-8

from selenium import webdriver
import time
from constant import chromedriver_path

driver = webdriver.Chrome(chromedriver_path)
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").submit()

time.sleep(7)
js = "window.scrollTo(200, 550)"
driver.execute_script(js)
time.sleep(3)
driver.close()






