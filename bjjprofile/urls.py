from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', 'bjjprofile.views.index'),
    url(r'^(?P<name>.*)/$', 'bjjprofile.views.show'),
)

