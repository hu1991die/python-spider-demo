#coding=utf-8
# Created by feizi at 2017/2/10

from urllib.request import urlopen

html = urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode('utf-8'))


