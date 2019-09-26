from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from marque.models import Group
from service.models import Service, Info, Slider


class Home(generic.TemplateView):
    """
    Home page
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        services = Service.objects.all().order_by('order')
        groups = Group.objects.all()
        infos = Info.objects.all().order_by('order')
        slides = Slider.objects.all()
        context = {"services": services, "groups": groups, "infos": infos, "slides": slides}
        return context


class ServiceDetailView(generic.DetailView):
    model = Service
