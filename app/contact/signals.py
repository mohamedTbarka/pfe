# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from app.settings import USE_SEND_EMAIL
from contact.models import Contacts
from contact.threads import SendEmailhread
from contact.utils import send


@receiver(post_save, sender=Contacts)
def send_email(sender, instance, created, **kwargs):
    if created:
        if USE_SEND_EMAIL:
            thread_1 = SendEmailhread(instance)
            thread_1.start()



