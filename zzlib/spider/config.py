#coding=utf-8

#默认的请求文件头
HEADERS = [
    ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'),
    ('X-Forwarded-For', '192.168.0.1'),  #预防对方网站透过代理得到本机IP
]

#是否缓存DNS查询结果，如果是，则将域名第一次查询到的ip置换掉请求网址的相应部分
CACHE_DNS = True
