from django.forms import ModelForm
from models import *

class PositionalImprovementForm(ModelForm):
    class Meta:
        model = PositionalImprovement

class PositionForm(ModelForm):
    class Meta:
        model = Position

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
