#coding=utf-8
# Created by feizi at 2017/2/9

from urllib import request

req = request.Request("http://www.baidu.com")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")
resp = request.urlopen(req)

print(resp.read().decode("utf-8"))
