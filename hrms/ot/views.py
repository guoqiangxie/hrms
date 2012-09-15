#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ot.models import Overtime, OvertimeRef
from django.forms.widgets import  Textarea
from hrms.ot.help import getOvertimesByGroup
from hrms.settings import DEPARTS


class FOvertime(forms.ModelForm):
    class Meta:
        model = Overtime
        widgets = {'remark': Textarea(attrs={'cols': 80, 'rows': 10}),
                   }


class ResetPwdForm(forms.Form):
    oldPwd = forms.CharField(widget=forms.PasswordInput)
    newPwd = forms.CharField(widget=forms.PasswordInput)
    confirmPwd = forms.CharField(widget=forms.PasswordInput)

    def clean_confirmPwd(self):
        if 'newPwd' in self.cleaned_data:
            password1 = self.cleaned_data['newPwd']
            password2 = self.cleaned_data['confirmPwd']
            if password1 == password2:
                return password2
        raise forms.ValidationError('两次密码不一样')


def page_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def resetPassword(request):
    resetPwdForm = ResetPwdForm()
    ctx = {}
    ctx['resetPwdForm'] = resetPwdForm
    if request.method == 'POST':
        resetPwdForm = ResetPwdForm(request.POST)
        user = request.user
        if resetPwdForm.is_valid():
            if user.check_password(resetPwdForm.cleaned_data['oldPwd']):
                user.set_password(resetPwdForm.cleaned_data['confirmPwd'])
                user.save()
                return redirect(reverse('logout'))
            else:
                ctx['error'] = '原始密码错误'
                render_to_response('resetPassword.html', ctx)
        else:
            return render_to_response('resetPassword.html', {'resetPwdForm': resetPwdForm})
    return render(request, 'resetPassword.html', ctx)


@login_required
def new(request):
    ctx = {}
    otf = FOvertime()
    ctx['model'] = request.user
    ctx['employees'] = User.objects.all()
    ctx['form'] = otf
    ot = Overtime()
    ot.apper = request.user
    if request.method == 'POST':
        otf = FOvertime(request.POST, instance=ot)
        if otf.is_valid():
            otf.save()
            for oterId in request.REQUEST.getlist('employee'):
                OvertimeRef(employee_id=oterId, overtimeform_id=ot.id).save()
            from ot.help import send_mail

            send_mail(ot)
            return redirect(reverse('ot_idx'))
        else:
            print 'form is not valid', otf.errors
    return render(request, 'overtimeForm.html', ctx)


@login_required
def index(request):
    overtimes = []
    for group in request.user.groups.all():
        if group.name in DEPARTS:
            for overtime in getOvertimesByGroup(group):
                overtimes.append(overtime)
    ctx = {}
    ctx['otList'] = overtimes
    return render(request, 'index.html', ctx)


@login_required
def detail(request, id):
    edit_app = get_object_or_404(Overtime, id=id)
    ctx = {}
    ctx['overtimeform'] = edit_app
    refs = OvertimeRef.objects.filter(overtimeform=edit_app)
    employees = []
    for ref in refs:
        employees.append(ref.employee)
    ctx['employees'] = employees
    return render(request, 'detail.html', ctx)
