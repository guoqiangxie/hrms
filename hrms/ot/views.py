#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from hrms.ot.models import  Overtimeform

from models import Application

class OvertimeForm(forms.ModelForm):
    class Meta:
        model = Overtimeform

@login_required
def index(request):
    return render(request, 'index.html')

def new(request):
    ctx = {}
    overtimeForm = OvertimeForm()
    ctx['model'] = User.objects.get(id=request.session["_auth_user_id"]).get_profile()
    ctx['form'] = overtimeForm
    if request.method == 'POST':
        overtimeForm = OvertimeForm(request.POST)
        if overtimeForm.is_valid():
            overtimeForm = overtimeForm.save()
            id = overtimeForm.id
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'overtimeForm.html', ctx)

def edit(request, id):
    edit_app = get_object_or_404(Application, id=id)
    appForm = ApplicationForm(instance=edit_app)
    if request.method=='POST':
        appForm = ApplicationForm(request.POST, instance=edit_app)
        if appForm.is_valid():
            appForm.save()
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'form.html', {'form':appForm})

def delete(request, id):
    del_app = get_object_or_404(Application, id=id)
    del_app.delete()
    return HttpResponseRedirect(reverse('ot_idx'))

def show(request, id):
    del_app = get_object_or_404(Application, id=id)
    return HttpResponseRedirect(reverse('ot_idx'))
