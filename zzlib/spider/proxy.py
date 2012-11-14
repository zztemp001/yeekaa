#coding=utf-8

import re
import sqlite3
import urllib, urllib2
import time
import socket
from zzlib.common.system import Logger

from libxml2 import htmlParseDoc as htmlParser

class MyProxy():
    conn = sqlite3.connect('proxy.db')

    def __init__(self):
        socket.setdefaulttimeout(30)  #设置代理检验的超时时长
        self.logger = Logger('proxy.log')  #用于保存log信息的文件
        self.logger.p_log('程序开始运行...')

        #类实例化时，打开数据库并清空数据
        try:
            self.conn.execute('create table if not exists proxy (host CHAR, port CHAR, proxy_type CHAR, user CHAR, password CHAR, checked BOOL, speed INT, catch_from CHAR, catch_time TIME)')
            self.conn.execute('delete from proxy')
            self.conn.commit()
        except Exception, e:
            self.logger.p_log('打开数据库时出错，程序退出...')
            return False

    def __del__(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
        self.logger.p_log('程序已退出...')

    def get_proxy(self, speed=60):
        ''' 返回数据库的代理列表，格式为：[(host, port), ...]
        level是代理的级别，在代理验证时生成，取值范围（1，9），级别越高，速度越高
        函数返回响应速度（秒）小于speed的代理
        '''
        if type(speed) is not int: return False
        if speed > 9 or speed < 0: speed = 0
        try:
            proxies = self.conn.execute('select host, port from proxy where speed<=%d' % speed).fetchall()
        except:
            return False
        #格式已经是[(host, port), ...]
        return proxies

    def fetch_proxy(self):
        self.__fetch_sitedigger()
        #self.__fetch_proxylist()

    def verify_proxy(self):
        url = 'http://www.myip.cn'
        xpath = '/html/body/center/div[4]/font[1]/b'
        verified = []

        #获取需要检验的代理
        try:
            proxies = self.conn.execute('select distinct host, port from proxy').fetchall()
            self.logger.p_log('从数据库中获取到不重复的代理共 %d 个，准备逐个校验中' % len(proxies))
            proxies = proxies[:5]
        except Exception, e:
            self.logger.p_log('读取代理数据库错误，退出...')
            return False

        #检验代理，成功的保存在verified中
        for host, port in proxies:
            host = str(host)
            port = str(port)
            proxy = {'http': 'http://' + host + ':' + port}
            self.logger.p_log('正在检验代理：%s:%s' % (host, port))
            start_time = time.time()
            try:
                html = urllib.urlopen(url, proxies=proxy).read()
                doc = htmlParser(html, 'utf-8')
                content = doc.xpathEval(xpath)[0].content
                if content:
                    ip_there = content.split(' ')[1]
                    self.logger.p_log('检测到的代理：%s' % (ip_there))
                    if ip_there == host:
                        time_used = time.time() - start_time + 1
                        verified.append((host, port, int(time_used)))
                        self.logger.p_log('代理 %s:%s 检验通过，用时：%d 秒' % (host, port, time_used))
                    else:
                        self.logger.p_log('检测到的IP %s 与代理IP %s 不相符，准备检验下一个...' % (ip_there, host))
                        continue
                else:
                    self.logger.p_log('代理 %s:%s 未能正确返回信息，校验失败，准备检验下一个...' % (host, port))
            except Exception, e:
                self.logger.p_log('使用代理 %s:%s 打开目标网页时发生错误，准备检验下一个...' % (host, port))

        #保存校验成功的代理
        self.logger.p_log('共有 %d 个代理通过校验，正在准备更新数据库记录...' % len(verified))
        #conn.text_factory = 'str'
        for host, port, speed in verified:
            try:
                self.conn.execute('update proxy set speed=? where host=? and port=?', (speed, host, port))
                self.conn.commit()
                self.logger.p_log('代理 %s:%s [%d 秒] 校验成功，并已成功入库' % (host, port, speed))
            except Exception, e:
                self.logger.p_log('代理 %s:%s [%d 秒] 校验成功，但在数据库更新状态时发生异常' % (host, port, speed))

        #删除校验不成功的数据
        try:
            self.conn.execute('delete from proxy where speed is null')
            self.logger.p_log('未通过校验的代理已从数据库中删除')
        except Exception, e:
            self.logger.p_log('从数据库中删除未通过校验的代理时发生错误')


    def __fetch_sitedigger(self):
        url = 'http://www.site-digger.com/html/articles/20110516/proxieslist.html'
        xpath = '//*[@id="content_detail"]/div[3]/p[3]/textarea'

        try:
            html = urllib2.urlopen(url).read()
            doc = htmlParser(html, 'utf-8')
            doc = htmlParser(html, 'utf-8')
            content = doc.xpathEval(xpath)[0].content
            if not content: return False
            self.logger.p_log('成功代开网页，获取内容的长度为：%d 字节' % len(content))
        except:
            self.logger.p_log('打开目标网页 %s 获取内容时出错，退出中...' % (url))

        proxies = []
        for ip_port in content.split('\n')[2:-2]:
            try:
                proxy = (ip_port.split(':')[0], ip_port.split(':')[1])
            except Exception, e:
                self.logger.p_log('处理记录：%s 是发生错误' % ip_port)
            if proxy not in proxies:
                proxies.append(proxy)

        self.logger.p_log('成功获取 %d 个代理，正在准备存入数据库中...' % len(proxies))
        self.__save_proxy(proxies)

    def __fetch_proxylist(self):
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

    def __save_proxy(self, proxies):
        if proxies:
            for host, port in proxies:
                try:
                    row = self.conn.execute('select host from proxy where host=%s and port=%s' % (host, port)).fetchone()
                except:
                    row = None
                try:
                    if row:
                        self.logger.p_log('代理 %s:%s 已存在' % (host, port))
                        continue
                    else:
                        self.conn.execute(u'insert into proxy (host, port, proxy_type) values (?,?,?)', (host, port, 'http'))
                except Exception, e:
                    self.logger.p_log('代理 %s:%s 保存失败' % (host, port))
            self.conn.commit()  #记得及时提交

        self.logger.p_log('目标代理列表已入库，等待校验中...')


if __name__ == '__main__':
    job = MyProxy()
    job.fetch_proxy()
    job.verify_proxy()
    del job