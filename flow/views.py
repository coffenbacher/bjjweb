# Create your views here.
from django.core import serializers
from django.http import HttpResponse
import json
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import *
from forms import *

def list(request):
    flows = Flow.objects.all()
    return render_to_response('flow/list.html', {'flows': flows}, RequestContext(request))

def view(request, id):
    f = Flow.objects.get(id=id)
    return render_to_response('flow/view.html', {'flow': f}, RequestContext(request))

def render(request, id):
    f = Flow.objects.get(id=id)
    nodes = f.get_nodes()
    links = []
    for t in f.techniques.all():
        if t.start:
            links.append({'source': t.start.pk, 'target': t.pk})

    res = json.dumps({"nodes": nodes, "links": links})
    return HttpResponse(res)

def create(request, id=None):
    flow = Flow.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = FlowForm(request.POST, instance=flow)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            form.save_m2m()
            return redirect('/flow/%s/' % f.id)
    else:        
        if id:
            form = FlowForm(instance=Flow.objects.get(id=id))
        else:
            form = FlowForm()

    return render_to_response('flow/create.html', {'form': form}, RequestContext(request))
