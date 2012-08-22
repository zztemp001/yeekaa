# coding=utf-8

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'yeekaa.views.home'),
    url(r'^coupon/', include('yeekaa.coupon.urls')),
    url(r'^dsource/', include('yeekaa.dsource.urls')),
    url(r'^baseinfo/', include('yeekaa.baseinfo.urls')),
)

urlpatterns += patterns('yeekaa.views',
    url(r"^time/$", 'current_datetime'),
    url(r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
    )

urlpatterns += staticfiles_urlpatterns()