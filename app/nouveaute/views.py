import datetime

from django.db.models import Q
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
    template_name = "promotions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PromotionDetailView(generic.DetailView):
    model = Promotion
    template_name = "promotion_detail.html"


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

    def get_queryset(self):
        return Event.objects.filter(Q(start_date__gte=timezone.now()) | Q(end_date__gte=timezone.now()))


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "event_detail.html"


class CompagneListView(generic.ListView):
    """
    Compagne list page
    """
    model = Compagne
    paginate_by = 50  # if pagination is desired
    template_name = "compagne.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CompagneDetailView(generic.DetailView):
    model = Compagne
    template_name = "promotion_detail.html"


class NouveauteList(generic.TemplateView):
    """
    Nouveautes List page
    """
    template_name = "nouveautes_list.html"
    def get_context_data(self, **kwargs):
        events = Event.objects.filter(Q(start_date__gte=timezone.now()) | Q(end_date__gte=timezone.now()))
        compagnes = Compagne.objects.filter(date__gte=timezone.now())
        promotions = Promotion.objects.filter(date__gte=timezone.now())
        nouveautes = []
        for event in events:
            nouveautes.append({"title": event.title, "date": event.start_date, "end_date": event.end_date,
                               "image": event.get_image_url(), "type": "Evenement", "badge": event.get_badge()})
        for compagne in compagnes:
            nouveautes.append({"title": compagne.title, "date": compagne.date, "end_date": None,
                               "image": compagne.get_image_url(), "type": "Compagne", "badge": None})
        for promotion in promotions:
            nouveautes.append({"title": promotion.title, "date": promotion.date, "end_date": None,
                               "image": promotion.get_image_url(), "type": "Compagne", "badge": None})

        context = {"nouveautes": events, }
        return context
