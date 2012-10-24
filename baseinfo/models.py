# coding=utf-8

from django.db import models
from config import PLACE_LEVEL_CODE as PLC

class PlaceManager(models.Manager):
    def get_city(self, place_id):
        ''' 给出一个地点，获取所在城市
        @params: place_id  要查询的地点
        @returns: 如果要查询的地点有所属城市，则返回城市；如果本身是城市，或者比城市更高级，则直接返回None
        '''
        p = self.get(id = place_id)
        if p.level <= 6:
            return None
        if p.level == 7:
            return p.parent
        if p.level == 8:
            return p.parent.parent

    def get_province(self, place_id):
        ''' 给出一个地点，获取所在省份
        @params: place_id  要查询的地点
        @returns: 如果要查询的地点有所属省份，则返回省份；如果本身就是省级，或者比省级更高级，则直接返回None
        '''
        p = self.get(id = place_id)
        if p.level <= 5:
            return None
        else:
            return self.get(path = p.path.split('C')[0])

    def get_full_path(self, place_id):
        ''' 给出一个地点，获取其所在的全部路径
        @params: place_id  要查询的地点
        @returns: 返回一个路径list，每个节点是包含“title”、“level”、“id”的dict
        '''
        path = []
        p = self.get(id = place_id)
        for i in range(p.level):
            node = {}
            spliter = PLC[i+1][1]
            path_id = p.path.split(spliter)[0]
            place = self.get(path = path_id)
            node['title'] = place.title
            node['level'] = place.level
            node['id'] = place.id
            path.append(node)
        return path


class Place(models.Model):
    title = models.CharField(max_length=50)  #地点名称
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name=u'上级地点', related_name='childpoint')  #链表
    level = models.IntegerField(verbose_name=u'层级')  #标记地点的所在层级，在config.py中定义
    parent_title = models.CharField(max_length=50, null=True)  #以及地点的名称，仅用于检验
    path = models.CharField(max_length=50)  #地点所在的路径
    pinyin = models.CharField(max_length=100, null=True)  #地点的拼音/英文名
    zimu = models.CharField(max_length=20, null=True)  #地名首个字母缩写/英文名缩写，用于快速输入查找
    id_code = models.CharField(max_length=10, null=True)  #身份证的前六位代码，用于初步验证身份信息
    hot = models.NullBooleanField(default=False, null=True, blank=True)  #标记是否热门
    have_scene = models.NullBooleanField(default=False, null=True, blank=True)  #标记该地点是否拥有景点
    extra = models.CharField(max_length=16, default=u'0000000000000000', null=True, blank=True)  #存储额外信息

    objects = PlaceManager()

    def __unicode__(self):
        return self.title