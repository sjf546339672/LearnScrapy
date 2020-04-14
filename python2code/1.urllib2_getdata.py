# coding:utf-8
# print ("hello  ")#中国
from urllib.request import urlopen


def download1(url):
    return urlopen(url).read()  # 读取全部网页


def download2(url):
    return urlopen(url).readlines()  # 读取每一行的网页数据，压入到列表


def download3(url):
    response = urlopen(url)  # 网页抽象为文件
    while True:
        line = response.readline()  # 读取一行
        if not line:
            break
        print(line)


url = "http://www.baidu.com"  # urlopen只能处理http, 不可以处理https
print(download3(url))