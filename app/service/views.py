from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from marque.models import Group
from service.models import Service, Info, Slider, Discover, Hotel, Bureau

from django.shortcuts import render_to_response
from django.template import RequestContext


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
    template_name = "service_detail.html"

class DiscoverListView(generic.ListView):
    """
    Discover list page
    """
    model = Discover
    # paginate_by = 50  # if pagination is desired
    template_name = "decouvrir.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class HotelListView(generic.ListView):
    """
    Hotel list page
    """
    model = Hotel
    # paginate_by = 50  # if pagination is desired
    template_name = "hotel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BureauListView(generic.ListView):
    """
    Bureau list page
    """
    model = Bureau
    # paginate_by = 50  # if pagination is desired
    template_name = "bureau.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Plan(generic.TemplateView):
    """
    Plan page
    """
    template_name = 'plan.html'


class Navigator(generic.TemplateView):
    """
    navigator page
    """
    template_name = 'navigator.html'


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
