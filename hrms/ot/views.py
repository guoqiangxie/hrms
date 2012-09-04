#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from hrms.ot.models import overtimeform, employee_overtimeform_ref, userpermission


class OvertimeForm(forms.ModelForm):
    class Meta:
        model = overtimeform

class Employee_overtimeform_refForm(forms.ModelForm):
    class Meta:
        model = employee_overtimeform_ref

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def new(request):
    ctx = {}
    overtimeForm = OvertimeForm()
    ctx['model'] = request.user
    ctx['employees'] = User.objects.all()
    ctx['form'] = overtimeForm
    user =  request.user
#    测试权限处理
    print(user.has_perm("ot.show_apply_track"))
    print(user.get_group_permissions())
    print(user.has_perm("auth.add_user"))
    if request.method == 'POST':
        overtimeForm = OvertimeForm(request.POST)
        if overtimeForm.is_valid():
            overtimeForm = overtimeForm.save()
            overtimeFormId = overtimeForm.id
            oterIds =  request.REQUEST.getlist('employee')
            for oterId in oterIds:
                employee_overtimeform_ref = Employee_overtimeform_refForm({'employee': oterId, 'overtimeform':overtimeFormId})
                employee_overtimeform_ref.save()
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'overtimeForm.html', ctx)

