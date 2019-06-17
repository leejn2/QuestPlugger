# quests/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .models import QuestPin, QuestResult
from .forms import QuestSubmissionForm, QuestResultSubmissionForm
# Create your views here.

def index(request):
    quest_pin_list = QuestPin.objects.order_by('-id')
    template = loader.get_template('quests/index.html')
    context = {
        'quest_pin_list': quest_pin_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, questpin_id):
    try:
        quest_pin = QuestPin.objects.get(pk=questpin_id)
        quest_result = QuestResult.objects.get(questpin_id=questpin_id)
        context = {
            'quest_pin': quest_pin,
            'quest_result': quest_result,
        }
    except QuestPin.DoesNotExist:
        raise Http404("Quest does not exist")
    return render(request, 'quests/detail.html', context)

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
            quest_result.questpin = quest
            quest_result.deliverables = result_form.cleaned_data['deliverables']
            quest_result.save()
            messages.info(request, 'Your quest has been sent successfully!')
            return HttpResponseRedirect('/quests')
    return render(request, "quests/questform.html", {'quest_form': quest_form, 'result_form': result_form})