import pdb
from helpers import video_id
from django_extensions.db.fields import UUIDField
from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.contenttypes import generic

# Create your models here.
class Technique(TimeStampedModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=200)
    level = models.ForeignKey("Level", default=1)
    description = models.TextField(null=True, blank=True)
    uuid = UUIDField(auto=True) 
    youtube_id = models.CharField(max_length=30, null=True, blank=True)
    youtube_link = models.CharField(max_length=200, null=True, blank=True)
    youtube_start = models.PositiveIntegerField(null=True, blank=True)

    def parse_youtube_id(self):
        self.youtube_id = video_id(self.youtube_link)
        return True
    
    def save(self, *args, **kwargs):
        if self.pk is None and self.youtube_link:
            self.parse_youtube_id()
        return super(Technique, self).save(*args, **kwargs)

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

    def get_forms(self, request):
        f = self.get_form()    
        return f

    def handle_forms(self, request):
        from forms import *
        if self.uuid:
            kwargs = {'instance': self}
        else:
            kwargs = {}
        if request.POST['tech-type'] == 'submission':
            f = SubmissionForm(request.POST, **kwargs)
        elif request.POST['tech-type'] == 'position':
            f = PositionForm(request.POST, **kwargs)
        elif request.POST['tech-type'] == 'p-improvement':
            f = PositionalImprovementForm(request.POST, **kwargs)

        if f.is_valid():
            t = f.save()
            return t
        
    def get_uuid(self):
        return unicode(self.uuid)

    def get_absolute_url(self):
        return reverse('technique.views.view', args=(self.get_uuid(),))

    def display_image(self):
        if self.images.exists():
            return self.images.all()[0]

    def __unicode__(self):
        return self.name

class Position(Technique):
    color = "brown"
    
    def get_form(self):
        from forms import *
        return PositionForm(instance=self)

class Submission(Technique):
    color = "red"
    start = models.ForeignKey(Position, related_name="start_submission")
    
    def get_form(self):
        from forms import *
        return SubmissionForm(instance=self)

class SubmissionType(TimeStampedModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("SubmissionType", null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class PositionalImprovement(Technique):
    color = "green"
    type = models.ForeignKey("PositionalImprovementType")
    start = models.ForeignKey(Position, related_name="start_pis")
    end = models.ForeignKey(Position, related_name="end_pis")
    
    def get_form(self):
        from forms import *
        return PositionalImprovement(instance=self)

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
