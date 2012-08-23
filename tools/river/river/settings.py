# encoding=utf-8

BOT_NAME = 'river'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['river.spiders']
NEWSPIDER_MODULE = 'river.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# 使用Proxy：第一步，在settings文件中定义代理列表
PROXIES = [
        {'ip_port': 'xx.xx.xx.xx:xxxx', 'user_pass': 'foo:bar'},
        {'ip_port': 'PROXY2_IP:PORT_NUMBER', 'user_pass': 'username:password'},
        {'ip_port': 'PROXY3_IP:PORT_NUMBER', 'user_pass': ''},
    ]

