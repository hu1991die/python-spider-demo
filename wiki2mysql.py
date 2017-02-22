#coding=utf-8
# Created by feizi at 2017/2/9

#引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

# 请求url，并对返回结果进行utf-8编码处理
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
# 使用beautifulSoup解析
soup = BeautifulSoup(resp, "html.parser")

# print(soup)
#获取所有以/wiki/打头的词条url链接
for url in soup.find_all("a", href=re.compile(r"^/wiki/")):
    # 输出url链接地址，剔除掉图片格式的数据
    if not re.search(r"\.(jpg|JPG|png|PNG|gif|GIF|jpeg|JPEG)$", url['href']):
        #输出词条文字和对应的链接
        urlname = url.get_text()
        urlhref = "https://en.wikipedia.org" + url['href']
        print(urlname, '<----------->', urlhref)

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='wikiurl',
                                     charset='utf8mb4')
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建一条SQL语句
                sql = "insert into `urls` (urlname, urlhref) values (%s, %s)"

                # 执行SQL语句
                cursor.execute(sql, (urlname, urlhref))

                #提交事务
                connection.commit()
        finally:
            connection.close()