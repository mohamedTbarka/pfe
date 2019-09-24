from django.urls import path

from nouveaute import views

urlpatterns = [
    path('evenemets/', views.EventListView.as_view, name='evenemets'),
    path('promotions/', views.PromotionListView.as_view, name='promotions'),
    path('compagne/', views.CompagneListView.as_view, name='compagne'),

]
