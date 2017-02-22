#coding=utf-8
# Created by feizi at 2017/2/9

import re
from urllib import request

def getHtmlContent(url):
    #打开url地址
    page = request.urlopen(url)
    #读取页面内容
    html = page.read()
    return html

def getImg(html):
    #查看页面源码，对应的正则表达式
    reg = r'src="(.*?\.jpg)" border'

    #对正则表达式进行编译，加快速度
    imgre = re.compile(reg)

    #查找所有匹配结果
    imgList = re.findall(imgre, html)

    x = 0
    for imgurl in imgList:
        #下载到本地，并进行重命名
        request.urlretrieve(imgurl, 'F:\spider\%s.jpg' %x)
        x += 1

html = getHtmlContent("http://tieba.baidu.com/p/445154390")
getImg(html)