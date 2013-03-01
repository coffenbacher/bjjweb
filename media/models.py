from django.db import models 
from django_extensions.db.models import TimeStampedModel
from django.forms import ModelForm
from django.contrib.auth.models import User
from technique.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
    
class MediaCategory(TimeStampedModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class BasicMedia(TimeStampedModel):
    class Meta:
        abstract = True

    submitter = models.ForeignKey(User)
    category = models.ForeignKey("MediaCategory", default=1)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    technique = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "%s on %s" % (self.category, self.technique)


class Image(BasicMedia):
    image = models.ImageField(upload_to="m/resource-images")

class Video(BasicMedia):
    youtube_id = models.CharField(max_length=200, verbose_name="Youtube parsed id")
    youtube_url = models.CharField(max_length=200, verbose_name="Youtube link")
    start = models.IntegerField(default=0, verbose_name="Start time (s)")

