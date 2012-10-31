#coding=utf-8

from django import template

register = template.Library()

def percent_decimal(value):
    value = float(str(value))
    value = round(value, 3)
    value = value * 100

    return  str(value) + '%'

register.filter('percent', percent_decimal)
