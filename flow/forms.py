from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import *
from django.forms import ModelForm
from models import *

class FlowForm(ModelForm):
    filter_horizontal = ('techniques',)
    
    class Meta:
        model = Flow
        exclude = ('user',)
        widgets = {
            'techniques': FilteredSelectMultiple("Techniques", is_stacked=False),
        }
    
    class Media:
        css = { 'all': ('/static/admin/css/widgets.css',), }
        js = ('/admin/jsi18n/',)
        
