from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ot.views.index', name='ot_idx'),
    url(r'^new/$', 'ot.views.new', name='ot_new'),
    url(r'^(?P<id>\d+)/edit/$', 'ot.views.edit', name='ot_edit'),
    url(r'^(?P<id>\d+)/delete/$', 'ot.views.delete', name='ot_delete'),
    url(r'^(?P<id>\d+)/apply/$', 'ot.applyviews.apply', name='ot_apply'),
    url(r'^(?P<id>\d+)/confirm/$', 'ot.applyviews.confirm', name='ot_confirm'),
    url(r'^stat$', 'ot.statviews.index', name='ot_stat'),
    url(r'^(?P<id>\d+)/show/$', 'ot.views.show', name='ot_show'),


)
