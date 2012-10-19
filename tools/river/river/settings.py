# encoding=utf-8

BOT_NAME = 'chrome'
BOT_VERSION = '21.0'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ROBOTSTXT_OBEY = False  # 是否遵守网站的robots.txt文件规则
DNSCACHE_ENABLED = True  # 开启DNS缓存
DEFAULT_RESPONSE_ENCODING = 'utf-8'  # 当文件中没有编码时使用的编码类型，仅用于TextResponse对象

DEPTH_LIMIT = 4  # 爬行深度
DOWNLOAD_DELAY = 1.25  # 下载间隔时间，以秒为单位，如果此项设置为0，则不会有任何间隔
RANDOMIZE_DOWNLOAD_DELAY = True  # 与DOWNLOAD_DELAY共同作用，实际值为DOWNLOAD_DELAY*(0.5~1.5)
DOWNLOAD_TIMEOUT = 180  # 下载超时设定，以秒为单位

CONCURRENT_ITEMS = 100  # 使用pipeline同时处理的item数量
CONCURRENT_REQUESTS = 16  # 最大下载线程数
CONCURRENT_REQUESTS_PER_DOMAIN = 8  # 针对单一域名启动的线程数
CONCURRENT_REQUESTS_PER_IP = 0  # 针对单一IP启动的线程数，如果为0，则使用域名数，如果非0，则覆盖域名设置

SPIDER_MODULES = ['river.spiders']
NEWSPIDER_MODULE = 'river.spiders'

# 缺省的Http请求头信息
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'river.middlewares.ProxyMiddleware': 100,
}

ITEM_PIPELINES = [
    # 'river.pipelines.DBPipeline',
]

# log服务设置
LOG_ENABLED = False
LOG_ENCODING = 'utf-8'
LOG_FILE = 'river\\log\\local.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False  #是否将屏幕显示的信息一并log进文件，缺省为False。如果为True，则屏幕不再显示信息

# 信息记录设置
STATS_ENABLED = True
STATS_DUMP = True  # 在log文件中记录stat信息
DOWNLOADER_STATS = True
DEPTH_STATS = True  # 是否收集爬行深度信息
DEPTH_STATS_VERBOSE = False  # 是否记录每一深度的request数量