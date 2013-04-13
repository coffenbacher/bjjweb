from django.db import models
from technique.models import Technique
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Competitor(TimeStampedModel):
    name = models.CharField(max_length=256)
    
class MatchStyle(TimeStampedModel):
    name = models.CharField(max_length=256)

class MatchType(TimeStampedModel):
    name = models.CharField(max_length=256)

class Match(TimeStampedModel):
    name = models.CharField(max_length=256)
    youtube_id = models.CharField(max_length=256)
    youtube_link = models.CharField(max_length=256)
    competitor_1 = models.ForeignKey(Competitor, related_name='c1s')
    competitor_2 = models.ForeignKey(Competitor, related_name='c2s')
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

class TechniqueAppearance(TimeStampedModel):
    technique = models.ForeignKey(Technique)
    match = models.ForeignKey(Match)
    second = models.PositiveIntegerField(verbose_name="At second")
    successful = models.BooleanField(default=True)
