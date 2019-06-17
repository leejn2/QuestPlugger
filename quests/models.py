from django.db import models
from multiselectfield import MultiSelectField
from .choices import *
# Create your models here.

class QuestPin(models.Model):
    name = models.CharField(max_length=75)
    rank = models.CharField(
        max_length=1,
        choices=RANK_CHOICES,
        default=F_RANK,
    )
    roles = MultiSelectField(
        choices=ROLE_CHOICES,
    )
    team_size = models.CharField(
        max_length=12,
        choices=TEAM_SZ_CHOICES,
        default=TEAM_SZ_SOLO,
    )
    duration = models.DurationField()

    def __str__(self):
        return self.name


class QuestResult(models.Model):
    questpin = models.ForeignKey(QuestPin, on_delete=models.CASCADE)
    deliverables = MultiSelectField(
        choices=DELIVERABLES_CHOICES,
    )

    def __str__(self):
        return self.questpin.__str__() + ' (Quest Results)'