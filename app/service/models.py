from django.core.exceptions import ValidationError
from django.db import models

from app import settings


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


def get_service_default_order():
    return Service.objects.count() + 1


def get_info_default_order():
    return Info.objects.count() + 1


def get_default_order():
    return Info.objects.count() + 1


class Service(BaseModel):
    title = models.CharField(max_length=100, )
    url = models.CharField(max_length=100, )
    description = models.TextField()
    content = models.TextField()
    icon = models.ImageField(upload_to="./uploads/service/icon")
    background_image = models.ImageField(upload_to="./uploads/service/img")
    principal = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=get_service_default_order)

    def __str__(self):
        return self.title


class Info(BaseModel):
    title = models.CharField(max_length=100, )
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=get_info_default_order)

    def __str__(self):
        return self.title


class Preference(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    icon = models.ImageField(upload_to="./uploads/preference/icon", blank=True, null=True)
    logo = models.ImageField(upload_to="./uploads/preference/logo", blank=True, null=True)
    background_image = models.ImageField(upload_to="./uploads/preference/img", blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    copyright = models.TextField(default="", null=True, blank=True)

    def get_logo(self):
        if self.logo:
            return "{0}{1}".format(settings.MEDIA_URL, self.logo)
        return ""

    def get_icon(self):
        if self.icon:
            return "{0}{1}".format(settings.MEDIA_URL, self.icon)
        return ""

    def get_background_image(self):
        if self.background_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.background_image)
        return ""

    def get_open_hour(self):
        if self.open_hour:
            return self.open_hour.strftime("%Hh%M")
        return ""

    def get_close_hour(self):
        if self.close_hour:
            return self.close_hour.strftime("%Hh%M")
        return ""

    def __str__(self):
        return u"%s" % self.title
