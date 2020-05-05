# coding: utf-8

from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html, 'lxml')  # lxml页面解析
soup1 = BeautifulSoup(html, 'html.parser')  # 常规页面解析
soup2 = BeautifulSoup(html, 'html5lib')  # html5解析，只是解析方法不一样， 结果是一样的

print(soup.title.string)  # 取出标签之间的内容
print(type(soup.name))  # 编码
print(soup.a)
print(soup.a.string)




