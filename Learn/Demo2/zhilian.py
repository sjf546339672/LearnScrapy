# coding: utf-8
import urllib
import urllib2

from constant import headers


def download():
    # "https://sou.zhaopin.com/?jl=653&kw=python"
    jl = {"jl": "杭州", "kw": "python"}
    result_encode = urllib.urlencode(jl)
    url = "https://sou.zhaopin.com/?{}".format(result_encode)
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    print(response.code)
    print(response.read())

download()

