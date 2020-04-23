# coding: utf-8
# 主要是对于登录的网页进行数据的抓取
import urllib
import urllib2
import cookielib

# 创建一个对象存储cookie
cookie = cookielib.CookieJar()
# 创建一个对象使用cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
# 创建一个打开器，使用cookie
opener = urllib2.build_opener(cookie_handler)
# 添加浏览器模拟
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
data = {"email": "18365597692", "password": "sjf18365597692"}
# 对数据进行编码
data = urllib.urlencode(data)
loginurl = "http://www.renren.com/PLogin.do"
# 发起请求，post请求，抓取cookie
request = urllib2.Request(loginurl, data)
# 载入cookie进行登录
opener.open(request)
url = "http://www.renren.com/969717682"
response_index = opener.open(url)
print(response_index.read())









































