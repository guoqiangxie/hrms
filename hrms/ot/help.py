#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail, EmailMessage
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

def getOvertimesByGroup(group):
    return Overtime.objects.raw('select ot.* from ot_overtime ot '
                                'inner join auth_user u on ot.apper_id=u.id '
                                'inner join auth_user_groups ug on u.id=ug.user_id '
                                'inner join auth_group g on ug.group_id = g.id '
                                'where g.name = \''+ group.name + '\'')

def getDirector(u):
    return u

def getHR(u):
    return u

def getDepart(user):
    for group in user.groups.all():
        if group.name in DEPARTS:
            return group

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
    