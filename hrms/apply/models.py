#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class apply_track(models.Model):

    approval_note = models.CharField(max_length=255)
    apply_date = models.DateTimeField()
    type = models.CharField(max_length=10)

    def __unicode__(self):
        return self.approval + self.overtimeform + self.type
