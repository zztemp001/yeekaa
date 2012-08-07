# coding=utf-8
__author__ = 'zhaowm'

from django import forms

class NewPlaceForm(forms.Form):
    LEVEL_CHOICES = (
        ('', u'请选择'),
        ('2', u'国家'),
        ('3', u'区域'),
        ('4', u'省'),
        ('5', u'城市'),
        ('6', u'城区'),
        ('7', u'商圈'),
        ('8', u'地标')
    )
    level = forms.ChoiceField(choices=LEVEL_CHOICES, label='类型')
    title = forms.CharField(max_length=60, label='新地点')
    parent = forms.CharField(widget=forms.HiddenInput, initial="")