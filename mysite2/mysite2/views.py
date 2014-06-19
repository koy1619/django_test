#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


#def display_meta(request):
#    values = request.META.items()
#    values.sort()
#    html = []
#    for k, v in values:
#        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def display_meta(request):
    values = request.META.items()
    values.sort()
    t=get_template('display_meta.html')
    html=t.render(Context({'values':values}))
    return HttpResponse(html)
