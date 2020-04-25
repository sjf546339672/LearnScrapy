# coding: utf-8

import lxml
import lxml.etree


html = lxml.etree.parse('index.html')
print lxml.etree.tostring(html)