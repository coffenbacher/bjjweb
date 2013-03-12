from django.forms import ModelForm
from django.forms.models import modelformset_factory
from models import *

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        exclude = ('youtube_id','created_by')

class TechniqueImageForm(ModelForm):
    class Meta:
        model = TechniqueImage
        exclude = ('technique','created_by', 'crop_from', 'effect')

TechniqueImageFormset = modelformset_factory(TechniqueImage, TechniqueImageForm)
