from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from marque.models import Group
from service.models import Service, Info, Slider, Discover

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


class DiscoverListView(generic.ListView):
    """
    Discover list page
    """
    model = Discover
    paginate_by = 50  # if pagination is desired
    template_name = "decouvrir.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Plan(generic.TemplateView):
    """
    Plan page
    """
    template_name = 'plan.html'


def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {}, RequestContext(request))
    response.status_code = 500
    return response
