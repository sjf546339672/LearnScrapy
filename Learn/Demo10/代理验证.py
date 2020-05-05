# coding: utf-8

import urllib2

try:
    httpproxy = urllib2.ProxyHandler({"http": "10.1.100.213"})
    opener = urllib2.build_opener(httpproxy)  # 创建一个打开器
    request = urllib2.Request("http://www.baidu.com/")
    response = opener.open(request, timeout=5)
    print(response.read())
    print("OK")
except:
    print("ON")







