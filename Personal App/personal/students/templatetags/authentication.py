from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag()
def from_staff(user):
    return user.groups.filter(name='staff').exists()