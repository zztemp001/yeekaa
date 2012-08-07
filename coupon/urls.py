__author__ = 'zhaowm'

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('yeekaa.coupon.views',
    url('^$', 'index'),
    url('^contact/$', 'contact'),
)