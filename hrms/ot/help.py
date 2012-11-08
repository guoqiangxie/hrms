#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.models import User
from django.core.mail import  EmailMessage
from hrms.ot.models import Overtime
from hrms.settings import DEPARTS


def send_mail(ot):
    subject = ''.join([ot.apper.username, ' apply for ', ot.reason])
    message = ''.join([ot.apper.username, ' apply for ', ot.reason, ' between ', ot.begintime.isoformat(), ' and ', ot.endtime.isoformat(), ' with ', ot.status])
    mail_from = ot.apper.email
    mail_to = [getDirector(ot.apper).email]
    msg = EmailMessage(subject, message, mail_from, mail_to)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()

def getOvertimesByDepart(depart, aStatus=None):
    overtimes = Overtime.objects.all()

    if depart is not None:
        overtimes = overtimes.filter(apper__groups=depart)

    if not aStatus is None:
        overtimes = overtimes.filter(status=aStatus)
        
    return overtimes

def getDirector(u):
    return u

def getHR(u):
    return u

def getDepart(user):
    for group in user.groups.all():
        if group.name in DEPARTS:
            return group

def getEmployeesByDepart(depart):
    sql = 'SELECT u.* from auth_user u '\
          'left join auth_user_groups ug on u.id = ug.user_id '
    if not depart is None:
        sql =  sql + 'WHERE ug.group_id = \''+str(depart.id)+'\''
    return User.objects.raw(sql)

def getSpecialUser(u):
    if(u.groups.get(name='manager')):
        return PMUser(u)
    if(u.groups.get(name='director')):
        return DUser(u)
    if(u.groups.get(name='hr_audit')):
        return HRUser(u)
    return CommonUser(u)
    
class SpecialUser:
    def list(self):
        overtimes = Overtime.objects.all()
        return overtimes


class PMUser(SpecialUser):
    def __init__(self, u):
        pass;
    
    def list(self):
        overtimes = Overtime.objects.all()
        return overtimes


class DUser(SpecialUser):
    def __init__(self, u):
        pass;
    
    def list(self):
        overtimes = Overtime.objects.all()
        return overtimes


class HRUser(SpecialUser):
    def __init__(self, u):
        pass;
    
    def list(self):
        overtimes = Overtime.objects.all()
        return overtimes


class CommonUser(SpecialUser):
    def __init__(self, u):
        pass;
    
    def list(self):
        overtimes = Overtime.objects.all()
        return overtimes
