from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^$', 'technique.views.list'),
    url(r'^create/$', 'technique.views.create'),
    url(r'^(?P<uuid>[-\w]+)/$', 'technique.views.view'),
    url(r'^(?P<uuid>[-\w]+)/edit/$', 'technique.views.create'),
)

