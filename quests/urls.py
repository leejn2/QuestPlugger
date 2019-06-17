# quests/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.quest_form, name='quest_form')
]