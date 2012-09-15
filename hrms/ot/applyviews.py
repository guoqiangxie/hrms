#!/usr/bin/env python
# coding: utf-8
import datetime
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from ot.models import Overtime, ApplyTrack, OvertimeRef


class apply_trackform(forms.Form):
    status = forms.CharField(label='同意审批', widget=forms.CheckboxInput)
    approval_note = forms.CharField(max_length=255, label='审批意见', widget=forms.Textarea)


@login_required
def apply(request, id):
    edit_app = get_object_or_404(Overtime, id=id)
    ctx = {}
    ctx['overtimeform'] = edit_app
    ctx['applyform'] = apply_trackform()
    if request.method == 'POST':
        appForm = apply_trackform(request.POST)
        if appForm.is_valid():
            status = appForm.cleaned_data['status']
            approval_note = appForm.cleaned_data['approval_note']
            ApplyTrack(apply_type='DEPART', approval_note=approval_note, approval=request.user, overtimeform=edit_app, apply_date=datetime.datetime.now()).save()
            if status == 'on':
                edit_app.status = 'APPLY'
            else:
                edit_app.status = 'CAN'
            edit_app.save()
            from ot.help import send_mail
            send_mail(edit_app)
            return redirect(reverse('ot_idx'))
        else:
            print 'form is not valid:', appForm.errors
    refs = OvertimeRef.objects.filter(overtimeform=edit_app)
    employees = []
    for ref in refs:
        employees.append(ref.employee)
    ctx['employees'] = employees
    return render(request, 'apply.html', ctx)


@login_required
def applyFormList(request):
    return redirect(reverse('ot_idx'))


@login_required
def auditFormList(request):
    return redirect(reverse('ot_idx'))


@login_required
def confirm(request, id):
    edit_app = get_object_or_404(Overtime, id=id)
    ctx = {}
    ctx['overtimeform'] = edit_app
    ctx['applyform'] = apply_trackform()
    if request.method == 'POST':
        appForm = apply_trackform(request.POST)
        if appForm.is_valid():
            status = appForm.cleaned_data['status']
            approval_note = appForm.cleaned_data['approval_note']
            ApplyTrack(apply_type='HR', approval_note=approval_note, approval=request.user, overtimeform=edit_app, apply_date=datetime.datetime.now()).save()
            if status == 'on':
                edit_app.status = 'AU'
            else:
                edit_app.status = 'DC'
            edit_app.save()
            from ot.help import send_mail
            send_mail(edit_app)
            return redirect(reverse('ot_idx'))
        else:
            print 'form is not valid:', appForm.errors
    refs = OvertimeRef.objects.filter(overtimeform=edit_app)
    employees = []
    for ref in refs:
        employees.append(ref.employee)
    ctx['employees'] = employees
    return render(request, 'apply.html', ctx)




