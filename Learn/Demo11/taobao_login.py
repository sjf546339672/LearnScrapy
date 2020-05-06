# coding: utf-8
import selenium
import lxml
import lxml.etree
import time
import requests
import selenium.webdriver
from constant import chromedriver_path


def taobao():

    # driver = selenium.webdriver.Chrome(executable_path=chromedriver_path)
    driver = selenium.webdriver.Firefox()
    driver.get("https://login.taobao.com/member/login.jhtml")

    user = driver.find_element_by_id("fm-login-id")
    password = driver.find_element_by_id("fm-login-password")
    user.clear()
    password.clear()
    user.send_keys("18365597692")
    time.sleep(3)
    password.send_keys("sjf18365597692")
    time.sleep(8)
    loginbtn = driver.find_element_by_class_name("fm-button fm-submit password-login")
    loginbtn.click()
    print("开始会话")
    req = requests.session()
    cookies = driver.get_cookies()
    for cookie in cookies:
        req.cookies.set(cookie["name"], cookie["value"])
    req.headers.clear()
    newpage = req.get("https://cart.taobao.com/cart.htm?")
    print("会话结束")
    # mytree = lxml.etree.HTML(newpage.text)
    print(newpage.text)

    time.sleep(10)
    driver.close()


taobao()