# coding: utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup

from constant import headers


def download(url):
    request = urllib2.Request(url, headers=headers)
    data = urllib2.urlopen(request).read()
    soup = BeautifulSoup(data, "html5lib", from_encoding="utf-8")
    mytable = soup.find_all(id="datalist")
    for line in mytable[0].select("tr"):
        for mydata in line.select("td"):
            print(mydata.get_text())


download("http://quote.stockstar.com/fund/stock_3_1_2.html")






