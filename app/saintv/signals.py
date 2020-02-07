# -*- coding: utf-8 -*-
import base64
import os

from django.core.files.base import ContentFile
from django.utils.text import slugify

from app import settings


def signal_create_ticket_image(sender, instance=None, created=False, **kwargs):
    """
    """
    if created:
        pass
        # if instance.ticket_base64:
        #     filename = 'ticket_%s_%s.png' % (slugify(instance.participant.full_name), instance.pk)
        #     path__photo = os.path.join(settings.MEDIA_ROOT)
        #     fh = open(os.path.join(path__photo, filename), "wb")
        #     decoded_image = base64.b64decode(instance.ticket_base64)
        #     fh.write(decoded_image)
        #     fh.close()
        #     image = ContentFile(decoded_image, filename)
        #     sender.objects.filter(pk=instance.pk) \
        #         .update(ticket=image)
