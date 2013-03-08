from django.forms import ModelForm
from models import *

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        exclude = ('youtube_id','created_by')
