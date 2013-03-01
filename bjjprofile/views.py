# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('bjjprofile/index.html', {}, RequestContext(request))

def show(request, name):
    return render_to_response('profile.html', {}, RequestContext(request))

