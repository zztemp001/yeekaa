#coding=utf-8

import re
import sqlite3
import urllib, urllib2
import time
import socket

from libxml2 import htmlParseDoc as htmlParser

class MyProxy():
    def __init__(self):
        socket.setdefaulttimeout(30)

    def get_sitedigger_proxy(self):
        url = 'http://www.site-digger.com/html/articles/20110516/proxieslist.html'
        xpath = '//*[@id="content_detail"]/div[3]/p[3]/textarea'

        try:
            html = urllib2.urlopen(url).read()
            doc = htmlParser(html, 'utf-8')
            doc = htmlParser(html, 'utf-8')
            content = doc.xpathEval(xpath)[0].content
        except:
            pass

        proxies = []
        for ip_port in content.split('\n')[2:-2]:
            host = ip_port.split(':')[0]
            port = ip_port.split(':')[1]
            proxies.append((host, port))

        self.save_proxy(proxies)

    def save_proxy(self, proxies):
        conn = sqlite3.connect('proxy.db')
        conn.execute('create table if not exists proxy (host CHAR, port CHAR, proxy_type CHAR, user CHAR, password CHAR, checked BOOL, speed INT, catch_from CHAR, catch_time TIME)')
        if proxies:
            for host, port in proxies:
                conn.execute('insert into proxy (host, port, proxy_type) values (?,?,?)', (host, port, 'http'))
        conn.commit()
        conn.close()
        conn = None

    def verify_proxy(self):
        url = 'http://www.myip.cn'
        xpath = '/html/body/center/div[4]/font[1]/b'

        conn = sqlite3.connect('proxy.db')
        proxies = conn.execute('select host, port from proxy').fetchall()
        proxies = proxies[21:30]

        for host, port in proxies:
            proxy = {'http': 'http://' + host + ':' + port}
            print u'正在使用的代理：', host, port
            start_time = time.time()
            try:
                html = urllib.urlopen(url, proxies=proxy).read()
                doc = htmlParser(html, 'utf-8')
                content = doc.xpathEval(xpath)[0].content
                print u'原始数据：', content
                ip_there = content.split(' ')[1]
                print u'远程返回地址：', ip_there
            except Exception, e:
                print u'错误：', e
            time_used = time.time() - start_time
            print u'用时：', time_used

def _get_proxylist():
    urls = []
    urls.append('http://www.proxylists.net/http.txt')
    urls.append('http://www.proxylists.net/http_highanon.txt')

    matches=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{2,5})',html)

    ret=[]
    for match in matches:
        ip=match[0]
        port=match[1]
        type=-1
        area='--'
        ret.append([ip,port,type,area])
        if indebug:print '8',ip,port,type,area
    return ret

def get_proxy_list():
    ''' 获取代理列表
    @param: use_proxy 如果是True，则尝试从数据库中返回所有代理，如果是False，则直接返回False
    '''
    try:
        conn = sqlite3.connect('proxy.db')
        proxies = conn.execute('select proxy_type, host, port, user, password from proxy').fetchall()
        conn.close()
        conn = None
    except:
        return False

    return proxies

if __name__ == '__main__':
    job = MyProxy()
    job.verify_proxy()