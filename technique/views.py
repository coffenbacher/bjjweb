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
    p = True if request.method == 'POST' else False

    if uuid:
        submission_form = None
        position_form = None
        p_improvement_form = None

        t = Technique.get_technique_or_none(uuid)
        if t[0] == 'Submission':
            submission_form = SubmissionForm(instance = t[1]) if not p else SubmissionForm(request.POST, instance=t[1])
            formset = ImagesFormSet(instance=t[1])
        elif t[0] == 'Position':
            position_form = PositionForm(instance = t[1]) if not p else PositionalImprovementForm(request.POST, instance = t[1])
            formset = ImagesFormSet(instance=t[1])
        elif t[0] == 'PositionalImprovement':
            p_improvement_form = PositionalImprovementForm(instance = t[1]) if not p else PositionalImprovementForm(request.POST, instance=t[1])
            formset = ImagesFormSet(instance=t[1])
    elif p:
        submission_form = SubmissionForm(request.POST)
        position_form = PositionForm(request.POST)
        p_improvement_form = PositionalImprovementForm(request.POST)
    else:
        submission_form = SubmissionForm()
        position_form = PositionForm()
        p_improvement_form = PositionalImprovementForm()
        formset = ImagesFormSet()


    if p:
        if request.POST['tech-type'] == 'submission':
            if submission_form.is_valid():
                s = submission_form.save()
                formset = ImagesFormSet(request.POST, request.FILES, instance=s)
                for form in formset:
                    if form.is_valid():
                        f = form.save(commit=False)
                        f.submitter = request.user
                        f.technique = s
                        f.category = MediaCategory.objects.get(name='Display')
                        if f.image:
                            f.save()
                return redirect('/technique/')
        if request.POST['tech-type'] == 'position':
            if position_form.is_valid():
                p = position_form.save()
                formset = ImagesFormSet(request.POST, instance=p)
                return redirect('/technique/')
        if request.POST['tech-type'] == 'p-improvement':
            if p_improvement_form.is_valid():
                pi = p_improvement_form.save()
                formset = ImagesFormSet(request.POST, instance=pi)
                return redirect('/technique/')

    return render_to_response('technique/create.html', 
        {'submission_form': submission_form,
        'position_form': position_form,
        'p_improvement_form': p_improvement_form,
        'images_formset': formset,
        }, RequestContext(request))
