# coding: utf-8

import urllib
import urllib2
import re
from constant import headers


def gettiebalistnumbers(name):
    base_url = "https://tieba.baidu.com/f?"
    word = {"kw": name}
    word = urllib.urlencode(word)
    url = base_url + word
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()

    restr = "<span class=\"card_infoNum\">([\s\S]*?)</span>"
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(data)
    tienumbers = eval(mylist[0].replace(",", ""))

    return tienumbers


print gettiebalistnumbers("python")


def gettiebalist(name):
    tiebalist = []
    return tiebalist


def geturllistfrompage(url):
    urllist = []
    return urllist


def getemaillistfrompage(url):
    emaillist= []
    return emaillist

