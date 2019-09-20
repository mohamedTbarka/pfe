from django import template

from app import settings
from service.models import Preference

register = template.Library()


@register.simple_tag
def logo():
    if Preference.objects.exists():
        return "{0}{1}".format(settings.MEDIA_URL, Preference.objects.first().logo)
    return ""


@register.simple_tag
def icon():
    if Preference.objects.exists():
        return "{0}{1}".format(settings.MEDIA_URL, Preference.objects.first().icon)
    return ""


@register.simple_tag
def background_image():
    if Preference.objects.exists():
        return "{0}{1}".format(settings.MEDIA_URL, Preference.objects.first().background_image)
    return ""


@register.simple_tag
def title():
    if Preference.objects.exists():
        return Preference.objects.first().title.title()
    return ""


@register.simple_tag
def address():
    if Preference.objects.exists():
        return Preference.objects.first().address
    return ""


@register.simple_tag
def phone():
    if Preference.objects.exists():
        return Preference.objects.first().phone
    return ""

@register.simple_tag
def email():
    if Preference.objects.exists():
        return Preference.objects.first().email
    return ""

@register.simple_tag
def open_hour():
    if Preference.objects.exists():
        return Preference.objects.first().open_hour
    return ""

@register.simple_tag
def close_hour():
    if Preference.objects.exists():
        return Preference.objects.first().close_hour
    return ""


@register.simple_tag
def copyright():
    if Preference.objects.exists():
        return Preference.objects.first().copyright
    return ""
