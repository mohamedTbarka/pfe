from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from nouveaute.models import Promotion, Event, Compagne


class PromotionListView(generic.ListView):
    """
    Promotion list page
    """
    model = Promotion
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class EventListView(generic.ListView):
    """
    Event list page
    """
    model = Event
    paginate_by = 50  # if pagination is desired
    template_name = "evenements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CompagneListView(generic.ListView):
    """
    Compagne list page
    """
    model = Compagne
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
