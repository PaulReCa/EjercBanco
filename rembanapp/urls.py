from django.urls import path
from . import views

app_name = 'rembanapp'
urlpatterns = [
    path('', views.main, name='main'),
    path('indexUsuarios/', views.IndexViewUsuarios.as_view(), name='indexUsuarios'),
    path('indexOrdenes/', views.IndexViewOrdenes.as_view(), name='indexOrdenes'),
    path('detailUsuarios/<int:pk>/', views.DetailViewUsuarios.as_view(), name='detailUsuarios'),
    path('detailOrdenes/<int:pk>/', views.DetailViewOrdenes.as_view(), name='detailOrdenes'),
]