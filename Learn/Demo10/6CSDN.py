# coding: utf-8

import urllib2, re, urllib, cookielib

cookie = cookielib.CookieJar()
cookieproc = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieproc)

