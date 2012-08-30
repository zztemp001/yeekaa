from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from river.items import LocalItem

class LocalSpider(BaseSpider):
    name = 'local'
    allowed_domains = ['localhost', '127.0.0.1']
    start_urls = ['http://127.0.0.1/',]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        menus = hxs.select('//ul[@class="dropdown-menu"]/li')
        items = []
        for menu in menus:
            item = LocalItem()
            item['title'] = menu.select('a/text()').extract()
            item['link'] = menu.select('a/@href').extract()
            item['body'] = menu.select('a').extract()
            items.append(item)
        return items
