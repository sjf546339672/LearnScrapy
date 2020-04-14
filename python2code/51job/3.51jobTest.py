# encoding:utf-8
import selenium  # 测试框架
import selenium.webdriver  # 模拟浏览器
import re


def getnumberbyname(searchname):
    url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=040000&keyword=" + searchname + "&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"
    driver = selenium.webdriver.Firefox()  # 调用火狐狸浏览器
    driver.get(url)  # 访问链接
    pagesource = driver.page_source  # 抓取网页源代码
    # print pagesource  打印源代码
    restr = """<div class="rt">([\s\S]*?)</div>"""  # 正则表达式，（）只要括号内的数据,如果正则抓取失败，空白字符
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)

    newstr = mylist[0].strip()  # 前后空格空白符
    print(newstr)
    restr = """(\\d+)"""  # 正则表达式，（）只要括号内的数据
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(newstr)

    driver.close()  # 关闭
    return mylist[0]


print(getnumberbyname("java"))
