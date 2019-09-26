from django.contrib import admin

from service.forms import InfoForm, ServiceForm, SliderForm
from . import models


@admin.register(models.Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'address',
        'phone',
        'email',
        'open_hour',
        'close_hour',
        'copyright',
    )

    def has_add_permission(self, request):
        if models.Preference.objects.exists():
            return False
        return True


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url',
        'principal',
        'order',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
    )
    form = ServiceForm
    list_editable = ('order',)


class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'order',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
    )
    form = InfoForm
    list_editable = ('order',)


class SliderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url',
        'url_text',
        'created',
        'updated',
    )
    list_filter = (
        'created',
        'updated',
    )
    form = SliderForm


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Service, ServiceAdmin)
_register(models.Info, InfoAdmin)
_register(models.Slider, SliderAdmin)
