# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    users = User.objects.all()
    return render_to_response('bjjprofile/list.html', {'users': users}, RequestContext(request))

def show(request, name):
    return render_to_response('profile.html', {}, RequestContext(request))

