#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from ot.models import Overtime, OvertimeRef
import datetime
import xlwt
from django.utils.encoding import smart_str
from django.forms.widgets import Widget, Textarea


class FOvertime(forms.ModelForm):
    class Meta:
        model = Overtime
        widgets = {'remark':Textarea(attrs={'cols':80,'rows':10}),
                   }


class FOvertimeRef(forms.ModelForm):
    class Meta:
        model = OvertimeRef


@login_required
def index(request):
    return render(request, 'index.html')


def page_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def new(request):
    ctx = {}
    overtimeForm = FOvertime()
    ctx['model'] = request.user
    ctx['employees'] = User.objects.all()
    ctx['form'] = overtimeForm
    if request.method == 'POST':
        overtimeForm = FOvertime(request.POST)
        if overtimeForm.is_valid():
            overtimeForm = overtimeForm.save()
            overtimeFormId = overtimeForm.id
            oterIds = request.REQUEST.getlist('employee')
            for oterId in oterIds:
                employee_overtimeform_ref = OvertimeRef({'employee': oterId, 'overtimeform': overtimeFormId})
                employee_overtimeform_ref.save()
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'overtimeForm.html', ctx)


