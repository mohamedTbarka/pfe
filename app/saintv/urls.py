from django.urls import path

from saintv.views import CreateParticipantAPIView, ParticipateAPIView

urlpatterns = [
    path('sinscrire/', CreateParticipantAPIView.as_view(), name='sinscrire'),
    path('participate/', ParticipateAPIView.as_view(), name='participate'),

]
