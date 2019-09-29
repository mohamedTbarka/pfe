from django.forms import ModelForm, Textarea

from contact.models import Contacts


class ContactForm(ModelForm):
    ''' make content field a ckeditor '''

    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'content': Textarea(attrs={'class': 'ckeditor', }),
        }

    class Media:
        js = ('ckeditor/ckeditor.js',)
        css = {
            'all': ('css/admin.css',)
        }
