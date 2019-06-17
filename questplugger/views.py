# questplugger/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from quests.models import QuestPin
# Create your views here.

#def index(request):
#    url_list = ['contact/', 'quests/']
#    template = loader.get_template('index.html')
#    context = {
#        'url_list': url_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
    quest_pin_list = QuestPin.objects.order_by('-id')[:10]
    template = loader.get_template('index.html')
    context = {
        'quest_pin_list': quest_pin_list,
    }
    return HttpResponse(template.render(context, request))