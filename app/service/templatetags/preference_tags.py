from django import template

from service.models import Preference

register = template.Library()


@register.simple_tag
def preference():
    if Preference.objects.exists():
        return Preference.objects.first()
    return None
