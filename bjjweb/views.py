from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('bjjprofile.views.show', args=(request.user.username,)))
    return render_to_response('home.html', {}, RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, RequestContext(request))
