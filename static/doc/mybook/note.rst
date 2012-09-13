===========
每日笔记
===========

上网任务
===========

#. 晚上到家：找到我的 **notebook** 文件，并入 *github*


工作笔记
========

#. 可以通过在 ``site-packages`` 目录中添加 ``*.pth`` 文件来讲路径自动添加到 ``sys.path`` 变量中，以便python可以找到
#. python文档注释方法可以参考：
    #. http://packages.python.org/an_example_pypi_project/sphinx.html#is-sweaty
    #. http://packages.python.org/an_example_pypi_project/pkgcode.html

#. fabric参考文章：
    #. http://tzangms.com/programming/2486/
    #. http://docs.fabfile.org/en/1.4.3/installation.html
    #. http://docs.fabfile.org/en/1.4.3/tutorial.html

#. python中文拼音排序：
    #. http://www.pythonclub.org/python-basic/chinese-sort
    #. http://gerry.lamost.org/blog/?p=338

#. 对字典的排序，最终都要归结为对字典的键/值列表的排序 ::

    def sortedDictValues(adict,reverse=False):
    	keys = adict.keys()
    	keys.sort(reverse=reverse)
    	return [adict[key] for key in keys]

#. 对列表的排序，优先使用内置的 ``list.sort()`` 方法 ::

    >>> a = [1,9,3,7,2,0,5]
    >>> a.sort()
    >>> print a
    [0, 1, 2, 3, 5, 7, 9]
    >>> a.sort(reverse=True)
    >>> print a
    [9, 7, 5, 3, 2, 1, 0]
    >>> b = ['e','a','be','ad','dab','dbc']
    >>> b.sort()
    >>> print b
    ['a', 'ad', 'be', 'dab', 'dbc', 'e']

#. jquery1.4版本以后，ajax.post函数需要指定返回数据的类型 ::

    $.post("test.php", {name: "Jone", time: "2pm" },
        function(data) {
            process(data);
        },
        "json"
    );

south的安装和使用
-----------------

#. 使用pip或easy_install均可安装 ::
    
    >>> easy_install South  # 初始化安装
    
    >>> easy_install -U South  # 升级

#. 在 ``settings.py`` 的 ``INSTALLED_APPS`` 中添加 ``'south'``

#. 运行 ``manage.py syncdb`` 生成South所需的跟踪表，否则会产生 ``south_migrationhistory does not exist.`` 的错误
    
#. 编辑好app的model后，实施初次跟踪（south是按app来跟踪的） ::

    >>> manage.py schemamigration southtut --initial  # 对于新的app进行初次跟踪

    >>> manage.py convert_to_south <app_name>  # 对于已存在的app进行初次跟踪，后续即可使用south

    # 以上命令将在southtut目录下生成一个migrations目录，用于后续的变更跟踪，对于没有这个目录的app，south将忽略
    
#. 实施migration，south将生成新的表，和 ``manage.py syncdb`` 做的工作一样 ::

    >>> manage.py migrate southtut

#. 对model进行修改后，用以下命令执行migration ::
    
    >>> manage.py schemamigration southtut --auto  # 找出app的变更

    >>> manage.py migrate southtut  # 执行变更

#. 恢复app的model到任一记录点 ::

    >>> manage.py migrate <app_name> 0016

  .. note ::

    * 1～3步是基础的、必须的
    * 对于 null = False 但又没有提供缺省值的列，south 会提示提供缺省值
    * 对于 unique = True 的列，south 会自动检测并完成变更
    * 对于 ManyToMany 字段，south 会自动检测并添加或删除相关表格
    * 参考文章：http://tzangms.com/programming/2484/


sqlite3的字符串编码问题
-----------------------

#. 在使用sqlite3的时候，提示了这样的错误信息： ::

    ErrorCode: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). 
    It is highly recommended that you instead just switch your application to Unicode strings.

#. 使用 ``conn.text_factory`` 来解决： ::
  
    import sqlite3
    self.conn = sqlite3.connect(datafile)
    self.conn.text_factory = 'utf-8'  # 这是关键，取值可以是utf-8/str等
    # sqlite3的blob字段是编码透明的，存进去什么，取出来就是什么，可以用来存储文件、大段文字、html页面数据等

.. note::

    参考文件：http://python.6.n6.nabble.com/CPyUG-sqlite3-td2828909.html

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
    * 去看看 `上网任务`_

    这是一个inline：``from django import *``

#. 引用python文档内容

    我喜欢 :mod:`doctest` 模块，里面有一个 :class:`models.Place` 的类，这是一个函数 :func:`baseinfo.views.get_parent_info`
