from django.contrib import admin

# Register your models here.

from .models import QuestPin, QuestResult

admin.site.register(QuestPin)
admin.site.register(QuestResult)