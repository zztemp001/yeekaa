from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('yeekaa.dsource.views',
    url('^$', 'default'),
)