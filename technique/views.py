import pdb
from django.db.models import Count
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from models import *
from forms import *
from django.http import HttpResponse

def list(request):
    techniques = Technique.objects.annotate(num_images = Count('images')).order_by('-num_images')
    return render_to_response('technique/list.html', {'techniques': techniques}, RequestContext(request))

def view(request, pk):
    t = Technique.objects.get(pk=pk)
    related = filter(lambda x: x, [t2 for t2 in t.starting_at.all()] + [t2 for t2 in t.ending_at.all()] + [t2 for t2 in t.children.all()] + [ t.start, t.end ])
    return render_to_response('technique/view.html', {'t': t, 'related': related}, RequestContext(request))

@login_required
def create(request, pk=None):
    if pk:
        t = Technique.objects.get(pk=pk)
    else:
        t = Technique(created_by=request.user)
    
    if request.method == 'POST':
        f = TechniqueForm(request.POST, instance=t)
        image_formset = TechniqueImageFormset(request.POST, request.FILES, instance = t)
        
        if f.is_valid():
            t = f.save(commit=False)
            image_formset = TechniqueImageFormset(request.POST, request.FILES, instance = t)
            
            if image_formset.is_valid():
                t.save()

                for i in image_formset.save(commit=False):
                    i.created_by = request.user
                    i.technique = t
                    i.save()
                
                return redirect(reverse('technique.views.view', args=(t.pk,)))
    else:
        f = TechniqueForm(instance=t)
        image_formset = TechniqueImageFormset(instance = t)
    
    return render_to_response('technique/create.html', {'f': f, 'image_formset': image_formset}, RequestContext(request))
