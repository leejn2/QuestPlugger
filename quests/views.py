# quests/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the quest index. There will be a quest list here in the future.")
