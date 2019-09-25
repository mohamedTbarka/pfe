from django.core.exceptions import ValidationError
from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Group(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    backgroud_image = models.ImageField(upload_to="./uploads/group/img", blank=True, null=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    sup_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, )

    class Meta:
        verbose_name_plural = "categories"

    def can_add(self):
        cat = self.sup_category
        while cat:
            if self == cat:
                return False
            else:
                cat = cat.sup_category
        return True

    # def ancestors(self):
    #     cat = self.sup_category
    #     ancestor = "%s" % self.id
    #     while cat:
    #         ancestor = "%s < %s" % (self.id, cat.id)
    #         cat = cat.sup_category
    #     return ancestor

    def clean(self):
        if not self.can_add():
            raise ValidationError("Can't have you as ancestor of yourself")

    def __str__(self):
        return self.name


class Slide(BaseModel):
    # title = models.CharField(max_length=100, )
    # text = models.TextField()
    # link = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="./uploads/marque/slide/img")


class Marque(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="./uploads/marque/img")
    categories = models.ManyToManyField(Category, null=True, blank=True, )
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=15)
    phone_second = models.CharField(max_length=15, null=True, blank=True, )
    email = models.EmailField()
    localisation = models.CharField(max_length=50)
    open_hours = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name
