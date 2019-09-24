from django.urls import path

from nouveaute import views

urlpatterns = [
    path('evenements/', views.EventListView.as_view(), name='evenements'),
    path('promotions/', views.PromotionListView.as_view(), name='promotions'),
    path('compagne/', views.CompagneListView.as_view(), name='compagne'),

]
