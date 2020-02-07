# -*- coding: utf-8 -*-

import base64

from django.core.files.base import ContentFile


def base64_file(data, name=None):
    # _format, _img_str = data.split(';base64,')
    # _name, ext = _format.split('/')
    # if not name:
    #     name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(data), name='{}.{}'.format(name, "png"))
