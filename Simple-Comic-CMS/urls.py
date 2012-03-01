from django.conf.urls.defaults import *
from settings import DEBUG, MEDIA_ROOT, STATIC_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('comicms.urls')),
)

if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,}),
        url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT + '/admin/',}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,})
                            )
