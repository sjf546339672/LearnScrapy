# encoding:utf-8
import re

mystr = """<div class="rt">
                共3424条职位
            </div>"""
restr = """<div class="rt">
                共(\\d+)条职位
            </div>"""  # 正则表达式，（）只要括号内的数据
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(mystr)
print(mylist)
print(mylist[0])
