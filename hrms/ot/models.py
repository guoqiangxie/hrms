#coding=utf-8

from django.db import models

class Application(models.Model):
    subject = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    applicationDate = models.DateField()
    applicant = models.CharField(max_length=10)

    def __unicode__(self):
        return self.subject


class Person(models.Model):
    app = models.ForeignKey(Application)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

#    员工表
class Employee(models.Model):
#    员工姓名
    name = models.CharField(max_length=20)
#    员工邮箱地址
    email = models.EmailField(max_length=40)
#    员工手机
    telephone = models.CharField(max_length=20)
#    员工级别
    level = models.CharField(max_length=10)

    def __unicode__(self):
            return self.name

#   加班申请单
class Overtimeform(models.Model):
#   加班开始时间
    begintime = models.DateTimeField()
#   加班结束时间
    endtime = models.DateTimeField()
#   加班理由
    reason = models.CharField(max_length=255)
#   备注
    remark = models.CharField(max_length=255)
#   申请人
    applyer = models.ForeignKey(Employee)
#   状态
    status = models.CharField(max_length=5)

    def __unicode__(self):
        return self.applyer + self.reason

#    员工加班中间表
class Employee_overtimeform_ref(models.Model):
#    员工
    employee = models.ForeignKey(Employee)
#    加班申请单
    overtimeform = models.ForeignKey(Overtimeform)

    def __unicode__(self):
        return self.employee + self.overtimeform


#    审批流程
class apply_track(models.Model):
#    加班申请单
    overtimeform = models.ForeignKey(Employee_overtimeform_ref)
#    审批人
    approval = models.ForeignKey(Employee)
#    审批意见
    approval_note = models.CharField(max_length=255)
#    审批时间
    apply_date = models.DateTimeField()
#    审批类型
    type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.approval + self.overtimeform + self.type