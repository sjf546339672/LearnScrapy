# coding: utf-8

import urllib
import urllib2
import lxml
import lxml.etree
import re

from constant import headers

url = "https://search.51job.com/list/080200,000000,0000,00,9,99,python,2,1.html"


def download(url):
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connectin", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()
    mytree = lxml.etree.HTML(data)
    mystr = (mytree.xpath("//*[@class='rt']/text()"))[0].strip()
    regex = re.compile("\d+", re.IGNORECASE)
    number = regex.findall(mystr)[0]
    return number


print(download(url))
