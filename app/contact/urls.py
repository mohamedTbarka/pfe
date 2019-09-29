from django.urls import path, include
from rest_framework import routers

from contact import views

router = routers.DefaultRouter()

"""Adding tokens"""
router.register(r'subscribe', views.SubscribeAPIView)
router.register(r'contact_us', views.ContactAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', views.Contact.as_view(), name="contact"),

]
