#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


OLIVER_STATE_CHOICES = ((u'NEW', u'create'),
                 (u'APPLY', u'apply'),
                 (u'DENY', u'deny'),
                 (u'CONFIRM', u'confirm'),
                 (u'VERIFY', u'verify'),
                 (u'FINISH', u'finish'),
                 )

IVEN_STATE_CHOICES = ((u'0', u'unverify'),
                 (u'1', u'verify'),
                 )


class Oliver(models.Model):
    '''加班申请单
    '''
    applyer = models.ForeignKey(User)
    begintime = models.DateTimeField()
    delta = models.FloatField()
    memo = models.CharField(max_length=255)
    status = models.CharField(max_length=8, choices=OLIVER_STATE_CHOICES, default='NEW')

    def toApply(self):
        self.status = 'APPLY'
        self.save()
        
    def deny(self):
        self.status = 'DENY'
        self.save()
    
    def verifyAll(self):
        pass;
    
    def auditAll(self):
        pass;
    
    def predictTime(self):
        return len(Iven.objects.filter(oliver=self))*self.delta
    
    def actualTime(self):
        return sum([x.actual for x in Iven.objects.filter(oliver=self)])
    
    def __unicode__(self):
        return str(self.id) + ":" + self.applyer.username
            
    

class Iven(models.Model):
    '''个人加班单
    '''
    oliver = models.ForeignKey(Oliver)
    employeer = models.ForeignKey(User)
    beginTime = models.DateTimeField()
    delta = models.FloatField()
    status = models.CharField(max_length=8, choices=IVEN_STATE_CHOICES, default='0')
    actual = models.FloatField(blank=True)
    
    def verify(self):
        self.status = 1
        self.save()
        return self.__checkLast()
    
    def __checkLast(self):
        return len(Iven.objects.filter(oliver=self.oliver, status = 0)) == 0
    
    def audit(self, actualTime):
        self.actual = actualTime
        self.save()


class Simon(models.Model):
    oliver = models.ForeignKey(Oliver)
    operator = models.ForeignKey(User)
    memo = models.CharField(max_length=255)
    action = models.CharField(max_length=8)
    processTime = models.DateTimeField()
    
    
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
