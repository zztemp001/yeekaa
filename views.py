__author__ = 'zhaowm'

import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def home(request):
    greeting = 'New Hello World'
    return render_to_response('home.html',locals())

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Current Time is: %s .</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset = 0):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    # assert False
    html = "<html><body> %s hour(s) later is %s .</body></html>" % (offset, dt)
    return HttpResponse(html)
