# coding: utf-8
import urllib2
import urllib
import lxml
import lxml.etree

from constant import headers


def download(url):
    request = urllib2.Request(url, headers=headers)
    request.add_header("Commection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()
    mytree = lxml.etree.HTML(data)
    datalist = mytree.xpath("//*[@id='datalist']//tr//td//text()")
    for linedata in datalist:
        print(linedata)


# 基金代码	基金简称	单位净值	  累计净值	日增长额 	日增长率 	申购 	赎回
download("http://quote.stockstar.com/fund/open.shtml")

import ssl
ssl._create_unverified_context()  # 忽略安全 https