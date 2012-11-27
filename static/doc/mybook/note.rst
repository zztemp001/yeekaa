===========
每日笔记
===========

上网任务
===========

#. 晚上到家：找到我的 **notebook** 文件，并入 *github*


工作笔记
========

#. 从两个表格选择一些不同的字段，存入一个新生成的表格中 ::

    >>> CREATE TABLE new_table_name AS SELECT old_table_01.somefields, old_table_02.somefields from old_table_01 join old_table_02 on old_table_01.ID = old_table_02.ID

#. 如果需要选择一个表格的所有字段，则可以是用通配符 ``table_name.*``

#. python三元赋值表达式用法 ::

    >>> value = 'True Value' if True else 'False Value'

#. ubuntu的磁盘管理命令 ::

    >>> fdisk /dev/xvdf  #给硬盘设备 xvdf 分区
    >>> mkfs.ext4 /dev/xvdf1  #给分好的分区xvdf1做格式化，格式为 ext4
    >>> mount /dev/xvdf1 /mnt/data  #将目录 /mnt/data 加载到 xvdf1 分区
    >>> mount  #不带参数的mount命令可以察看加载情况
    >>> vim /etc/fstab  #如果需要开机就加载数据到分区中，则可以修改 /etc/fstab 文件
    >>> df -h  #查看分区大小、使用情况

    
#. ubuntu下查看硬件信息的命令 ::

    >>> sudo lshw  #查看一般的硬件信息
    >>> sudo fdisk -l  #查看分区情况
    >>> df -h  #查看硬盘分区大小
    >>> du -h  #查看硬盘使用情况

#. 要使特定EC2实例能够连接到RDS实例，需要在RDS实例的 ``Security Group`` 设定 ``CIDR`` 规则和所需使用的 ``Security Group``

#. 通过以下命令连接到RDS实例，重要的参数是 ``RDS_Endpoint`` 和 ``Master_Name`` ，都可以在console中得到 ::

    >>> mysql -h RDS_Endpoint -P 3306 -u Master_Name -p

#. EC2产生的 ``key-pair.pem`` 如果是通过putty访问，需要用putty自带的 ``puttygen.exe`` 来转换为 ``key-pair.ppk`` 格式

#. 通过python在后台异步执行命令行 ::
    
    >>> from subprocess import Popen, PIPE
    >>> proc = Popen('command string', shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    >>> proc.pid  #进程的pid
    >>> proc.poll()  #如果进程执行完毕，则返回一个0/1代码，否则为空
    >>> proc.stdin.write('something\n')  #如果程序尚未执行完，可向进程发送输入内容，换行符是'\n'（universal_newlines参数）
    >>> a, b = proc.communicate()  #得到进程的输出内容，其中a是进程的屏幕输出，b是出错信息（这个函数会block主进程）
    >>> a = proc.stdout.read()  #同上面的a功能，同样会block主进程
    >>> b = proc.stderr.read()  #同上面的b功能，同样会block主进程

#. sqlite3每一行的id可以通过记录的 ``rowid`` 获得

#. sqlite3通过在创建连接时加入 ``check_same_thread=False`` 支持多线程 ::

    >>> conn = sqlite3.connect('some.db', check_same_thread=False)

#. ubuntu下更改 ``/etc/vim/vimrc`` 文件，使支持中文 ::
    
    set encoding=utf-8
    set fileencodings=ucs-bom,utf-8,cp936
    set fileencoding=utf-8
    set termencoding=utf-8

#. 可以通过在 ``site-packages`` 目录中添加 ``*.pth`` 文件来讲路径自动添加到 ``sys.path`` 变量中，以便python可以找到
#. python文档注释方法可以参考：
    #. http://packages.python.org/an_example_pypi_project/sphinx.html#is-sweaty
    #. http://packages.python.org/an_example_pypi_project/pkgcode.html

#. django.form字段required=False时，表格可以是空的也可以提交数据。

#. django template 简介：
    #. 变量用 **{{ }}** 标识
    #. 过滤器用 **{{ value | default: "nothing" }}**
    #. 标签使用 **{% %}** 标识

#. 缺省情况下，django的模板系统打开自动转换html字符的功能，转换以下字符 ::

    < 转换为 &lt;
    > 转换为 &gt;
    '（单引号）转换为 &#39;
    "（双引号）转换为 &quot;
    & 转换为 &amp;

#. 使用 ``safe`` 过滤器关闭变量的自动转换 ::
    
    This will be escaped: {{ data }}
    This will not be escaped: {{ data | safe }}

#. 使用 ``autoescape`` 标签关闭或打开一个模板块的自动转换 ::
    
    {% autoescape off %}
        Hello {{ name }}
    {% endautoescape %}

#. python 几个随机数的用法::

    import random
    random.randit(1, 10)  #取得1到10之间的随机整数，包括10
    random.sample(xrange(10000), 20]  #从1～9999之间返回一个包含20个随机数的list
    random.shuffle(xrange(20))  #将一个列表随机打乱顺序

#. fabric参考文章：
    #. http://tzangms.com/programming/2486/
    #. http://docs.fabfile.org/en/1.4.3/installation.html
    #. http://docs.fabfile.org/en/1.4.3/tutorial.html

#. 从另外一个表获取数据来更新本表的数据时，使用子查询 ::

    // 如果本表的parent_name与continent表的title字段相同，则使用两表的code字段拼接后来更新本表的code字段
    update semi_continent \
        set code = (select continent.code from continent where semi_continent.parent_name = continent.title) || code \
        where exists (select * from continent where semi_continent.parent_name = continent.[title])

    // 步骤一：语句在本表中的第一条记录上，通过where exists语句，看是否存在本表的parent_name字段和continent的title字段相等
    // 步骤二：如果相等，则通过第一个select子查询来得到continent表该条记录的code字段值，拼接，更新本表的code字段
    // 重复以上两个步骤，完成本表所有记录的更新

#. 将一个表中的数据插入到一个新表中 ::

    insert into new_table (col1,col2,col3) select col1,col2,col3 from old_table where ...
    //数据列之间不要留空格

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
