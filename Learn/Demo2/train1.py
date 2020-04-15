# coding: utf-8

import urllib

word = {"wd": "李小龙"}

result_encode = urllib.urlencode(word)  # 编码
print(result_encode)
result_code = urllib.unquote(result_encode)  # 解码
print(result_code)
