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
soup_lxml = BeautifulSoup(html, 'lxml')  # lxml解析方式
soup_html = BeautifulSoup(html, 'html.parser')  # 常规解析页面
soup_html1 = BeautifulSoup(html, 'html5lib')

# print(soup_lxml.prettify())
# print(soup_html.prettify())
# print(soup_html1.prettify())


















