from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='overdue')
def overdue(value, frequency):
    dt = timezone.now() - value
    days = dt.days - frequency
    if days > 90:
        days = 999
    return days

@register.filter(name='absolute')
def absolute(value):
    absolute_value = abs(value)
    return absolute_value
