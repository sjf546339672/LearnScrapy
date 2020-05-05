# coding: utf-8
from selenium import webdriver
import time
from constant import chromedriver_path

# https://www.kuaidaili.com/free/inha/3/


def download_daili(url):
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)
    elems = driver.find_elements_by_xpath("//tbody/tr")
    for elem in elems:
        print(elem.find_elements_by_xpath("./td")[0]).text
        print(elem.find_elements_by_xpath("./td")[1]).text
    driver.close()


download_daili("https://www.kuaidaili.com/free/inha/3/")


