# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PromotionAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'created', 'updated',)
    list_filter = (
        'created',
        'updated',
    )
    search_fields = ('title',)


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'description',
        'start_date',
        'end_date',
    )
    list_filter = (
        'created',
        'updated',
        'start_date',
        'end_date',
    )
    search_fields = ('title',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Promotion, PromotionAdmin)
_register(models.Event, EventAdmin)
