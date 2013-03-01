from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.forms import ModelForm
from models import *
from technique.models import *

class ImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ('submitter')
        include = ('image')

ImagesFormSet = generic_inlineformset_factory(Image, exclude=['submitter', 'category'], can_delete=False)

class VideoForm(ModelForm):
    class Meta:
        model = Video

VideosFormSet = generic_inlineformset_factory(Video, exclude=['submitter', 'youtube_id', 'category'], extra=1, can_delete=False)
