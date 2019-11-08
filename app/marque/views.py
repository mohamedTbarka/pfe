import string

from django.db.models import Q
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
        cat = self.request.GET.get('cat', '')
        group = self.request.GET.get('group', '')

        for alpha in alphas:
            alpha_dict = {'key': alpha, "value": Marque.objects.filter(name__istartswith=alpha, ).exists()}
            if group or cat:
                alpha_dict = {'key': alpha, "value": Marque.objects.filter(name__istartswith=alpha, ).filter(
                    Q(categories__pk__in=cat) | Q(categories__group__pk__in=group)).exists()}
            alphabet.append(alpha_dict)

        alpha = self.request.GET.get('alpha', '')

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
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
