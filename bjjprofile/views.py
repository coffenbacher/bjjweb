# Create your views here.
from django.shortcuts import render_to_response

def show(request, name):
    return render_to_response('profile.html', {})

