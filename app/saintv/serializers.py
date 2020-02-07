# -*- coding: utf-8 -*-

import base64

from django.db.models import Q
from rest_framework import serializers, status

from saintv.models import Participant, Response, Question, Participation
from saintv.validators import CustomValidation


class CreateParticipantSerializer(serializers.ModelSerializer):
    ticket_base64 = serializers.CharField(required=False, allow_blank=True)
    ticket = serializers.ImageField(read_only=True)

    class Meta:
        model = Participant
        fields = ("full_name", "email", "telephone", "ticket_base64", "ticket")

    def validate(self, data):
        participant = Participant.objects.filter(Q(telephone=data["telephone"]) | Q(email=data["email"])).last()
        if participant:
            if not participant.is_allowed_to_participate():
                raise CustomValidation("detail", "406_not_allowed_participant", status.HTTP_406_NOT_ACCEPTABLE)
        if "ticket_base64" in data and data["ticket_base64"]:
            try:
                decoded_image = base64.b64decode(data["ticket_base64"])
                # data["ticket"] = decoded_image
            except:
                raise CustomValidation("detail", "406_invalide_Foto", status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        return data


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ("id", "response",)


class QuestionSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(source="question_responses", many=True,
                                   read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question", "responses")


class ParticipateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hash_code = serializers.CharField(allow_blank=False, max_length=155)

    def validate(self, data):
        participation = Participation.objects.filter(hash_code=data.get('hash_code')).last()
        response = Response.objects.filter(pk=data.get('id')).last()

        if not participation:
            raise CustomValidation("detail", "404_prarticipation", status.HTTP_404_NOT_FOUND)
        if not response:
            raise CustomValidation("detail", "404_response", status.HTTP_404_NOT_FOUND)

        return data
