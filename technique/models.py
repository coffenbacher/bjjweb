import pdb
from photologue.models import ImageModel
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

class TechniqueImage(ImageModel):
    technique = models.ForeignKey("Technique", related_name='images')
    created_by = models.ForeignKey(User)

class Technique(TimeStampedModel):
    name = models.CharField(max_length=200)
    level = models.ForeignKey("Level", default=1)
    type = models.ForeignKey("TechniqueType")
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey("Technique", null=True, blank=True, related_name='children')
    start = models.ForeignKey("Technique", null=True, blank=True, related_name='starting_at')
    end = models.ForeignKey("Technique", null=True, blank=True, related_name='ending_at')
    youtube_id = models.CharField(max_length=30, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_start = models.PositiveIntegerField(null=True, blank=True, verbose_name="At second", default=0)
    created_by = models.ForeignKey(User)
    
    objects = models.Manager()
    sweeps = SweepManager()
    positions = PositionManager()
    submissions = SubmissionManager()

    class Meta:
        ordering = ['type__id', 'start__name', 'name']
        
    def get_group_depth(self):
        if self.parent:
            return 1 + self.parent.get_group_depth()
        if self.start:
            return 1 + self.start.get_group_depth()
        else:
            return 1 

    def get_group_id(self):
        if self.parent:
            return self.parent.get_group_id()
        if self.start:
            return self.start.get_group_id()
        else:
            return self.pk


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
        try:
            if self.type.name == 'Position':
                return 'Position: %s' % (self.name)
            if self.type.name == 'Submission':
                return 'Sub: %s > %s' % (self.start.name, self.name)
            if self.type.name == 'Sweep':
                return 'Sweep: %s > %s' % (self.start.name, self.name)
            if self.type.name == 'Pass':
                return 'Pass: %s > %s' % (self.start.name, self.name)
            if self.type.name == 'Transition':
                return 'Transition: %s > %s' % (self.start.name, self.name)
            if self.type.name == 'Counter':
                return 'Counter: %s > %s' % (self.start.name, self.name)
            return self.name
        except:
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
