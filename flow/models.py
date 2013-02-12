from technique.models import *
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
# Create your models here.

class Flow(TimeStampedModel):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    positions = models.ManyToManyField(Position)
    submissions = models.ManyToManyField(Submission, blank=True)
    positional_improvements = models.ManyToManyField(PositionalImprovement, blank=True)
