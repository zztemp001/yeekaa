# encoding=utf-8

BOT_NAME = 'chrome'
BOT_VERSION = '21.0'

SPIDER_MODULES = ['river.spiders']
NEWSPIDER_MODULE = 'river.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'river.middlewares.ProxyMiddleware': 100,
}

ITEM_PIPELINES = [
    # 'river.pipelines.DBPipeline',
]

# 使用Proxy：第一步，在settings文件中定义代理列表
PROXIES = [
    '112.25.12.36:80',
    '220.195.192.172:80',
    '58.53.192.218:8123',
    '122.72.80.99:80',
    '122.72.80.105:80',
    '203.66.187.252:80',
    '218.247.129.3:80',
    '112.25.12.38:80',
    '202.142.17.120:80',
    '61.55.141.10:80',
    '122.72.80.106:80',
    '122.72.80.107:80',
    '112.25.12.39:80',
    '112.25.12.37:80',
    '122.72.80.100:80',
    '121.33.249.170:8080',
]
"""
PROXIES = [
        {'ip_port': 'xx.xx.xx.xx:xxxx', 'user_pass': 'foo:bar'},
        {'ip_port': 'PROXY2_IP:PORT_NUMBER', 'user_pass': 'username:password'},
        {'ip_port': 'PROXY3_IP:PORT_NUMBER', 'user_pass': ''},
]
"""

LOG_ENABLED = False
LOG_ENCODING = 'utf-8'
LOG_FILE = './log/local.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False  #是否将屏幕显示的信息一并log进文件，缺省为False
