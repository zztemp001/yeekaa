# coding=utf-8

import pickle
import time

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

from scrapy import log

from river.items import KpOriginItem, KpShopItem

class LocalCrawlSpider(CrawlSpider):
    name = 'place'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1/baseinfo/place/',]

    rules = (
        # Rule(SgmlLinkExtractor(allow=('OpenSSL\.html')), follow=True),
        Rule(SgmlLinkExtractor(allow=('offset=')), callback= 'parse_item'),
    )

    def parse_item(self, response):
        self.log('URL: %s' % response.url)

        item = KpOriginItem()

        # 将网页存入数据库
        item['url'] = unicode(response.url)
        item['body'] = response.body
        item['timestamp'] = unicode(time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time())))

        return item
