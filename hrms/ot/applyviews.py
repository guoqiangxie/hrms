#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from hrms.ot.models import Overtimeform, Employee_overtimeform_ref, apply_track
from hrms.ot.views import OvertimeForm

class apply_trackform(forms.ModelForm):
    class Meta:
        model = apply_track

@login_required
def apply(request, id):
    edit_app = get_object_or_404(Overtimeform, id=id)
    ctx = {}
    ctx['overtimeform'] = edit_app
    appForm = apply_trackform()
    if request.method == 'POST':
        appForm = apply_trackform(request.POST)
        appForm.save()
        overtimeForm = OvertimeForm(instance=edit_app)
        overtimeForm.status = 'APPLY'
        overtimeForm.save()
        return render(request, 'index.html')
    ctx['applyform'] = appForm
    ctx['model'] = User.objects.get(id=request.session["_auth_user_id"]).get_profile()
    refs = Employee_overtimeform_ref.objects.filter(overtimeform=edit_app)
    employees = []
    for ref in refs:
        employees.append(ref.employee)
    ctx['employees'] = employees
    return render(request, 'apply.html', ctx)

@login_required
def applyFormList(request):
    ctx = {}
    ctx['applyFormList'] = Overtimeform.objects.filter(status='NEW')
    return render(request, 'applyFormList.html', ctx)

@login_required
def confirm(request, id):
    ctx = {}
    return render(request, 'index.html', ctx)

