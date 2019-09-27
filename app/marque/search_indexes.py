import datetime
from haystack import indexes

from marque.models import Marque


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='name')
    body = indexes.CharField(model_attr='content')

    def get_model(self):
        return Marque

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
