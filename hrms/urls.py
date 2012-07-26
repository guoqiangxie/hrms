#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns(  # Examples:
                         # url(r'^hrms/', include('hrms.foo.urls')),
                         # Uncomment the admin/doc line below to enable admin documentation:
                         # Uncomment the next line to enable the admin:
    '',
    url(r'^$', 'ot.views.index', name='idx'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ot/', include('ot.urls')),
    url(r'^accounts/login/$', login, {'template_name': 'ot/login.html'
        }),
    url(r'^accounts/logout/$', logout),
    )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
