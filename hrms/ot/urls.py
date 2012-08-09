from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ot.views.index', name='ot_idx'),
    url(r'^new/$', 'ot.views.new', name='ot_new'),
    url(r'^(?P<id>\d+)/edit/$', 'ot.views.edit', name='ot_edit'),
    url(r'^(?P<id>\d+)/delete/$', 'ot.views.delete', name='ot_delete'),
    url(r'^addEmployee/$', 'ot.employee.add', name='ot_employee_add'),
    url(r'^addOvertimeform/$', 'ot.overtimeform.add', name='ot_overtimeform_add'),

)
