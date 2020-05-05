# coding: utf-8

from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- E
lsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie<
/a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilli
e</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# HTML5解析 ,只是解析方法不一样，结果一样
soup = BeautifulSoup(html, "html5lib")

# 根据标签
print(soup.select("head"))
print(soup.select("a"))
print(soup.select("p"))

# 根据类型名
print(soup.select(".title"))
print(soup.select(".sister"))

# 根据id
print(soup.select("#link3"))
print(soup.select("#link2"))

# p标签内部的id=link1
print(soup.select("p #link1"))
print(soup.select(".title"))

# >标签层级
print(soup.select("body > p"))

# 标签为a的class=sister元素
print(soup.find_all("a", class_="sister"))
print(soup.select("a[class=\"sister\"]"))

# 抓取标签之间的内容
print(soup.select("title")[0].string)
print(soup.select("title")[0].get_text())






