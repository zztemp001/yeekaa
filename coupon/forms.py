# coding=utf-8
__author__ = 'zhaowm'

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='主题：')
    email = forms.EmailField(required=False, label='邮箱：')
    message = forms.CharField(widget=forms.Textarea, label='内容')