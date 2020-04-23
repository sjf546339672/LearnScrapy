# coding: utf-8

# https://sou.zhaopin.com/?jl=杭州&kw=python&kt=3
# https://sou.zhaopin.com/?p=1&jl=%E6%9D%AD%E5%B7%9E&kw=python&kt=3

import urllib
import re
import selenium

from selenium import webdriver
from constant import chromedriver_path


def download():
    base_url = "https://sou.zhaopin.com/"
    data = {
        "p": "1",
        "jl": "杭州",
        "kw": "python",
        "kt": "3",
    }
    data = urllib.urlencode(data)
    url = base_url + "?" + data
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(url)
    pagesource = driver.page_source
    print(pagesource)


download()

