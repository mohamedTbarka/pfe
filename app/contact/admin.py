# vim: set fileencoding=utf-8 :
from django.contrib import admin

from contact.forms import ContactForm
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'object',
        'content',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
    )
    search_fields = ('name',)
    form = ContactForm


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'subscribed', 'created', 'updated',)
    list_filter = (
        'created',
        'updated',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.Newsletter, NewsletterAdmin)
