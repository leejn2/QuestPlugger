# quests/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import QuestSubmissionForm, QuestResultSubmissionForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the quest index. There will be a quest list here in the future.")

def quest_form(request):
    if request.method == 'GET':
        quest_form = QuestSubmissionForm()
        result_form = QuestResultSubmissionForm()
    else:
        quest_form = QuestSubmissionForm(request.POST)
        result_form = QuestResultSubmissionForm(request.POST)
        if quest_form.is_valid() and result_form.is_valid():
            quest = quest_form.save(commit=False)
            quest_result = result_form.save(commit=False)
            quest.name = quest_form.cleaned_data['name']
            quest.rank = quest_form.cleaned_data['rank']
            quest.roles = quest_form.cleaned_data['roles']
            quest.team_size = quest_form.cleaned_data['team_size']
            quest.duration = quest_form.cleaned_data['duration']
            quest.save()
            print("---------------------------------- questpin_id = {}".format(quest.id))
            quest_result.questpin = quest
            quest_result.deliverables = result_form.cleaned_data['deliverables']
            quest_result.save()
            messages.info(request, 'Your quest has been sent successfully!')
            return HttpResponseRedirect('/quests/')
    return render(request, "questform.html", {'quest_form': quest_form, 'result_form': result_form})