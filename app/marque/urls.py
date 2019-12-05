from django.urls import path

from marque import views

urlpatterns = [
    path('marques', views.MarqueListView.as_view(), name='marques'),
    # path('marques/<group>', views.MarqueListView.as_view(), name='marques'),
    # path('marques/<group>/<cat>', views.MarqueListView.as_view(), name='marques'),
    path('marque/<slug>/', views.MarqueDetailView.as_view(), name='marque_detail'),

]
