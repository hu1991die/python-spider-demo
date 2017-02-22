#coding=utf-8
# Created by feizi at 2017/2/9

from urllib import request

resp = request.urlopen("http://www.baidu.com")

print (resp.read().decode("utf-8"))