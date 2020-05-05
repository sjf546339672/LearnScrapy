# coding: utf-8
import urllib
import urllib2
import ssl
from bs4 import BeautifulSoup
from constant import headers

# https://sou.zhaopin.com/?jl=%E6%9D%AD%E5%B7%9E&kw=python&kt=3


def download(url):
    request = urllib2.Request(url, headers=headers)
    data = urllib2.urlopen(request).read()
    soup = BeautifulSoup(data, "html5lib", from_encoding="utf-8")
    div_list = soup.find_all("div", class_="rt")
    print(div_list[0].string)

download("https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")




