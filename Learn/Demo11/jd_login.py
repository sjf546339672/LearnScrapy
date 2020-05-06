# coding: utf-8
import time
import urllib2
import urllib

import lxml
import lxml.etree
import requests
import selenium
import selenium.webdriver

from constant import chromedriver_path


def jingdong(url):
    driver = selenium.webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(url)
    time.sleep(2)
    elem = driver.find_element_by_xpath("//*[@class=\"login-tab login-tab-r\"]/a")
    elem.click()
    user = driver.find_element_by_id("loginname")
    password = driver.find_element_by_id("nloginpwd")
    loginbtn = driver.find_element_by_id("loginsubmit")
    user.clear()
    password.clear()
    user.send_keys("18365597692")
    password.send_keys("sjf18365597692")
    time.sleep(2)
    loginbtn.click()
    time.sleep(10)
    print("开始会话")
    req = requests.session()  # 会话
    cookies = driver.get_cookies()  # 抓取全部的cookie
    for cookie in cookies:
        req.cookies.set(cookie["name"], cookie["value"])
    # req.headers.clear()
    newpage = req.get("https://cart.jd.com/cart.action")
    print("会话完成")
    print(newpage.text)  # 页面
    mytree = lxml.etree.HTML(newpage.text)
    print(mytree.xpath("//*[@class=\"cell p-sum\"]/strong/text()"))
    time.sleep(10)
    driver.close()


jingdong("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F")





