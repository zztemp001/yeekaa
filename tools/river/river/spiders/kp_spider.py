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
    name = 'kp_crawler'
    allowed_domains = ['site-digger.com']
    start_urls = ['http://db.site-digger.com/csv/6469616e70696e675f6265696a696e675f3230313230375f66697273745f32303030/',]

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
