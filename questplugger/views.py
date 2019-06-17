# questplugger/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    url_list = ['contact/', 'quests/']
    template = loader.get_template('index.html')
    context = {
        'url_list': url_list,
    }
    return HttpResponse(template.render(context, request))