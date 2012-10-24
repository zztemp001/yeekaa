# coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from django.template import RequestContext
from baseinfo.models import Place
from baseinfo.forms import NewPlaceForm
from django.core.mail import send_mail

def default(request):
    greeting = u'欢迎进入基础信息管理页面。'
    return render_to_response('baseinfo_default.html', locals())

def place(request):
    """
    @ param request
    """
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid():
            pdata = form.cleaned_data
            try:  # 检测数据是否重复，名称相同，父节点相同
                Place.objects.get(title__exact=pdata['title'], parent__exact=pdata['parent'])
            except Place.DoesNotExist:  #如果不存在，就正常添加
                info = u'新位置：' + pdata['title']
                try:
                    pr=Place.objects.get(pk=int(pdata['parent']))
                    p = Place(
                        title=pdata['title'],
                        level=int(pdata['level']),
                        parent=pr
                    )
                    p.save()
                    # todo: 根据需要进行缓存更新
                except:
                    info = u'存储数据时发生错误'
            else:
                info = u'已存在：' + pdata['title']
        else:
            info = u'数据校验不正确'
        return  render_to_response('info.html', {'info': info})
    else:
        places = Place.objects.all()[300:400]
        form = NewPlaceForm()
    return render_to_response('baseinfo_place.html', {'form': form, 'places': places}, context_instance=RequestContext(request))

def get_parent_info(request):
    def_set = [1, 8, 10, 16, 21, 23, 26]
    #todo:通过用户上一次提交的数据作为依据得到缺省值列表
    if request.is_ajax():
        if request.method == 'POST':
            level = int(request.POST['level'])
            options = {}
            for lv in range(1, level):
                places = Place.objects.filter(level__exact=lv)
                result = u''
                for p in places:
                    if p.id in def_set:
                        result += u'<option value="%d" selected=selected>%s</option>' % (p.id, p.title)
                    else:
                        result += u'<option value="%d">%s</option>' % (p.id, p.title)
                options[lv] = result
            mimetype = 'application/javascript'
            options = simplejson.dumps(options)
            return HttpResponse(options, mimetype)
    else:
        return HttpResponse(status=400)

def get_next_parent(request):
    if request.is_ajax():
        if request.method == 'POST':
            parent = int(request.POST['parent'])
            level = int(request.POST['level']) + 1
            places = Place.objects.filter(level__exact=level, parent__exact=parent)
            result = u''
            for p in places:
                result += u'<option value="%d">%s</option>' % (p.id, p.title)
            return HttpResponse(result)
    else:
        return HttpResponse(status=400)