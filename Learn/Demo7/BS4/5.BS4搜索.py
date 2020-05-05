# coding: utf-8

from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'html5lib')

# 查询第一个标签
print(soup.find('p'))

# 查询所有的标签
print(soup.find_all('p'))
print(soup.find_all('p')[0])
print(soup.find_all('p')[1])
print(soup.find_all('p')[2])

# 使用正则进行提取
for tag in soup.find_all(re.compile("^t")):
    print(tag.name)

# 按照列表，有一个符合条件即可
for i in soup.find_all(["title", "body"]):
    print(i)

# 按照id
for i in soup.find_all(id="link3"):
    print(i)

# 限定查找a标签的class
for i in soup.find_all("a", class_="sister"):
    print(i)

# 精确等于
for i in soup.find_all(text='The Dormouse\'s story'):
    print(i)

# 其中一个满足即可
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))

# 正则表达式
for i in soup.find_all(text=re.compile("Dormouse")):
    print(i)









