# -*- coding: utf-8 -*-


class SourceMediumMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET.get("utm_source"):
            request.session["utm_source"] = request.GET.get("utm_source")
        if request.GET.get("utm_medium"):
            request.session["utm_medium"] = request.GET.get("utm_medium")
        if request.GET.get("utm_campaign"):
            request.session["utm_campaign"] = request.GET.get("utm_campaign")
        response = self.get_response(request)

        return response