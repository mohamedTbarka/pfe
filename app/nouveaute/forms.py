from django.forms import ModelForm, Textarea

from nouveaute.models import Event, Compagne, Promotion


class EventForm(ModelForm):
    ''' make content field a ckeditor '''

    class Meta:
        model = Event

        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }


class CompagneForm(ModelForm):
    ''' make content field a ckeditor '''

    class Meta:
        model = Compagne

        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }


class PromotionForm(ModelForm):
    ''' make content field a ckeditor '''

    class Meta:
        model = Promotion

        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }
