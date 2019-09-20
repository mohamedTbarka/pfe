from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Contact(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    content = models.TextField()


class Newsletter(BaseModel):
    email = models.EmailField(unique=True)
    subscribe = models.BooleanField(default=True)
