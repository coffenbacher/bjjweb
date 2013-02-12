# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('bjjprofile/index.html')

def show(request, name):
    return render_to_response('profile.html', {})

