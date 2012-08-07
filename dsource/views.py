# Create your views here.
# coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from coupon.forms import ContactForm

def default(request):
    greeting = 'This is 信息源管理主页'
    return render_to_response('dsource_home.html', locals())
