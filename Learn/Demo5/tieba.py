# coding: utf-8
"""爬取贴吧的QQ邮箱"""
import urllib
import urllib2
import re
from constant import headers


def get_tieba_list_numbers(name):
    # 获取所有的贴吧数量、关注人数
    base_url = "https://tieba.baidu.com/f?"
    word = {"kw": name}
    word = urllib.urlencode(word)
    url = base_url + word
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()

    tieba_restr = "<span class=\"card_infoNum\">([\s\S]*?)</span>"
    tieba_regex = re.compile(tieba_restr, re.IGNORECASE)
    tieba_mylist = tieba_regex.findall(data)
    tieba_numbers = eval(tieba_mylist[0].replace(",", ""))

    person_restr = "<span class=\"card_menNum\">([\s\S]*?)</span>"
    person_regex = re.compile(person_restr, re.IGNORECASE)
    person_mylist = person_regex.findall(data)
    person_numbers = eval(person_mylist[0].replace(",", ""))
    return tieba_numbers, person_numbers


def get_tieba_list(name):
    # 获取所有的网页url
    tieba_list = []
    numbers_tuple = get_tieba_list_numbers(name)
    tieba_number = numbers_tuple[0]
    if tieba_number % 50 == 0:
        for i in range(tieba_number//50):
            url = "https://tieba.baidu.com/f?kw={}&pn={}".format(name, str(i*50))
            tieba_list.append(url)
    else:
        for i in range(tieba_number//50+1):
            url = "https://tieba.baidu.com/f?kw={}&pn={}".format(name, str(i * 50))
            tieba_list.append(url)
    return tieba_list


def get_url_list_from_page(url):
    # 获取单个网页中每个用户的url
    url_list = []
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()

    restr = "<ul id=\"thread_list\" class=\"threadlist_bright j_threadlist_bright\">([\s\S]*?)<div class=\"thread_list_bottom clearfix\">"
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)

    table_str = mylist[0]
    table_restr = "href=\"/p/(\d+)\""
    table_regex = re.compile(table_restr, re.IGNORECASE)
    url_title_list = table_regex.findall(table_str)
    for i in url_title_list:
        url = "https://tieba.baidu.com/p/{}".format(i)
        url_list.append(url)
    return url_list


def get_page_data(url):
    # 获取每个用户的点击进去的页面网页源码
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connectin", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()
    return data


def get_email_list_from_page(page_data):
    # 在每个页面中查询出所有的QQ邮箱
    restr = r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})"
    regex = re.compile(restr, re.IGNORECASE)
    email_list = regex.findall(page_data)
    return email_list


for tieba_list in get_tieba_list("python3"):
    for url in (get_url_list_from_page(tieba_list)):
        email_list = get_email_list_from_page(get_page_data(url))
        if len(email_list) != 0:
            print(email_list)

