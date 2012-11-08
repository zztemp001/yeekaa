#coding=utf-8

import re
import sqlite3
import urllib2
from bs4 import BeautifulSoup

from download import get_page_basic

def init_db():
    conn = sqlite3.connect('proxy.db')
    conn.execute('create table if not exists proxy (host CHAR, port CHAR, type CHAR, user CHAR, password CHAR)')
    return conn

def get_cnproxy_proxy():
    ''' 数据源:http://www.cnproxy.com/proxy1.html(proxy1.html到proxy10.html共10页)
    更新频率:几天一次
    访问速度:比较快
    代理数:>1000
    这个网站的端口信息不是明文,替换下文本就可以得到端口信息了
    '''
    global g_proxies

    for i in range(1,11):
        url = 'http://www.cnproxy.com/proxy%d.html' % i
        soup = BeautifulSoup(get_html(url))

        for table in soup.find_all('table')[2:]:
            for tr in table.find_all('tr')[1:]:
                tds = tr.find_all('td')
                if len(tds) >= 2 and len(tds[0]) > 0 and len(tds[1]) > 0:
                    if tds[1].text == 'HTTP':
                        data = tds[0].text.encode('mbcs')
                        data = data.replace("document.write(","")
                        data = data.replace("\"","")
                        data = data.replace(")","")

                        data = data.replace("+l","9")
                        data = data.replace("+r","8")
                        data = data.replace("+i","7")
                        data = data.replace("+w","6")
                        data = data.replace("+b","5")
                        data = data.replace("+m","4")
                        data = data.replace("+z","3")
                        data = data.replace("+k","2")
                        data = data.replace("+c","1")
                        data = data.replace("+d","0")

                        proxy = {}
                        proxy['url'] = data
                        proxy['time'] = 0

                        if not (proxy in g_proxies):
                            g_proxies.append(proxy)

def get_51proxied_proxy():
    ''' 数据源:无忧代理
    http://www.51proxied.com/http_fast.html
    http://www.51proxied.com/http_anonymous.html
    http://www.51proxied.com/http_non_anonymous.html
    更新频率:一天多次
    访问速度:较慢
    代理数:>2000
    '''
    urls = list()
    urls.append('http://www.51proxied.com/http_fast.html')
    urls.append('http://www.51proxied.com/http_anonymous.html')
    urls.append('http://www.51proxied.com/http_non_anonymous.html')

    for url in urls:
        html = get_html(url)
        if len(html) == 0:
            continue
        soup = BeautifulSoup(html)
        for div in soup.find_all('div')[9:10]:
            for tr in div.find_all('tr')[1:]:
                tds = tr.find_all('td')
                if len(tds) >= 3 and len(tds[1]) > 0 and len(tds[2]) > 0:
                    proxy_url = '%s:%s' % (tds[1].text.encode('utf8'),tds[2].text.encode('utf8'))
                    add_proxy(proxy_url)

def get_01kk_proxy():
    ''' 数据源:http://www.01kk.net/daili/
    更新频率:几天一次
    访问速度:比较快
    代理数:<90
    '''
    global g_proxies
    soup = BeautifulSoup(get_html('http://www.01kk.net/daili/'))

    for table in soup.find_all('table'):
        for tr in table.find_all('tr')[1:]:
            tds = tr.find_all('td')
            if len(tds) >= 2 and len(tds[0]) > 0 and len(tds[0]) > 0:
                proxy = {}
                proxy['url'] = '%s:%s' % (tds[0].text.encode('mbcs'),tds[1].text.encode('mbcs'))
                proxy['time'] = 0

                if not (proxy in g_proxies):
                    g_proxies.append(proxy)

def  get_proxylists_proxy():
    ''' 数据源: http://www.proxylists.net/cn_0.html 0到38,可以更多
    访问速度:非常慢,因为页数太多了
    代理数:<400 (有一半以上的代理跟之前几个代理页面内容重复)
    '''
    for i in range(0,39):
        url = 'http://www.proxylists.net/cn_%d.html' % i
        soup = BeautifulSoup(get_html(url))
        for table in soup.find_all('table')[1:2]:
            for tr in table.find_all('tr')[2:]:
                tds = tr.find_all('td')
                if len(tds) >= 2:
                    script = tds[0].find_all('script')
                    if len(script) > 0:
                        proxy_url = '%s:%s' % (urllib.unquote(script[0].text[84:-13]),tds[1].text)
                        add_proxy(proxy_url)

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
        rows = conn.execute('select host, port, type from proxy').fetchall()
        proxies = []
        for host, port, proxy_type in rows:
            proxies.append({'host': host + ':' + port, 'type': proxy_type})
        conn.close()
        conn = None
    except:
        return False

    return proxies