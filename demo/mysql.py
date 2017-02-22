#coding=utf-8
# Created by feizi at 2017/2/9

# 引入开发包
import pymysql.cursors

# 获取数据库链接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='wikiurl',
                             charset='utf8mb4')
