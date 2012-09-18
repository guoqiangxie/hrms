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

def getOvertimesByDepart(depart, status=None):
    sql = 'select ot.* from ot_overtime ot ' \
          'left join auth_user u on ot.apper_id=u.id ' \
          'left join auth_user_groups ug on u.id=ug.user_id ' \
          'where 1 = 1 '

    if not depart is None:
        sql =  sql + 'and ug.group_id = \''+ str(depart.id) + '\''

    if not status is None:
        sql =  sql + 'and ot.status = \''+ status + '\''
    return Overtime.objects.raw(sql)

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

def getState(st):
    ss = {'NEW':NewState, 'APPLY':ApplyState, 'AU':AuditState}
    return ss[st]()


class NewState:
    def send(self, subject, message, ot):
        pass
    
class ApplyState:
    def send(self, subject, message, ot):
        pass

class AuditSate:
    def send(self, subject, message, ot):
        pass
    