# coding: utf-8
import urllib
import urllib2


def download():
    # "https://sou.zhaopin.com/?jl=653&kw=python"
    jl = {"jl": "杭州", "kw": "python"}
    result_encode = urllib.urlencode(jl)
    url = "https://sou.zhaopin.com/?{}".format(result_encode)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    print(response.code)
    print(response.read())


download()

