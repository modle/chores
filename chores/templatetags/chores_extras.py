from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='overdue')
def overdue(value, frequency):
    dt = timezone.now() - value
    days = dt.days - frequency
    if days > 99:
        days = 999
    return days
