#!/usr/bin/env python
# coding: utf-8
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ot.views.index', name='ot_idx'),
    url(r'^new/$', 'ot.views.new', name='ot_new'),
    url(r'^(?P<id>\d+)/apply/$', 'ot.applyviews.apply', name='ot_apply'),
    url(r'^(?P<id>\d+)/view/$', 'ot.views.detail', name='ot_overtime_detail'),
    url(r'^/applyFormList/$', 'ot.applyviews.applyFormList', name='ot_applyFormList'),
    url(r'^/auditFormList/$', 'ot.applyviews.auditFormList', name='ot_auditFormList'),
    url(r'^(?P<id>\d+)/confirm/$', 'ot.applyviews.confirm', name='ot_confirm'),
    url(r'^stat$', 'ot.statviews.stat', name='ot_stat'),
    url(r'^export$', 'ot.statviews.export', name='ot_export'),
)
