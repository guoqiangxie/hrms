#!/usr/bin/env python
# coding: utf-8
from django import template

register = template.Library()
__ABC = {'NEW':'待确认', 'APPLY':'待审核', 'AU':'已审核', 'CAN':'总监打回', 'DC':'人事打回'}

@register.filter(name='screenname')
def screenname(value):
    return __ABC.get(value, value)