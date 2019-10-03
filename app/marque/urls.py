from django.urls import path

from marque import views

urlpatterns = [
    path('marques', views.MarqueListView.as_view(), name='marques'),
    path('marque/<int:pk>/', views.MarqueDetailView.as_view(), name='marque_detail'),

]