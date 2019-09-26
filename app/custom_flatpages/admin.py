# coding=utf-8
from django.contrib import admin
from django.forms import ModelForm, Textarea
from django.core.exceptions import ValidationError

from custom_flatpages.models import FlatPage, Display, Gallery


class FlatPageForm(ModelForm):
    class Meta:
        model = FlatPage
        fields = '__all__'
        # search_fields = ('url', 'title')
        widgets = {
            'description': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }

    def clean(self):
        url = self.cleaned_data.get('url')
        if not url.startswith("/"):
            raise ValidationError("url must start with /")

        if not url.endswith("/"):
            raise ValidationError("url must end with /")


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageForm
    list_display = ("titre", 'url',"order")

    class Meta:
        model = FlatPage

class DisplayInline(admin.TabularInline):
    model = Display


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated',)
    list_filter = ('created', 'updated',)
    search_fields = ('name',)
    inlines = [DisplayInline]

admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Gallery, GalleryAdmin)
