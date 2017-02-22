#coding=utf-8
# Created by feizi at 2017/2/9

import re
from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story <a>Hello</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, "html.parser")
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.get_text())
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id="link2").get_text())
# print(soup.get_text())
# print('\n\n\n\n')
# print(soup.find('p', {"class":"story"}))
#
# print('\n')
# for link in soup.findAll('a'):
#     print(link.get('href'))
#     print(link.string)

# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
#
# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)

data = soup.find_all('a', href=re.compile(r"^http://example\.com/"))
print(data)
