from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Promotion(BaseModel):
    title = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="./uploads/promotion/img")

    def __str__(self):
        return self.title


class Event(BaseModel):
    title = models.CharField(max_length=100, )
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/event/img")

    def __str__(self):
        return self.title


class Compagne(BaseModel):
    title = models.CharField(max_length=100, )
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to="./uploads/compagne/img")

    def __str__(self):
        return self.title
