# coding=utf-8
__author__ = 'zhaowm'

from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('yeekaa.baseinfo.views',
    url('^$', 'default'),
    url('^place/$', 'place'),
    url('^testajax/$', 'test_ajax'),
    url('^testjson/$', 'test_json'),
    url('^getparent/$', 'get_parent_info'),
    url('^getnextparent/$', 'get_next_parent'),
)