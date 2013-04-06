import random
from operator import attrgetter
from technique.models import *
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
# Create your models here.

class Flow(TimeStampedModel):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    techniques = models.ManyToManyField(Technique, blank=True)

    def get_nodes(self):
        nodes = []
        
        for p in self.techniques.all():
            nodes.append({
                'color': p.type.color,
                'url': p.get_absolute_url(),
                'text': p.name,
                'name': p.pk,
                'pk': p.pk,
                'group': p.get_group_id(),
                'group_depth': p.get_group_depth(),
                'x': random.randint(0,100),
                'y': random.randint(0,100),
            })
        nodes = sorted(nodes, key=lambda k: k['group_depth'])
        return nodes
    
    def get_absolute_url(self):
        return reverse('flow.views.view', args=(self.pk,))
    
    def __unicode__(self):
        return self.name
