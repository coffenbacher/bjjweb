from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin
from django import forms
from models import *

class FlowAdmin(admin.ModelAdmin):
    filter_horizontal = ('techniques',)
    
admin.site.register(Flow, FlowAdmin)

