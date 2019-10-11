from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from app import settings
from service.validators import minimum_size


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
    url = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to="./uploads/service/icon")
    background_image = models.ImageField(upload_to="./uploads/service/img", null=True, blank=True)
    principal = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=get_service_default_order)
    old_principal = None

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.old_principal = self.principal

    def get_icon_url(self):
        if self.icon:
            return "{0}{1}".format(settings.MEDIA_URL, self.icon)
        return ""

    def get_background_image_url(self):
        if self.background_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.background_image)
        return ""

    def save(self, *args, **kwargs):
        if self.old_principal != self.principal and self.principal:
            Service.objects.all().update(principal=False)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk, })


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
    background_image2 = models.ImageField(upload_to="./uploads/preference/img", blank=True, null=True)
    parallax_mobile_image = models.ImageField(upload_to="./uploads/preference/img", blank=True, null=True)
    parallax_mobile_image2 = models.ImageField(upload_to="./uploads/preference/img", blank=True, null=True)
    rdc = models.ImageField(upload_to="./uploads/preference/img/plan", blank=True, null=True)
    first_floor = models.ImageField(upload_to="./uploads/preference/img/plan", blank=True, null=True)
    second_floor = models.ImageField(upload_to="./uploads/preference/img/plan", blank=True, null=True)
    bureau_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    hotel_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    decouvrir_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    compagne_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    event_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    promotion_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    nouveautes_banner = models.ImageField(upload_to="./uploads/preference/img/banner", blank=True, null=True)
    shopping_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    restauration_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    cinema_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    culture_loisirs_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    hypermarche_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    promotion_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    event_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    compagne_image = models.ImageField(upload_to="./uploads/preference/img/", blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    youtube = models.CharField(max_length=250, null=True, blank=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    copyright = models.TextField(default="", null=True, blank=True)

    def clean(self):
        # Then call the clean() method of the super  class
        cleaned_data = super(Preference, self).clean()
        # ... do some cross-fields validation for the subclass
        if self.promotion_image:
            minimum_size(self.promotion_image, 275, 350)
        if self.event_image:
            minimum_size(self.event_image, 275, 350)
        if self.compagne_image:
            minimum_size(self.compagne_image, 575, 350)
        # Finally, return the cleaned_data
        return cleaned_data

    def get_promotion_image(self):
        if self.promotion_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.promotion_image)
        return ""

    def get_compagne_image(self):
        if self.compagne_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.compagne_image)
        return ""

    def get_event_image(self):
        if self.event_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.event_image)
        return ""

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

    def get_background_image2(self):
        if self.background_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.background_image2)
        return ""

    def get_parallax_mobile_image(self):
        if self.parallax_mobile_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.parallax_mobile_image)
        return ""

    def get_parallax_mobile_image2(self):
        if self.parallax_mobile_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.parallax_mobile_image2)
        return ""

    def get_rdc_image(self):
        if self.rdc:
            return "{0}{1}".format(settings.MEDIA_URL, self.rdc)
        return ""

    def get_1st_floor_image(self):
        if self.first_floor:
            return "{0}{1}".format(settings.MEDIA_URL, self.first_floor)
        return ""

    def get_2nd_floor_image(self):
        if self.second_floor:
            return "{0}{1}".format(settings.MEDIA_URL, self.second_floor)
        return ""

    def get_bureau_banner_image(self):
        if self.bureau_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.bureau_banner)
        return ""

    def get_hotel_banner_image(self):
        if self.hotel_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.hotel_banner)
        return ""

    def get_decouvrir_banner_image(self):
        if self.decouvrir_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.decouvrir_banner)
        return ""

    def get_compagne_banner_image(self):
        if self.compagne_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.compagne_banner)
        return ""

    def get_event_banner_image(self):
        if self.event_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.event_banner)
        return ""

    def get_promotion_banner_image(self):
        if self.promotion_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.promotion_banner)
        return ""

    def get_nouveautes_banner_image(self):
        if self.nouveautes_banner:
            return "{0}{1}".format(settings.MEDIA_URL, self.nouveautes_banner)
        return ""

    def get_shopping_image(self):
        if self.shopping_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.shopping_image)
        return ""

    def get_restauration_image(self):
        if self.restauration_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.restauration_image)
        return ""

    def get_cinema_image(self):
        if self.cinema_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.cinema_image)
        return ""

    def get_culture_loisirs_image(self):
        if self.culture_loisirs_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.culture_loisirs_image)
        return ""

    def get_hypermarche_image(self):
        if self.hypermarche_image:
            return "{0}{1}".format(settings.MEDIA_URL, self.hypermarche_image)
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


class Slider(BaseModel):
    image = models.ImageField(upload_to="./uploads/slider/img",
                              help_text=u'width>=1600px height>=600px ratio:"height/width"≍0.3')
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    url_text = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    def clean(self):
        # Then call the clean() method of the super  class
        cleaned_data = super(Slider, self).clean()
        # ... do some cross-fields validation for the subclass
        width = 1600
        height = 600
        if self.image:
            minimum_size(self.image, width, height)
        # Finally, return the cleaned_data
        return cleaned_data


class Discover(BaseModel):
    image = models.ImageField(upload_to="./uploads/discover/img")
    title = models.CharField(max_length=100, )
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"%s" % self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""


class Hotel(BaseModel):
    image = models.ImageField(upload_to="./uploads/hotel/img")
    title = models.CharField(max_length=100, )
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"%s" % self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    class Meta:
        verbose_name_plural = u'Hôtels'
        verbose_name = u'Hôtel'


class Bureau(BaseModel):
    image = models.ImageField(upload_to="./uploads/bureau/img")
    title = models.CharField(max_length=100, )
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"%s" % self.title

    def get_image_url(self):
        if self.image:
            return "{0}{1}".format(settings.MEDIA_URL, self.image)
        return ""

    class Meta:
        verbose_name_plural = u'Bureaux'
