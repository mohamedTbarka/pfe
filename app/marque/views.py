from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from marque.models import Marque


class MarqueListView(generic.ListView):
    """
    Marque list page
    """
    model = Marque
    paginate_by = 50  # if pagination is desired
    template_name = "marque_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
