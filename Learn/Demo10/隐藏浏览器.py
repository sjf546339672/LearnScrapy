# coding: utf-8

import pyvirtualdisplay
import selenium.webdriver
from constant import chromedriver_path

display = pyvirtualdisplay.Display(size=(1024, 768))
display.start()

driver = selenium.webdriver.Chrome(chromedriver_path)
driver.get("http://www.baidu.com/")
print(driver.page_source)
driver.close()
