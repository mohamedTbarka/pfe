from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Contacts(BaseModel):
    name = models.CharField(max_length=100, )
    email = models.EmailField()
    object = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    content = models.TextField()


class Newsletter(BaseModel):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)
