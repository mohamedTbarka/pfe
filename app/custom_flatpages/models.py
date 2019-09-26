# coding=utf-8
from django.db import models
import os

from app import settings

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
templates = os.listdir(here("templates/flatpages/"))


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Gallery(BaseModel):
    name = models.CharField(max_length=100, )

    # image = models.ImageField(upload_to="./uploads/gallery/img")

    def __str__(self):
        return self.name


class Display(BaseModel):
    image = models.ImageField(upload_to="./uploads/images/flatepages/display/img")
    title = models.CharField(max_length=100, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')

    # def __str__(self):
    #     return self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""


class FlatPage(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    image = models.ImageField(upload_to='./uploads/images/flatepages', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Paragraphe")
    url = models.CharField(verbose_name='URL', max_length=100, )
    order = models.PositiveSmallIntegerField(verbose_name="Ordre", null=True, blank=True)
    template_name = models.CharField(verbose_name="templates name",
                                     choices=[(str(templates[i]), str('flatpages/' + templates[i])) for i in
                                              range(len(templates))], max_length=70, blank=True, help_text=(
            "Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ('order',)

    def __str__(self):
        return u'%s' % self.titre

    # def save(self,):
    #     pass

    def get_absolute_url(self):
        return u"%s" % self.url
