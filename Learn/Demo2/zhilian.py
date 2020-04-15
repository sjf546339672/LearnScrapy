# coding: utf-8
import urllib
import urllib2


def download():
    url = "https://sou.zhaopin.com/?jl=653&kw=python"
    data = urllib2.urlopen(url)
    print(data)




download()