from django.urls import path

from service import views

urlpatterns = [
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('decouvrir/', views.DiscoverListView.as_view(), name='discovers'),
    path('hotel/', views.HotelListView.as_view(), name='hotels'),
    path('bureau/', views.BureauListView.as_view(), name='bureaux'),
    path('plan/', views.Plan.as_view(), name='plan'),
    path('navigator/', views.Navigator.as_view(), name='navigator'),


]
