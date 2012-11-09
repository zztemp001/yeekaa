#coding=utf-8

import time, random
import urllib, urllib2, cookielib
from threading import Thread, Lock
from Queue import Queue
from config import *

class Fetcher:
    def __init__(self, threads, data=None):
        self.lock = Lock() #线程锁
        self.q_request = Queue() #任务队列
        self.q_response = Queue() #完成队列

        #创建opener，如果需要登录，也需要设置cookie
        if USE_COOKIE or NEED_LOGIN:
            cj = cookielib.CookieJar()
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler)
        else:
            self.opener = urllib2.build_opener(urllib2.HTTPHandler)

        #如果需要登录，则先登录
        if NEED_LOGIN:
            self.login()

        self.data = data
        self.threads = threads

        #生成线程池
        for i in range(threads):
            t = Thread(target = self.threaded_fetch)
            t.setDaemon(True)
            t.start()

        #线程开始运行设为1，结束设为0
        self.running = 0

    def __del__(self): #解构时需等待两个队列完成
        time.sleep(0.5)
        self.q_request.join()
        self.q_response.join()

    def is_running(self):
        ''' 只要请求序列、返回数据列、线程尚在运行，都可以从返回数据列中pop出数据
        '''
        return self.q_request.qsize() + self.q_response.qsize() + self.running

    def push(self, url):
        self.q_request.put(url)

    def pop(self):
        return self.q_response.get()

    def threaded_fetch(self):
        while True:
            url = self.q_request.get()
            with self.lock: #线程开始运行设为1
                self.running += 1

            response = self.handle_request(url, self.data, RETRY_NUM)

            self.q_response.put((url, response))
            with self.lock:
                self.running -= 1
            self.q_request.task_done()
            time.sleep(round(random.random() + 0.01, 2) * SLEEP_TIME_SEED)

    def login(self, retries=3):
        pass

    def handle_request(self, url, data=None, retries=3):
        request = urllib2.Request(url)
        #如果有需要提交的数据
        if type(data) is dict:
            request.add_data(urllib.urlencode(data))   #Request会自动将请求方式转为POST
        #如果需要用headers
        if USE_HEADER and HEADERS:
            for key, value in HEADERS:
                request.add_header(key, value)
        #如果需要使用代理

        response = ''
        try:
            response = urllib2.urlopen(request).read()
        except Exception, error_msg:
            print Exception, error_msg
            if retries > 0:
                self.handle_request(url, data, retries-1)
            else:
                print 'Request Failed: ', url
        return response

if __name__ == "__main__":
    urls = ['http://www.verycd.com/topics/%d/' % i for i in range(5420, 5430)]
    f = Fetcher(threads=10)
    for url in urls:
        f.push(url)
    while f.is_running():
        url,content = f.pop()
        print url,len(content)