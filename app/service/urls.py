from django.urls import path

from service import views

urlpatterns = [
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('decouvrir/', views.DiscoverListView.as_view(), name='discovers'),

]
