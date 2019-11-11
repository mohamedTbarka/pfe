import datetime
from haystack import indexes

from nouveaute.models import Event, Compagne, Promotion


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Event


class CompagneIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Compagne


class PromotionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='title')
    content = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Promotion
