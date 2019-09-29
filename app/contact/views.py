from django.shortcuts import render

# Create your views here.
from django.views import generic
from rest_framework import mixins, viewsets

from contact.models import Newsletter, Contacts
from contact.serializers import NewsletterSerializer, ContactSerializer


class SubscribeAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()


class ContactAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()


class Contact(generic.TemplateView):
    """
    Contact page
    """
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['success'] = False
        if "email" in self.request.GET:
            name = self.request.GET.get('nom')
            email = self.request.GET.get('email')
            phone = self.request.GET.get('phone')
            objet = self.request.GET.get('objet')
            content = self.request.GET.get('message')

            if name and email and phone and objet and content:
                c = Contacts(name=name,
                            email=email,
                            phone=phone,
                            object=objet,
                            content=content,
                            )
                c.save()
                context['success'] = True
        return context
