from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item

from scrapy import log

from river.items import LocalItem

class LocalCrawlSpider(CrawlSpider):
    name = 'local_crawl'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:7464/',]

    rules = (
        Rule(SgmlLinkExtractor(allow=('OpenSSL\.html')), follow=True),
        Rule(SgmlLinkExtractor(allow=('rand', 'versi')), callback= 'parse_item'),
    )

    def parse_item(self, response):
        self.log('Hello: %s' % response.url)
        item = Item()
        return item
