from django.urls import path

from nouveaute import views

urlpatterns = [
    path('evenements/', views.EventListView.as_view(), name='evenements'),
    path('promotions/', views.PromotionListView.as_view(), name='promotions'),
    path('compagnes/', views.CompagneListView.as_view(), name='compagnes'),
    path('evenement/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('promotion/<int:pk>/', views.PromotionDetailView.as_view(), name='promotion_detail'),
    path('compagne/<int:pk>/', views.CompagneDetailView.as_view(), name='compagne_detail'),

]
