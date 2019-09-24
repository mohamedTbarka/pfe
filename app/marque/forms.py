from django.forms import ModelForm, Textarea

from marque.models import Marque


class MarqueForm(ModelForm):
    ''' make content field a ckeditor '''

    class Meta:
        model = Marque

        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
            'open_hours': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }

