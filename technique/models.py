import pdb
from helpers import video_id
from django_extensions.db.fields import UUIDField
from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

# Create your models here.
class PositionManager(models.Manager):
    def get_query_set(self):
        return super(PositionManager, self).get_query_set().filter(type__name='Position')
        
class SubmissionManager(models.Manager):
    def get_query_set(self):
        return super(SubmissionManager, self).get_query_set().filter(type__name='Submission')

class SweepManager(models.Manager):
    def get_query_set(self):
        return super(SweepManager, self).get_query_set().filter(type__name='Sweep')

class Technique(TimeStampedModel):
    name = models.CharField(max_length=200)
    level = models.ForeignKey("Level", default=1)
    type = models.ForeignKey("TechniqueType")
    description = models.TextField(null=True, blank=True)
    start = models.ForeignKey("Technique", null=True, blank=True, related_name='starting_at')
    end = models.ForeignKey("Technique", null=True, blank=True, related_name='ending_at')
    youtube_id = models.CharField(max_length=30, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_start = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.ForeignKey(User)
    
    objects = models.Manager()
    sweeps = SweepManager()
    positions = PositionManager()
    submissions = SubmissionManager()

    def parse_youtube_id(self):
        self.youtube_id = video_id(self.youtube_link)
        return True
    
    def save(self, *args, **kwargs):
        if self.youtube_link:
            self.parse_youtube_id()
        return super(Technique, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('technique.views.view', args=(self.pk,))

    def display_image(self):
        if self.images.exists():
            return self.images.all()[0]

    def __unicode__(self):
        return self.name

class TechniqueType(TimeStampedModel):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Level(TimeStampedModel):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("pk",)

    def __unicode__(self):
        return self.name
