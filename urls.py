# coding=utf-8

from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'yeekaa.views.home'),
    url(r'^coupon/', include('yeekaa.coupon.urls')),
    url(r'^dsource/', include('yeekaa.dsource.urls')),
    url(r'^baseinfo/', include('yeekaa.baseinfo.urls')),
)

urlpatterns += patterns('yeekaa.views',
    # Examples:
    # url(r'^$', 'yeekaa.views.home', name='home'),
    # url(r'^yeekaa/', include('yeekaa.foo.urls')),
    url(r"^time/$", 'current_datetime'),
    url(r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )