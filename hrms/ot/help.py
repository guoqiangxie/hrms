#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail, EmailMessage


def send_mail(ot):
    subject = ''.join([ot.apper.username, ' apply for ', ot.reason])
    message = ''.join([ot.apper.username, ' apply for ', ot.reason, ' between ', ot.begintime.isoformat(), ' and ', ot.endtime.isoformat(), ' with ', ot.status])
    mail_from = ot.apper.email
    mail_to = getDirector(ot.apper).email
    msg = EmailMessage(subject, message, mail_from, [mail_to])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def getDirector(u):
    return u

def getHR(u):
    return u