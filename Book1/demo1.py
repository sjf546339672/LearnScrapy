# coding: utf-8
import urllib
import urllib.request as urllib2
from urllib.error import URLError

import re


def download(url, num_retries=2, user_agent="wswp"):
    print("download:{}".format(url))
    headers = {"User-agent": user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except URLError as e:
        print("download error", e.reason)
        html = None
        if num_retries > 0:
            if (hasattr(e, "code")) and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall("<loc>(.*?)</loc>", sitemap)
    for link in links:
        html = download(link)
        print(html)


print(crawl_sitemap("http://example.webscrping.com/sitemap.xml"))

"""

     
deal_gitlab_api()
"""














