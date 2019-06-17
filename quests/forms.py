from django import forms
from .choices import *
from .models import QuestPin, QuestResult

class QuestSubmissionForm(forms.ModelForm):
    name = forms.CharField()
    rank = forms.ChoiceField(
        choices=RANK_CHOICES, 
    )
    roles = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ROLE_CHOICES
    )
    team_size = forms.ChoiceField(
        choices=TEAM_SZ_CHOICES,
    )
    duration = forms.DurationField()

    class Meta:
        model = QuestPin
        fields = ('name', )

class QuestResultSubmissionForm(forms.ModelForm):
    quest_item = QuestPin
    deliverables = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=DELIVERABLES_CHOICES,
    )

    class Meta:
        model = QuestResult
        fields = ('deliverables', )