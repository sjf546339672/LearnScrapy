# coding: utf-8
import re
from urllib import urlopen

import selenium
import selenium.webdriver

mystr = """
<div class="rt">
    共2106条职位
</div>
"""

restr = """<div class="rt">([\s\S]*?)</div>"""
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(mystr)
print mylist


def download(serchname):
    url = "https://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000&" \
          "keyword=" + serchname + "&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    driver = selenium.webdriver.Firefox(executable_path=r"E:\ruanjanfolder\Firefox\geckodriver.exe")
    driver.get(url)
    pagesource = driver.page_source  # 抓取网页源代码
    restr = """<div class="rt">([\s\S]*?)</div>"""
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)

    newstr = mylist[0].strip()  # 前后空格空白符
    print newstr
    restr = """(\\d+)"""  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(newstr)

    driver.close()  # 关闭
    return mylist[0]


pythonlist = ["python", "python 运维", "python 测试", "python 数据", "python web"]
for pystr in pythonlist:
    print pystr, download(pystr)