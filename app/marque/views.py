import string

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
        alphas = list(string.ascii_lowercase)
        alphabet = []
        for alpha in alphas:
            alphabet.append({'%s' % alpha: Marque.objects.filter(name__istartswith=alpha).exists()})
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['alphabet'] = alphabet
        return context

    # def get_queryset(self):
    #     alpha = self.request.GET.get('alpha', '')
    #     cat = self.request.GET.get('cate', '')
    #     new_context = Marque.objects.filter(name__istartswith=alpha,categories__name=cat )
    #     return new_context


class MarqueDetailView(generic.DetailView):
    model = Marque
