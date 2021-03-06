#!/usr/bin/env python
# coding: utf-8
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from ot.models import Overtime, OvertimeRef
import datetime
import xlwt


class FOvertime(forms.ModelForm):
    class Meta:
        model = Overtime


def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)

@login_required
def stat(request):
    ctx = {}
    overtimes = Overtime.objects.all()
    ctx['overtimes'] = overtimes
    return render(request, 'ot/stat.html', ctx)


@login_required
def export(request):
    overtimes = Overtime.objects.all()

    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet')

    ws.write(0, 0, u'基本信息')
    ws.write(1, 0, u'姓名')
    ws.write(1, 1, request.user.username)
    ws.write(2, 0, u'部门')
    ws.write(3, 0, u'入职日期')
    ws.write(4, 0, u'已休年假天数')
    ws.write(5, 0, u'年假剩余天数')

    ws.write(7, 0, u'加班信息')
    ws.write(8, 1, u'原因')
    ws.write(8, 2, u'开始时间')
    ws.write(8, 3, u'结束时间')
    ws.write(8, 4, u'加班时间(小时)')

    i = 0
    for overtime in overtimes:
        ws.write(9+i, 0, i+1)
        ws.write(9+i, 1, overtime.reason)
        ws.write(9+i, 2, unicode(overtime.begintime.strftime('%Y年%m月%d日 %H:%M'), 'utf-8'))
        ws.write(9+i, 3, unicode(overtime.begintime.strftime('%Y年%m月%d日 %H:%M'), 'utf-8'))
        ws.write(9+i, 4, overtime.total_time)
        i = i + 1

    fname = datetime.datetime.now().strftime('%Y%m%d.xls')
    response = HttpResponse(mimetype="application/x-download")
    response['Content-Disposition'] ='attachment; filename=%s' % smart_str(fname) #解决文件名乱码/不显示的问题
    wb.save(response)
    return response
