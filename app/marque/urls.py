from django.urls import path

from marque import views

urlpatterns = [
    path('marques/', views.MarqueListView.as_view, name='marques'),

]
