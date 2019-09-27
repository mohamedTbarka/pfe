from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from contact.models import Newsletter, Contact
from contact.serializers import NewsletterSerializer, ContactSerializer


class SubscribeAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()


class ContactAPIView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
