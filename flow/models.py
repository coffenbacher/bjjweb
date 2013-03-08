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
    
    def techniques(self):
        ts = []
        ts += list(self.positions.all())
        ts += list(self.submissions.all())
        ts += list(self.positional_improvements.all())
        return ts
        
    def get_nodes(self):
        nodes = []
        
        for p in self.techniques():
            nodes.append({
                'color': p.color,
                'url': p.get_absolute_url(),
                'name': p.name,
                'uuid': p.uuid,
            })
        
        return nodes
    
    def get_absolute_url(self):
        return reverse('flow.views.view', args=(self.pk,))
    
    def __unicode__(self):
        return self.name
