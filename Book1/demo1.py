# coding: utf-8
import re
import urllib
from urllib import request
from urllib.error import URLError


def download(url, user_agent='wswp',num_retries=2):
    try:
        html = request.urlopen(url).read()
    except URLError as e:
        print(e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries - 1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for i in links:
        html = download(i)
        print(html)

# t = crawl_sitemap('http://example.webscraping.com/sitemap.xml')
# print(t)  # http://example.webscraping.com/view/1



# http://example.num_webscraping.com/places/default/view/5
import itertools

max_errors = 5
num_errors = 0

for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/{}'.format(page)
    print(url)
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
        else:
            print(html)
            num_errors = 0


















