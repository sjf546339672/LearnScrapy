# coding: utf-8

import requests
import chardet

response = requests.get("http://www.baidu.com/")
print(chardet.detect(response.content))
response.encoding = chardet.detect(response.content)["encoding"]  # 检测网页的编码
print(response.text)