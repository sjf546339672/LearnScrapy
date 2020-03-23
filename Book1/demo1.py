# coding: utf-8

from urllib import request


def download(url):
    return request.urlopen(url).read()


