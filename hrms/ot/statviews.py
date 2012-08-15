#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)

