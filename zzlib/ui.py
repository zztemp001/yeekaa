#coding=utf-8

def pager(page=1, records=0, per_page=20, list_count=5):
    ''' 根据当前页码、每页显示数、记录总数、显示的页码按钮数，返回一个分页器
    @params: page, 当前页码
    @params: records, 记录总数
    @params: per_page, 每页要显示的记录数量
    @list_page: 页码按钮数量，显示在“前一页”与“后一页”之间
    @returns: dict{'total':页码总数 , 'per_page':每页记录数, 'page':当前页 ,'prev':前一页 ,'next':后一页 , 'range': [显示的页码列表], }
    '''

    result = {}
    result['page'] = page
    result['per_page'] = per_page

    #计算页码总数，如果除不尽，则增加一页
    if records % per_page:
        result['total'] = records / per_page + 1
    else:
        result['total'] = records / per_page

    #“前一页”页码=当前页-1，但如果当前页是第1页，则“前一页”=1
    result['prev'] = page - 1
    if page <= 1: result['prev'] = 1

    #“后一页”页码=当前页+1，如果当前页是最后1页，则“后一页”=总页码
    result['next'] = page + 1
    if page >= result['total']: result['next'] = result['total']

    #计算页码列表
    #如果总页码少于list_count，则list_count=总页码
    if list_count > result['total']: list_count = result['total']
    #正常情况下，页码的起始页为list_count的一半+1，如list_count=9，则起始页为5
    prevs = nexts = list_count / 2
    start = page - prevs
    if page <= prevs + 1:
        start = 1
    if page > result['total'] - nexts:
        start = result['total'] - list_count + 1
    if start < 1: start = 1
    result['range'] = range(start, start + list_count)

    return result