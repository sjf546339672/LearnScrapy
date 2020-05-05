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

soup = BeautifulSoup(html, 'lxml')
soup_html = BeautifulSoup(html, 'html.parser')
soup_html5lib = BeautifulSoup(html, 'html5lib')

print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.p.attrs)
print(soup.p['class'])
print(soup.p['name'])
print(soup.title.string)

