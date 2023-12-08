# yourapp/templatetags/date_tags.py

from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='date_filter')
def date_filter(val):
    return datetime.now().date()
