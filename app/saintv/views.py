import base64
import os

from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response as Response_rest
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from saintv.models import Participant, Participation, Question, Response
from saintv.serializers import CreateParticipantSerializer, ParticipateSerializer, QuestionSerializer


class CreateParticipantAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        source = None
        medium = None
        campaign = None

        serializer = CreateParticipantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response_rest(serializer.errors, status=HTTP_400_BAD_REQUEST)
        data = serializer.data
        full_name = data["full_name"]
        email = data["email"]
        telephone = data["telephone"]

        participant = Participant.objects.filter(Q(telephone=telephone) | Q(email=email)).last()
        if not participant:
            participant = Participant.objects.create(full_name=full_name, telephone=telephone, email=email)

        if "ticket_base64" in data:
            ticket_base64 = data["ticket_base64"]
            
        if "utm_source" in self.request.session:
            source = self.request.session.get("utm_source")
        if "utm_medium" in self.request.session:
            medium = self.request.session.get("utm_medium")
        if "utm_campaign" in self.request.session:
            campaign = self.request.session.get("utm_campaign")

        question = Question.objects.last()  #############""
        participation = Participation.objects.create(ticket_base64=ticket_base64, participant=participant,
                                                     question=question,
                                                     source=source, medium=medium, campaign=campaign)

        serializer_question = QuestionSerializer(question)
        question_data = serializer_question.data

        return Response_rest({"hash_code": participation.hash_code, "data": question_data}, status=status.HTTP_200_OK)


class ParticipateAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = ParticipateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response_rest(serializer.errors, status=HTTP_400_BAD_REQUEST)
        data = serializer.data
        id = data["id"]
        hash_code = data["hash_code"]

        participation = Participation.objects.filter(hash_code=hash_code).last()
        response = Response.objects.filter(pk=id).last()
        participation.response = response
        participation.save()

        return Response_rest({"result": "response added"}, status=status.HTTP_200_OK)
