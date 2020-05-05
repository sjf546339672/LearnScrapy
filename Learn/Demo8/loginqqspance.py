# coding: utf-8
import urllib
import urllib2

import selenium
import selenium.webdriver
import time
from constant import chromedriver_path


def download(url):
    driver = selenium.webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)
    time.sleep(3)
    driver.switch_to_frame("login_frame")
    elem = driver.find_element_by_id("switcher_plogin")
    elem.click()
    time.sleep(3)
    username = driver.find_element_by_id("u")
    password = driver.find_element_by_id("p")
    loginbtn = driver.find_element_by_id("login_button")
    username.send_keys("546339672")
    password.send_keys("sjfsjfsjf123456")
    loginbtn.click()
    time.sleep(5)
    # print(driver.find_element_by_class_name("title-text ui-mr5").text)
    url = driver.find_element_by_id("QM_OwnerInfo_Icon").get_attribute("src")
    print(url)
    urllib.urlretrieve(url, filename="touxiang.jpg")
    driver.close()


download("https://qzone.qq.com/")