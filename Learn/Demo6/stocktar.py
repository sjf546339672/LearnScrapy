# coding: utf-8
import urllib
import urllib2
import lxml
import lxml.etree
# http://quote.stockstar.com/fund/open.shtml
# http://quote.stockstar.com/fund/open_5_1_1.html 第一页
# http://quote.stockstar.com/fund/open_5_1_2.html 第二页
from constant import headers


def get_number_pages(url):
    """获取总页数"""
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()
    mytree = lxml.etree.HTML(data)
    # count_page = mytree.xpath("//*[@class=\"noSelect no_trHover\"]//a[last()]//text()")
    count_page = mytree.xpath("//*[@id='datatime']//text()")[0]
    print(count_page)
    return 111


get_number_pages("http://quote.stockstar.com/fund/open.shtml")


