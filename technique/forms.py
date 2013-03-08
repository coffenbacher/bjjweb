from django.forms import ModelForm
from models import *

class PositionalImprovementForm(ModelForm):
    class Meta:
        model = PositionalImprovement
        exclude = ('youtube_id',)

class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ('youtube_id',)

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        exclude = ('youtube_id',)
