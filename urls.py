from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable django-export:
    # url(r'^admin/export/', include('export.urls')),
    # Uncomment the next line to enable django-webalizer:
    # url(r'^admin/webalizer/', include('webalizer.urls')),

    (r'^admin/(.*)', admin.site.root),
)
