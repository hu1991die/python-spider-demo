#coding=utf-8
# Created by feizi at 2017/2/9

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
    ("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("SearchDate", "2017/02/09"),
    ("SearchTime", "14:30"),
    ("SearchWay", "DepartureInMandarin")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))

print(resp.read().decode("utf-8"))