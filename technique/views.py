import pdb
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from models import *
from forms import *
from django.http import HttpResponse

def list(request):
    techniques = Technique.objects.all()
    return render_to_response('technique/list.html', {'techniques': techniques}, RequestContext(request))

def view(request, pk):
    t = Technique.objects.get(pk=pk)
    return render_to_response('technique/view.html', {'t': t}, RequestContext(request))

@login_required
def create(request, pk=None):
    if pk:
        t = Technique.objects.get(pk=pk)
    else:
        t = Technique(created_by=request.user)
    if request.method == 'POST':
        f = TechniqueForm(request.POST, instance=t)
        if f.is_valid():
            t = f.save()
            return redirect(reverse('technique.views.view', args=(t.pk,)))
    else:
        f = TechniqueForm(instance=t)
    
    return render_to_response('technique/create.html', {'f': f}, RequestContext(request))
