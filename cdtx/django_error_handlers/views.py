from django.template import RequestContext
from django.shortcuts import render
from django.http import *
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.
def handler400(request):
    context = RequestContext(request, {
                            'error_number': '400',
                            'image_path': static('images/bad_request_brian.jpg'),
                        })
    return HttpResponseBadRequest(render(request, 'error_xxx.html', context_instance=context))

def handler403(request):
    context = RequestContext(request, {
                            'error_number': '403',
                            'image_path': static('images/less_privileges.jpg'),
                        })
    return HttpResponseForbidden(render(request, 'error_xxx.html', context_instance=context))

def handler404(request):
    context = RequestContext(request, {
                            'error_number': '404',
                            'image_path': static('images/confused_travolta.gif'),
                        })
    return HttpResponseBadRequest(render(request, 'error_xxx.html', context_instance=context))

def handler500(request):
    context = RequestContext(request, {
                            'error_number': '500',
                            'image_path': static('images/server_error.jpg'),
                        })
    return HttpResponseServerError(render(request, 'error_xxx.html', context_instance=context))

