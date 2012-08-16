#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import render
from hrms.ot.models import Overtimeform

def apply(request, id):
    return render(request, 'index.html', ctx)

def applyFormList(request):
    ctx = {}
    ctx['applyFormList'] = Overtimeform.objects.filter(status='NEW')
    return render(request, 'applyFormList.html', ctx)

def confirm(request, id):
    ctx = {}
    return render(request, 'index.html', ctx)

