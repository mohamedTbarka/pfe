import datetime
from haystack import indexes

from marque.models import Marque


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Marque

