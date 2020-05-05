# coding: utf-8
import time
import urllib2
import urllib
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
    time.sleep(5)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(10)
    driver.close()


jingdong("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F")





