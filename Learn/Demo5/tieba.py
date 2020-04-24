# coding: utf-8

import urllib
import urllib2
import re
from constant import headers


def get_tieba_list_numbers(name):
    base_url = "https://tieba.baidu.com/f?"
    word = {"kw": name}
    word = urllib.urlencode(word)
    url = base_url + word
    request = urllib2.Request(url, headers=headers)
    request.add_header("Connection", "keep-alive")
    response = urllib2.urlopen(request)
    data = response.read()

    tieba_restr = "<span class=\"card_infoNum\">([\s\S]*?)</span>"
    tieba_regex = re.compile(tieba_restr, re.IGNORECASE)
    tieba_mylist = tieba_regex.findall(data)
    tieba_numbers = eval(tieba_mylist[0].replace(",", ""))

    person_restr = "<span class=\"card_menNum\">([\s\S]*?)</span>"
    person_regex = re.compile(person_restr, re.IGNORECASE)
    person_mylist = person_regex.findall(data)
    person_numbers = eval(person_mylist[0].replace(",", ""))
    return tieba_numbers, person_numbers


print get_tieba_list_numbers("python")


def get_tieba_list(name):
    tiebalist = []
    return tiebalist


def get_url_list_from_page(url):
    url_list = []
    return url_list


def get_email_list_from_page(url):
    email_list = []
    return email_list

