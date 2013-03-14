from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bjjweb.views.home', name='home'),
    url(r'^about/$', 'bjjweb.views.about', name='about'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    (r'^users/', include('bjjprofile.urls')),
    (r'^technique/', include('technique.urls')),
    (r'^flow/', include('flow.urls')),
    # url(r'^bjjweb/', include('bjjweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^photologue/', include('photologue.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#FIX THIS NEED SOMETHING BETTER FOR TESTS
if 'StaticFilesStorage' in settings.STATICFILES_STORAGE:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
