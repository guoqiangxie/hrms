from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ot.views.index', name='ot_idx'),
    url(r'^new/$', 'ot.views.new', name='ot_new'),
    url(r'^(?P<id>\d+)/apply/$', 'ot.applyviews.apply', name='ot_apply'),
    url(r'^(?P<id>\d+)/overtimedetail/$', 'ot.applyviews.overtimedetail', name='ot_overtime_detail'),
    url(r'^/applyFormList/$', 'ot.applyviews.applyFormList', name='ot_applyFormList'),
    url(r'^(?P<id>\d+)/confirm/$', 'ot.applyviews.confirm', name='ot_confirm'),
    url(r'^stat$', 'ot.statviews.index', name='ot_stat'),
)
