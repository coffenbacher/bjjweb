from django.forms.widgets import *
from django.forms import ModelForm
from models import *

class FlowForm(ModelForm):
    class Meta:
        model = Flow
        exclude = ('user',)
        widgets = {
            'techniques': CheckboxSelectMultiple(),
        }
