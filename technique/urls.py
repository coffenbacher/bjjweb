from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^$', 'technique.views.list'),
    url(r'^create/$', 'technique.views.create'),
    url(r'^(?P<pk>[-\w]+)/$', 'technique.views.view'),
    url(r'^(?P<pk>[-\w]+)/edit/$', 'technique.views.create'),
)

