from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from app import settings


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

    class Meta:
        verbose_name_plural = "Albums"
        verbose_name = "Album"


class Promotion(BaseModel):
    title = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="./uploads/promotion/img")
    content = models.TextField()
    date = models.DateTimeField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=100, unique=True, )

    def clean(self):
        'here we go'
        if self.slug:
            self.slug = slugify(self.slug)
        else:
            self.slug = slugify(self.title)
        super(Promotion, self).clean()

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    def get_absolute_url(self):
        return reverse('promotion_detail', kwargs={'slug': self.slug, })


class Event(BaseModel):
    title = models.CharField(max_length=100, )
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/event/img")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=100, unique=True)

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    def get_badge(self):
        if timezone.now() < self.start_date:
            return u"A venir"
        elif self.start_date <= timezone.now() <= self.end_date:

            return u"En cours"
        else:
            return "Achevé"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug, })

    def clean(self):
        'here we go'
        if self.slug:
            self.slug = slugify(self.slug)
        else:
            self.slug = slugify(self.title)
        super(Event, self).clean()

    class Meta:
        verbose_name_plural = "Événements"
        verbose_name = "Événement"


class Compagne(BaseModel):
    title = models.CharField(max_length=100, )
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/compagne/img")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=100, unique=True)

    def clean(self):
        'here we go'
        if self.slug:
            self.slug = slugify(self.slug)
        else:
            self.slug = slugify(self.title)
        super(Compagne, self).clean()

    def __str__(self):
        return self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    def get_absolute_url(self):
        return reverse('compagne_detail', kwargs={'slug': self.slug, })

    class Meta:
        verbose_name_plural = "Galeries"
        verbose_name = "Galerie"


class Display(BaseModel):
    image = models.ImageField(upload_to="./uploads/gallery/display/img")
    title = models.CharField(max_length=100, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')

    # def __str__(self):
    #     return self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""
