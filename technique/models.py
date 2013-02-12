from django_extensions.db.fields import UUIDField
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes import generic
from media.models import *

# Create your models here.
class Technique(TimeStampedModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=200)
    level = models.ForeignKey("Level", default=1)
    description = models.TextField(null=True, blank=True)
    images = generic.GenericRelation(Image)
    uuid = UUIDField(auto=True) 

    @classmethod
    def get_technique_or_none(cls, uuid):
        try:
            return ('Submission', Submission.objects.get(uuid=uuid))
        except:
            pass
        try:
            return ('PositionalImprovement', PositionalImprovement.objects.get(uuid=uuid))
        except:
            pass
        try:
            return ('Position', Position.objects.get(uuid=uuid))
        except:
            pass
        return None    


    def get_uuid(self):
        return unicode(self.uuid)
    def display_image(self):
        if self.images.exists():
            return self.images.all()[0]

    def __unicode__(self):
        return self.name

class Position(Technique):
    color = "brown"

class Submission(Technique):
    color = "red"
    start = models.ForeignKey(Position, related_name="start_submission")

class SubmissionType(TimeStampedModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("SubmissionType", null=True, blank=True)
    def __unicode__(self):
        return self.name

class PositionalImprovement(Technique):
    color = "green"
    type = models.ForeignKey("PositionalImprovementType")
    start = models.ForeignKey(Position, related_name="start")
    end = models.ForeignKey(Position, related_name="end")

class PositionalImprovementType(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Level(TimeStampedModel):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("pk",)

    def __unicode__(self):
        return self.name
