from django.template import RequestContext
from django.shortcuts import render
from django.http import *
from django.conf.urls.static import static

uniqueTemplate = 'django_error_handlers/error_xxx.html'

# Create your views here.
def handler400(request, *args, **kwargs):
    context = {
        'error_number': '400',
        'image_path': static('images/bad_request_brian.jpg'),
    }
    response = render(request, uniqueTemplate, context)
    response.status_code = 400
    return response

def handler403(request, *args, **kwargs):
    context = {
        'error_number': '403',
        'image_path': static('images/less_privileges.jpg'),
    }
    response = render(request, uniqueTemplate, context)
    response.status_code = 403
    return response

def handler404(request, *args, **kwargs):
    context = {
        'error_number': '404',
        'image_path': static('images/confused_travolta.gif'),
    }
    response = render(request, uniqueTemplate, context)
    response.status_code = 404
    return response

def handler500(request, *args, **kwargs):
    context = {
        'error_number': '500',
        'image_path': static('images/server_error.jpg'),
    }
    response = render(request, uniqueTemplate, context)
    response.status_code = 500
    return response

