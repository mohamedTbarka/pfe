from django.forms import ModelForm, Textarea

from service.models import Info, Service


class InfoForm(ModelForm):
    ''' mettre field titre un ckeditor'''

    class Meta:
        model = Info
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }


class ServiceForm(ModelForm):
    ''' mettre field titre un ckeditor'''

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'class': 'ckeditor', }),
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }
