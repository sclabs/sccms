from django.conf.urls.defaults import *

urlpatterns = patterns('sccms.views',
    url(r'^$', 'lastcomic', name="last"),
    url(r'^(\d+)/$', 'particularcomic', name="particular"),
    url(r'^random/$', 'randomcomic', name="random"),
    url(r'^(\d+)/previous/$', 'previouscomic', name="previous"),
    url(r'^(\d+)/next/$', 'nextcomic', name="next"),
)
