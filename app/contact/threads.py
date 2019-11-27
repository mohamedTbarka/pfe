# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from threading import Thread

from contact.utils import send


class SendEmailhread(Thread):
    """
    """
    def __init__(self, instance):
        Thread.__init__(self)
        self.instance = instance

    def run(self):
        send(self.instance)
