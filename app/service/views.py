from django.shortcuts import render

# Create your views here.
from django.views import generic

from marque.models import Group
from service.models import Service


class Home(generic.TemplateView):
    """
    Home page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        services = Service.objects.all()
        groups = Group.objects.all()
        context = {"services": services, "groups": groups, }
        return context
