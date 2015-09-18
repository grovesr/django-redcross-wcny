from django.shortcuts import render, render_to_response
from django.template import RequestContext

def home(request):
    return render(request,'base/base.html',{'nav_home':1})

def redcross_help(request):
    return render(request,'base/redcross_help.html',{'nav_help':1})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

