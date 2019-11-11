import datetime
from haystack import indexes
from marque.models import Marque


class MarqueIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='name')
    content = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Marque

