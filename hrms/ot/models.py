#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Overtime(models.Model):
    '''加班申请单
    '''
    STATE_CHOICES = ((u'NEW', u'create'),
                     (u'APPLY', u'apply'),
                     (u'AU', u'audit'),
                     (u'CF', u'confirm'),
                     (u'CAN', u'cancel'),
                     (u'DC', u'decline'),
                     )
    begintime = models.DateTimeField()
    endtime = models.DateTimeField()
    reason = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    status = models.CharField(max_length=5, choices=STATE_CHOICES)
    apper = models.ForeignKey(User)

    def __unicode__(self):
        return self.apper.username + ', ' + self.reason

    @property
    def total_time(self):
        initTime = self.begintime.replace(hour=19, minute=0, second=0)
        begin = max(initTime, self.begintime)
        return max(0, int((self.endtime - begin).total_seconds() / 3600))


class OvertimeRef(models.Model):
    '''员工加班中间表
    '''
    employee = models.ForeignKey(User)
    overtimeform = models.ForeignKey(Overtime)

    def __unicode__(self):
        return self.employee + self.overtimeform


class ApplyTrack(models.Model):
    '''审批流程
    '''
    overtimeform = models.ForeignKey(Overtime)
    approval = models.ForeignKey(User)
    approval_note = models.CharField(max_length=255)
    apply_date = models.DateTimeField()
    apply_type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.approval + self.overtimeform + self.type


class userpermission(models.Model):
    class Meta:
        permissions = (
            ("depart_confirm_overtimeform", "Depart director confirm overtimeform"),
            ("hr_audit_overtimeform", "Hr audit overtimeform"),
        )
