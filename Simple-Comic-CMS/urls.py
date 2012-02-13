from django.conf.urls.defaults import patterns, include, url
from settings import DEBUG, MEDIA_ROOT, STATIC_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comicms.views.lastcomic', name="last"),
    url(r'^(\d+)/$', 'comicms.views.particularcomic', name="particular"),
    url(r'^random/$', 'comicms.views.randomcomic', name="random"),
    url(r'^(\d+)/previous/$', 'comicms.views.previouscomic', name="previous"),
    url(r'^(\d+)/next/$', 'comicms.views.nextcomic', name="next"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,}),
        url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT + '/admin/',}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,})
                            )