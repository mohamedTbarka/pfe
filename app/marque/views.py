import string

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic

from marque.models import Marque, Category


class MarqueListView(generic.ListView):
    """
    Marque list page
    """
    model = Marque
    # paginate_by = 50  # if pagination is desired
    template_name = "marque_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alphas = list(string.ascii_lowercase)
        alphabet = []
        for alpha in alphas:
            alphabet.append({'key': alpha, "value": context["marque_list"].filter(name__istartswith=alpha).exists()})

        alpha = self.request.GET.get('alpha', '')
        cat = self.request.GET.get('cat', '')
        group = self.request.GET.get('group', '')

        context['now'] = timezone.now()
        context['alphabet'] = alphabet
        context['categories'] = Category.objects.all()
        if group:
            context['categories'] = Category.objects.filter(group=group)
            context['group'] = group
        if alpha:
            context['alpha'] = alpha
        if cat:
            context['cat'] = cat

        return context

    def get_queryset(self):
        alpha = self.request.GET.get('alpha', '')
        cat = self.request.GET.get('cat', '')
        group = self.request.GET.get('group', '')
        new_context = Marque.objects.all()
        if alpha:
            new_context = Marque.objects.filter(name__istartswith=alpha)
        if group:
            new_context = new_context.filter(categories__group=group)
        if cat:
            new_context = new_context.filter(categories=cat)

        return new_context


class MarqueDetailView(generic.DetailView):
    model = Marque
    template_name = "marque_details.html"
