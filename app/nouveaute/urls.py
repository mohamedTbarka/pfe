from django.urls import path

from nouveaute import views

urlpatterns = [
    path('evenements/', views.EventListView.as_view(), name='evenements'),
    path('promotions/', views.PromotionListView.as_view(), name='promotions'),
    path('galerie/', views.CompagneListView.as_view(), name='compagnes'),
    path('evenement/<slug>/', views.EventDetailView.as_view(), name='event_detail'),
    path('promotion/<slug>/', views.PromotionDetailView.as_view(), name='promotion_detail'),
    path('galerie/<slug>/', views.CompagneDetailView.as_view(), name='compagne_detail'),
    path('nouveautes/', views.NouveauteList.as_view(), name='nouveautes'),

]
