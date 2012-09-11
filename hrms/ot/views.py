#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ot.models import Overtime, OvertimeRef
import datetime
from django.forms.widgets import Widget, Textarea


class FOvertime(forms.ModelForm):
    class Meta:
        model = Overtime
        widgets = {'remark':Textarea(attrs={'cols':80, 'rows':10}),
                   }


def page_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


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
            return redirect(reverse('ot_idx'))
        else:
            print 'form is not valid', otf.errors
    return render(request, 'overtimeForm.html', ctx)


@login_required
def index(request):
    ctx = {}
    ctx['otList'] = Overtime.objects.all()
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
