from django.forms import ModelForm, Textarea

from service.models import Info, Service


class InfoForm(ModelForm):
    ''' make description field a ckeditor'''

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
    ''' make description and content a ckeditor'''

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
