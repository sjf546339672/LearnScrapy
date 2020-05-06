# coding: utf-8
import requests
import json

url = "http://httpbin.org/post"
data = {"hello": "world"}
testfile = {"file": open("test.txt", "r")}
r1 = requests.post(url, data=data)
print(r1.text)

print("===========================================")
r2 = requests.post(url, files=testfile)
print(r2.text)