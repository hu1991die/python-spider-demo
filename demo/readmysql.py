#coding=utf-8
# Created by feizi at 2017/2/9

# 导入开发包
import pymysql.cursors

# 获取数据库链接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='wikiurl',
                             charset='utf8mb4')

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 定义SQL语句查询
        sql = "select `id`, `urlname`, `urlhref` from `urls` where `id` is not null"

        # 获取总记录数
        count = cursor.execute(sql)
        print(count)

        # 查询所有数据
        # result = cursor.fetchall()
        # print(result)

        #查询指定条数的数据
        result = cursor.fetchmany(size=20)
        print(result)
finally:
    # 关闭数据库链接
    connection.close()
