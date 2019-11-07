import datetime
from haystack import indexes
from marque.models import Marque


class MarqueIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    name = indexes.NgramField(model_attr='name')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Marque

