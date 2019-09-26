from django.forms import ModelForm, Textarea

from service.models import Info, Service, Slider, Discover


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


class SliderForm(ModelForm):
    ''' make description field a ckeditor'''

    class Meta:
        model = Slider
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }

class DiscoverForm(ModelForm):
    ''' make description field a ckeditor'''

    class Meta:
        model = Discover
        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }
