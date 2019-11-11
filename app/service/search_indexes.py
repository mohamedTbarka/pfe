import datetime
from haystack import indexes

from service.models import Service


class ServiceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Service
