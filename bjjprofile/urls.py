from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<name>.*)/$', 'bjjprofile.views.show'),
)

