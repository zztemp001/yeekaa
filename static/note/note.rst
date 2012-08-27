===========
每日笔记
===========

上网任务
===========

#. 下载reg文件恢复输入法设置界面
#. 将变形金刚的连接发给老婆
#. bootstrap

   #. 打开相关网页
   #. 下载开发包
   #. 下载中英文文档
#. 晚上到家：找到我的 **notebook** 文件，并入 *github*

.. note::

  | 打开scrapy相关网页
  | 打开asana、gantter
  | 非常好
  | 上面来一行
  | 再来一行
  | 打开github issue list
  | vim 中文手册（cheatsheet）
  | google 日历、文档的离线编辑
  | 看看todolist有没有更新

工作笔记
========

在Scrapy项目中使用代理
----------------------
#. 在项目的配置文件中加入代理列表（数组） ::

    PROXIES = [
        {'ip_port': 'xx.xx.xx.xx:xxxx', 'user_pass': 'foo:bar'},
        {'ip_port': 'PROXY2_IP:PORT_NUMBER', 'user_pass': 'username:password'},
        {'ip_port': 'PROXY3_IP:PORT_NUMBER', 'user_pass': ''},
    ]
#. 在项目根目录中添加 ``middlewares.py`` ，添加以下内容： ::

    import base64
    import random
    from settings import PROXIES

    class ProxyMiddleware(object):
        def process_request(self, request, spider):
            proxy = random.choice(PROXIES)
            if proxy['user_pass'] is not None:
                request.meta['proxy'] = "http://%s" % proxy['ip_port']
                encoded_user_pass = base64.encodestring(proxy['user_pass'])
                request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            else:
                request.meta['proxy'] = "http://%s" % proxy['ip_port']

#. 在项目配置文件 ``settings.py`` 中添加以下内容： ::

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        'project_name.middlewares.ProxyMiddleware': 100,
    }

#. 代理的测试，增加一个用于测试的 **Spider** ，代码如下： ::

    from scrapy.spider import BaseSpider
    from scrapy.contrib.spiders import CrawlSpider, Rule
    from scrapy.http import Request

    class TestSpider(CrawlSpider):
        name = "test"
        domain_name = "whatismyip.com"
        # The following url is subject to change, you can get the last updated one from here :
        # http://www.whatismyip.com/faq/automation.asp
        start_urls = ["http://automation.whatismyip.com/n09230945.asp"]

        def parse(self, response):
            open('test.html', 'wb').write(response.body)

#. 参考文档：
    * http://mahmoud.abdel-fattah.net/2012/04/07/using-scrapy-with-proxies/
    * http://mahmoud.abdel-fattah.net/2012/04/16/using-scrapy-with-different-many-proxies/
    * `代理资源1 <http://proxymesh.com/pricing/>`_
    * `代理资源2 <http://squidproxies.com>`_

处理静态文件的步骤（使用开发服务器时）
-----------------------------------------------------------

#. django缺省会在项目根目录，以及每个app的static目录下找静态文件
#. settings.py - 在INSTALLED_APPS中加入django.contrib.staticfiles
#. urls.py ::

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
#. 模板中可以使用绝对路径来引用静态文件，或通过{{ STATIC_URL }}，后者需要确保在views中使用了RequestContext

github 使用技巧
------------------------------------------
#. 打开git shell的颜色高亮 ::

    >>> git config --global color.ui "auto"

#. 打开git的图形界面（自带的） ::

    >>> git gui

其他
===========

#. 源代码高亮示例 ::

    def say_hello():
        print 'aldslfjfdsa'

    def asdlfj():
        print 'ok'

#. 引用示例 ::

    Finished: An initial directory structure has been created.

    You should now populate your master file .\source\index.rst and create other documentation
    source files. Use the sphinx-build command to build the docs, like so:
       sphinx-build -b builder .\source .\build
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

#. note & warning

  .. note::
    Finished: An initial directory structure has been created.

  .. warning::
    Finished: An initial directory structure has been created.

#. 链接

* http://docutils.sourceforge.net/rst.html
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* `参考图 <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_
* 去看看 `今天任务`_

  这是一个inline：``from django import *``

#. 引用python文档内容

  我喜欢 :mod:`doctest` 模块，里面有一个 :class:`models.Place` 的类，这是一个函数 :func:`baseinfo.views.get_parent_info`
