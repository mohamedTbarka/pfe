# vim: set fileencoding=utf-8 :
from django.contrib import admin

from marque.forms import MarqueForm
from . import models


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated',)
    list_filter = ('created', 'updated',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sup_category', 'created', 'updated',)
    list_filter = (
        'sup_category',
        'created',
        'updated',
    )
    search_fields = ('name',)


class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created', 'updated',)
    list_filter = ('created', 'updated',)


class MarqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'email', 'phone', 'localisation', 'created', 'updated',)
    list_filter = ('group', 'created', 'updated',)
    filter_horizontal = ('categories',)
    search_fields = ('name',)
    form = MarqueForm


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Group, GroupAdmin)
_register(models.Category, CategoryAdmin)
_register(models.Slide, SlideAdmin)
_register(models.Marque, MarqueAdmin)
