from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from models import *

class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        exclude = ('youtube_id','created_by')

class TechniqueImageForm(ModelForm):

    def __init__(self, *arg, **kwarg):
        super(TechniqueImageForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = True

    class Meta:
        model = TechniqueImage
        exclude = ('technique','created_by', 'crop_from', 'effect')

TechniqueImageFormset = inlineformset_factory(Technique, TechniqueImage, TechniqueImageForm, extra=1)
