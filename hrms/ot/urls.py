from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^ot/$', 'ot.views.index', name='ot_idx'),
    url(r'^ot/new/$', 'ot.views.new', name='ot_new'),
    url(r'^ot/(?P<id>\d+)/edit/$', 'ot.views.edit', name='ot_edit'),
    url(r'^ot/(?P<id>\d+)/delete/$', 'ot.views.delete', name='ot_delete'),
    url(r'^ot/addEmployee/$', 'ot.employee.add', name='ot_employee_add'),

)
