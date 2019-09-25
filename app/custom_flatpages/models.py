# coding=utf-8
from django.db import models
import os

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
templates = os.listdir(here("templates/flatpages/"))


class FlatPage(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Titre")
    image = models.ImageField(upload_to='./uploads/images/flatepages', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Paragraphe")
    url = models.CharField(verbose_name='URL', max_length=100,)
    order = models.PositiveSmallIntegerField(verbose_name="Ordre", null=True, blank=True)
    template_name = models.CharField(verbose_name="templates name",
                                     choices=[(str(templates[i]), str('flatpages/' + templates[i])) for i in
                                              range(len(templates))], max_length=70, blank=True, help_text=(
            "Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))

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
