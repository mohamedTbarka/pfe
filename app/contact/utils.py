# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from app.settings import SUPPORT_EMAIL, DEFAULT_FROM_EMAIL


def send(instance):
    """get Send instance created to send this email """

    email_template_name = "email_template.html"
    sujet = instance.object
    context = {}

    try:
        context.update({"name": instance.name})
        context.update({"email": instance.email})
        context.update({"phone": instance.phone})
        context.update({"object": instance.object})
        context.update({"content": instance.content})
    except:
        pass

    email = SUPPORT_EMAIL
    from_email = DEFAULT_FROM_EMAIL
    # try:
    msg_html = render_to_string(email_template_name, context=context)
    msg = EmailMessage(sujet,
                       msg_html,
                       from_email,
                       email
                       )
    msg.content_subtype = "html"

    # except Exception as exception1:
    #     # instance.status = 500
    #     # instance.description = exception1
    #     # instance.save()
    #     return
    print("test")
    s = msg.send()
    print(s)
    # try:
    #
    #     s = msg.send()
    #     print (s)
    #     # instance.status = s
    #     # instance.save()
    #
    # except Exception as exception2:
    #     # instance.status = 500
    #     # instance.description = exception2
    #     # instance.save()
    #     return
