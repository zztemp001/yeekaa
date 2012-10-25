# coding=utf-8
__author__ = 'zhaowm'

from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('yeekaa.baseinfo.views',
    url('^$', 'default'),
    url('^place/list/$', 'place_list'),
    url('^place/list/(?P<page>\d+)/$', 'place_list'),
    url('^place/list/(?P<page>\d+)/(?P<pagecount>\d+)/$', 'place_list'),
    url('^place/add/$', 'place_add'),
    url('^place/map/alph/$', 'place_city_list_alph'),
    url('^place/map/zone/$', 'place_city_list_zone'),
    url('^place/country/list/$', 'place_country_list'),
    url('^getparent/$', 'get_parent_info'),
    url('^getnextparent/$', 'get_next_parent'),
)