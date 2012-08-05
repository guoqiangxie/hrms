#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from hrms.ot.models import Employee, Overtimeform

class OvertimeForm(forms.ModelForm):
    class Meta:
        model = Overtimeform

def add(request):
    overtimeForm = OvertimeForm()
    if request.method == 'POST':
        overtimeForm = OvertimeForm(request.POST)
        if overtimeForm.is_valid():
            overtimeForm.save()
            return HttpResponseRedirect(reverse('ot_idx'))
    return render(request, 'overtimeForm.html', {'form': overtimeForm})

#def edit(request, id):
#    edit_app = get_object_or_404(Application, id=id)
#    appForm = ApplicationForm(instance=edit_app)
#    if request.method=='POST':
#        appForm = ApplicationForm(request.POST, instance=edit_app)
#        if appForm.is_valid():
#            appForm.save()
#            return HttpResponseRedirect(reverse('ot_idx'))
#    return render(request, 'form.html', {'form':appForm})
#
#def delete(request, id):
#    del_app = get_object_or_404(Application, id=id)
#    del_app.delete()
#    return HttpResponseRedirect(reverse('ot_idx'))
