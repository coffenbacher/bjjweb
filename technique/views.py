import pdb
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from models import *
from media.forms import *
from forms import *
from django.http import HttpResponse

def list(request):
    techniques = [s for s in Submission.objects.all()] + [p for p in Position.objects.all()] + [pi for pi in PositionalImprovement.objects.all()]
    return render_to_response('technique/list.html', {'techniques': techniques}, RequestContext(request))

def view(request, uuid):
    t = Technique.get_technique_or_none(uuid)[1]
    return render_to_response('technique/view.html', {'t': t}, RequestContext(request))

@login_required
def create(request, uuid=None):
    t = Technique.get_technique_or_none(uuid)
    d = {}
    if request.method == 'POST':
        if not t:
            t = Technique()
        d['f'] = t.handle_forms(request)
        if isinstance(d['f'], Technique):
            return redirect(reverse('technique.views.view', args=(d['f'].uuid,)))
        
    elif t:    
        d['f'] = t[1].get_forms(request)
    else:    
        d['s_form'] = SubmissionForm()
        d['p_form'] = PositionForm()
        d['pi_form'] = PositionalImprovementForm()
    
    return render_to_response('technique/create.html',
        d, RequestContext(request))
