from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Promotion(BaseModel):
    title = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="./uploads/promotion/img")
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Event(BaseModel):
    title = models.CharField(max_length=100, )
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/event/img")

    def get_badge(self):
        if timezone.now < self.start_date:
            return u"A venir"
        elif self.start_date <= timezone.now <= self.end_date:
            return u"En cours"
        else:
            return "Achevé"

    def __str__(self):
        return self.title


class Compagne(BaseModel):
    title = models.CharField(max_length=100, )
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/compagne/img")

    def __str__(self):
        return self.title


class Display(BaseModel):
    image = models.ImageField(upload_to="./uploads/gallery/display/img")
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Gallery(BaseModel):
    name = models.CharField(max_length=100, )
    # image = models.ImageField(upload_to="./uploads/gallery/img")
    displays = models.ManyToManyField(Display)

    def __str__(self):
        return self.name
