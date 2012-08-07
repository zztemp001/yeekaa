# coding=utf-8

from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=30)  #地点名称
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=u'上级地点', related_name='childpoint')  #链表
    level = models.IntegerField(verbose_name=u'层级')
    hot = models.NullBooleanField(default=False, null=True, blank=True)  #标记是否热门
    extra = models.CharField(max_length=16, default=u'0000000000000000', null=True, blank=True)  #存储额外信息

    def __unicode__(self):
        return self.title