#coding=utf-8
from django.contrib.auth.models import User
from django.db import models
import datetime

class overtimeform(models.Model):
    '''加班申请单
    '''
    #   加班开始时间
    begintime = models.DateTimeField()
    #   加班结束时间
    endtime = models.DateTimeField()
    #   加班理由
    reason = models.CharField(max_length=255)
    #   备注
    remark = models.CharField(max_length=255)
    #   申请人
    applyer = models.ForeignKey(User)
    #   状态
    status = models.CharField(max_length=5)

    def __unicode__(self):
        return self.applyer.username + ', ' + self.reason
        
    @property
    def total_time(self):
        begin = self.begintime
        if self.begintime.hour < 19:
            begin = datetime.datetime(self.begintime.year, self.begintime.month, self.begintime.day, 19, 0, 0)
        total = int((self.endtime-begin).total_seconds()/3600)
        if total < 0:
            total = 0
        return total

class employee_overtimeform_ref(models.Model):
    '''员工加班中间表
    '''
    #    员工
    employee = models.ForeignKey(User)
    #    加班申请单
    overtimeform = models.ForeignKey(overtimeform)

    def __unicode__(self):
        return self.employee + self.overtimeform


class apply_track(models.Model):
    '''审批流程
    '''
    #    加班申请单
    overtimeform = models.ForeignKey(overtimeform)
    #    审批人
    approval = models.ForeignKey(User)
    #    审批意见
    approval_note = models.CharField(max_length=255)
    #    审批时间
    apply_date = models.DateTimeField()
    #    审批类型
    type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.approval + self.overtimeform + self.type


class userpermission(models.Model):
    class Meta:
        permissions = (
            ("apply_overtimeform", "Can apply overtimeform"),
            ("depart_confirm_overtimeform", "Depart director confirm overtimeform"),
            ("hr_audit_overtimeform", "Hr audit audit overtimeform"),
        )
