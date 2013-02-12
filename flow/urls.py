from django.conf.urls import patterns, url

urlpatterns = patterns('', 
    url(r'^$', 'flow.views.list'),
    url(r'^(?P<id>\d+)/$', 'flow.views.view'),
    url(r'^(?P<id>\d+)/render/$', 'flow.views.render'),
    url(r'^(?P<id>\d+)/edit/$', 'flow.views.create'),
    url(r'^create/$', 'flow.views.create')
)
