from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from contact.serializers import NewsletterSerializer


class SubscribeAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = NewsletterSerializer
