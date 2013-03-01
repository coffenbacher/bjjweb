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
    for p in f.positions.all():
        for s in p.start_submission.filter(id__in=f.submissions.values_list("id", flat=True)):
            links.append({"source": p.get_uuid(), "target": s.get_uuid(), "value": 1})
        for pi in p.start.filter(id__in=f.positional_improvements.values_list("id", flat=True)):
            links.append({"source": p.get_uuid(), "target": pi.get_uuid(), "value": 1})
        for pi in p.end.filter(id__in=f.positional_improvements.values_list("id", flat=True)):
            links.append({"target": p.get_uuid(), "source": pi.get_uuid(), "value": 1})

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

    valid_subs = {}
    valid_pis = {}
    for p in Position.objects.all():
        valid_subs[p.pk] = [dict({'from': p.name}, **i) for i in p.start_submission.values('id', 'name')] 
        valid_pis[p.pk] = [dict({'from': p.name}, **i) for i in p.start.values("id", "name")]

    return render_to_response('flow/create.html', {'form': form, 'valid_pis': json.dumps(valid_pis), 'valid_subs': json.dumps(valid_subs)}, RequestContext(request))
