# Create your views here.
# coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from coupon.forms import ContactForm

def index(request):
    greeting = 'This is coupon greeting, 中文 ziti'
    return render_to_response('coupon_home.html', locals())

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #greeting = '感谢你提交了表格'
            return render_to_response('coupon_home.html', {'greeting':request.POST['message']})
    else:
        form = ContactForm(initial={'subject':'填写主题', 'email':'zhao@gmail.com', 'message':'有什么好的优惠券？'})
    return render_to_response('coupon_contact.html', {'form':form}, context_instance=RequestContext(request))