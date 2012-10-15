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

# 抓取本地的place项
class LocalPlaceSpider(BaseSpider):
    name = 'localplace'
    allowed_domains = ['localhost', '127.0.0.1']
    start_urls = ['http://127.0.0.1/baseinfo/place/',]
    filename = 'river\\data\\data.sqlite'

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        places = hxs.select('//tbody/tr')

        self.conn = sqlite3.connect(self.filename)

        for place in places:
            item = PlaceItem()
            item['title'] = place.select('td[2]/text()')[0].extract()
            if place.select('td[3]/text()').extract():
                item['parent'] = place.select('td[3]/text()')[0].extract()
            else:
                item['parent'] = ''
            item['level'] = place.select('td[4]/text()')[0].extract()
            self.conn.execute('insert into place values (?,?,?,?)', (item['title'], item['parent'], int(item['level']), time()))

        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

        return item