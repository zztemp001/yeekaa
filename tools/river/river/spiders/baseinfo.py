# coding=utf-8

import pickle
import time
import sqlite3
from os import path
from time import time

from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy import log

from river.items import PlaceItem

# 抓取大洲/洲片区/国家
# 目标网址：http://baike.baidu.com/view/4262975.htm
class WorldPlaceSpider(BaseSpider):
    name = 'worldplace'
    allowed_domains = ['localhost', '127.0.0.1']
    start_urls = ['http://127.0.0.1/static/page/4262975.htm',]
    filename = 'river\\data\\basic.sqlite'


    def parse(self, response):
        item = PlaceItem()
        hxs = HtmlXPathSelector(response)
        self.conn = sqlite3.connect(self.filename)
        self.conn.text_factory = 'utf-8'

        # 获取大洲名称列表
        continents = []
        cs = hxs.select('//*[@id="lemmaContent-0"]/h2')[2:]  # 有用的数据从第3条开始，依次为非洲、美洲、亚洲、欧洲、大洋洲
        for c in cs:
            continents.append(c.select('span[2]/text()').extract()[0])

        # 获取并处理洲片区和国家数据
        # 主要的数据在以下表格中，有用的数据为2～6，依次为非洲、美洲、亚洲、欧洲、大洋洲
        data = hxs.select('//*[@id="lemmaContent-0"]/table')[1:]
        rows = data.select('tr')
        for row in rows:
            # 获取洲片区信息并存入数据库
            if len(row.select('td[1]/a/text()').extract()) > 0:
                semi_continent = row.select('td[1]/a/text()').extract()[0]
                url = row.select('td[1]/a/@href').extract()[0]
            else:
                semi_continent = row.select('td[1]/text()').extract()[0]
                url = ''
            self.conn.execute('insert into semi_continent (title, level, url) values (?,?,?)', (semi_continent, 2, url))

            # 获取国家信息并存入数据库，一些信息有错、漏，需要手动调整
            cs = row.select('td[2]/a')
            for c in cs:
                country = c.select('text()').extract()[0]  # 国家名称
                url = c.select('@href').extract()[0]  # 国家所引用的url
                self.conn.execute('insert into country (title, level, parent_title, url) values (?,?,?,?)', (country, 3, semi_continent, url))

        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

        return item