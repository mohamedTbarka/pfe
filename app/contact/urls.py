from django.urls import path

from contact import views

urlpatterns = [
    path('subscribe', views.SubscribeAPIView().as_view(), name='subscribe'),

]
