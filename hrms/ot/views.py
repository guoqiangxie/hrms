#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from models import Application, Person

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

@login_required
def index(request):
    ctx = {}
    ctx['applications'] = Application.objects.all()
    return render(request, 'index.html', ctx)

def new(request):
    appForm = ApplicationForm()
    if request.method == 'POST':
        appForm = ApplicationForm(request.POST)
        if appForm.is_valid():
            appForm.save()
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'form.html', {'form': appForm})

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
