from django.forms.widgets import *
from django.forms import ModelForm
from models import *

class FlowForm(ModelForm):
    class Meta:
        model = Flow
        exclude = ('user',)
        widgets = {
            'positions': CheckboxSelectMultiple(),
            'submissions': CheckboxSelectMultiple(),
            'positional_improvements': CheckboxSelectMultiple()
        }
