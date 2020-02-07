import uuid
from datetime import timedelta

from django.db import models
from django.db.models.signals import post_save
from django.utils.timezone import now

from saintv.signals import signal_create_ticket_image


class SaintVBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u"Date création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u"Date dernière mise à jour")

    class Meta:
        abstract = True


class Participant(SaintVBaseModel):
    full_name = models.CharField(max_length=255, verbose_name=u"Nom et prénom")
    email = models.CharField(max_length=255, )
    telephone = models.CharField(max_length=255, )

    def is_allowed_to_participate(self):
        partcipations = self.participant_participations.filter(created_at__gte=(now() - timedelta(hours=24)))
        if partcipations:
            return False
        return True

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Participants"


class Question(SaintVBaseModel):
    question = models.TextField()

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name_plural = "Question"


class Response(SaintVBaseModel):
    response = models.TextField(verbose_name=u"Réponse")
    is_True = models.BooleanField(default=False, verbose_name=u"Vrais?")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name=u"question_responses")

    def __str__(self):
        return "%s" % self.response

    class Meta:
        verbose_name_plural = "Réponses"


class Participation(SaintVBaseModel):
    hash_code = models.UUIDField(max_length=255, default=uuid.uuid4, null=True, blank=True, verbose_name=u"Hash code",
                                 editable=False)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name=u"participant_participations")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name=u"question_participations")
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name=u"response_participations",
                                 verbose_name=u"Réponse", null=True, blank=True)
    ticket = models.ImageField(upload_to="./tickets", blank=True, null=True)
    ticket_base64 = models.TextField(blank=True, null=True, editable=False)
    source = models.CharField(max_length=355, verbose_name=(u"Source"), null=True, blank=True)
    medium = models.CharField(max_length=355, verbose_name=(u"Medium"), null=True, blank=True)
    campaign = models.CharField(max_length=355, verbose_name=(u"Campaign"), null=True, blank=True)

    def __str__(self):
        return "%s" % self.pk

    class Meta:
        verbose_name_plural = "Participations"


post_save.connect(signal_create_ticket_image, sender=Participation)
