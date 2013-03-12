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
    
    image_formset = TechniqueImageFormset(queryset = t.images.all())
    if request.method == 'POST':
        f = TechniqueForm(request.POST, instance=t)
        image_formset = TechniqueImageFormset(request.POST, request.FILES)
        if f.is_valid() and image_formset.is_valid():
            t = f.save()

            for form in image_formset:
                image = form.save(commit=False)
                image.created_by = request.user
                image.technique = t
                image.save()
                
            return redirect(reverse('technique.views.view', args=(t.pk,)))
    else:
        f = TechniqueForm(instance=t)
    
    return render_to_response('technique/create.html', {'f': f, 'image_formset': image_formset}, RequestContext(request))
