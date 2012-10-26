#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from django.template import RequestContext
from django.core.mail import send_mail
from django.db.models import Q

from zzlib.ui import pager

from baseinfo.models import Place
from baseinfo.forms import SearchPlaceForm

def default(request):
    return render_to_response('baseinfo_base.html')

def place_list(request):
    #todo: 修复缺陷：关键字为空时，提交无反应
    #todo: 修复缺陷：表单中的页码数字不能自动回复为1
    #初始化默认的查询数据
    keyword = '' #无关键字
    level = 0  #全部
    page = 1
    per_page = 20
    order = 'level' #默认按层级排序

    #获取、处理用户提交的查询数据
    if request.method == 'POST':
        form = SearchPlaceForm(request.POST)
        if form.is_valid():
            fdata = form.cleaned_data
            keyword = fdata['keyword']
            level = int(fdata['level'])
            page = int(fdata['page'])
            per_page = int(fdata['per_page'])
            order = fdata['order']
        else:
            render_to_response('baseinfo_base.html')
    else:
        form = SearchPlaceForm()

    #生成查询条件
    Q1 = Q2 = Q()
    if len(keyword) > 0:
        Q1 = Q(title__contains=keyword)
    if level > 0:
        Q2 = Q(level__exact=level)

    total = Place.objects.filter(Q1, Q2).count()
    start = (page - 1) * per_page
    places = Place.objects.filter(Q1, Q2).order_by(order)[start : start + per_page]

    #返回结果
    return render_to_response('baseinfo_place_list.html', {
        'places': places,
        'form': form,
        'keyword': keyword,
        'level': level,
        'pager': pager(page, total, per_page, 9),
    })

def place_add(request):
    return

def place_city_list_alph(request):
    return

def place_city_list_zone(request):
    return

def place_country_list(request):
    return

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