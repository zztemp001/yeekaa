#coding=utf-8

from django import forms

class SearchPlaceForm(forms.Form):
    LEVEL_CHOICES = (
        ('0', u'全部'),
        ('1', u'大洲'),
        ('2', u'洲片区'),
        ('3', u'国家'),
        ('4', u'国家区域'),
        ('5', u'省/州/直辖市'),
        ('6', u'城市'),
        ('7', u'县/城区'),
        ('8', u'县镇/街道')
    )
    ORDER_CHOICES = (
        ('level', u'按层级排序'),
        ('title', u'按地理名称排序'),
    )
    level = forms.ChoiceField(choices=LEVEL_CHOICES, label=u'级别')
    order = forms.ChoiceField(choices=ORDER_CHOICES, label=u'筛选')
    keyword = forms.CharField(max_length=60, label=u'关键字', required=False)
    page = forms.CharField(initial='1', widget=forms.HiddenInput)
    per_page = forms.CharField(initial='15', widget=forms.HiddenInput)