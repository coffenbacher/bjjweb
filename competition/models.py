from django.db import models
from technique.helpers import video_id
from technique.models import Technique
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Competitor(TimeStampedModel):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
        
class MatchStyle(TimeStampedModel):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name

class MatchType(TimeStampedModel):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name

class Match(TimeStampedModel):
    youtube_id = models.CharField(max_length=256)
    youtube_link = models.CharField(max_length=256)
    competitor_1 = models.ForeignKey(Competitor, related_name='c1s')
    competitor_2 = models.ForeignKey(Competitor, related_name='c2s')
    event_date = models.DateField(null=True, blank=True)
    event_name = models.CharField(max_length=256, null=True, blank=True)
    result = models.CharField(max_length=2,
        choices = (
            ('W1', 'Competitor 1 win'),
            ('W2', 'Competitor 2 win'),
            ('D', 'Draw'),
            ('NC', 'Non-competitive'),
            )
        )
    style = models.ForeignKey(MatchStyle)
    type = models.ForeignKey(MatchType)
    
    def parse_youtube_id(self):
        self.youtube_id = video_id(self.youtube_link)
        return True

    def save(self, *args, **kwargs):
        if self.youtube_link:
            self.parse_youtube_id()
        return super(Match, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s X %s' % (self.competitor_1, self.competitor_2)

class TechniqueAppearance(TimeStampedModel):
    technique = models.ForeignKey(Technique)
    match = models.ForeignKey(Match)
    competitor = models.ForeignKey(Competitor)
    second = models.PositiveIntegerField(verbose_name="At second")
    successful = models.BooleanField(default=True)
