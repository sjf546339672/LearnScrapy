# coding: utf-8

from selenium import webdriver
import time
from constant import chromedriver_path

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("https://www.51shucheng.net/jiakong/qingyunian/qingyunian1/39559.html")
data = driver.find_elements_by_xpath("/*")
for tag in data:
    print(tag.text)
driver.close()

