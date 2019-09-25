# vim: set fileencoding=utf-8 :
from django.contrib import admin

from nouveaute.forms import PromotionForm, EventForm, CompagneForm
from nouveaute.models import Display
from . import models


class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'image',
        'content',
        'date',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
        'date',
    )
    form = PromotionForm


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'start_date',
        'end_date',
        'image',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
        'start_date',
        'end_date',
    )
    form = EventForm


class CompagneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'date',
        'image',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
        'date',
    )
    form = CompagneForm


class DisplayInline(admin.TabularInline):
    model = Display


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated',)
    list_filter = ('created', 'updated',)
    search_fields = ('name',)
    inlines = [DisplayInline]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Promotion, PromotionAdmin)
_register(models.Event, EventAdmin)
_register(models.Compagne, CompagneAdmin)
_register(models.Gallery, GalleryAdmin)
