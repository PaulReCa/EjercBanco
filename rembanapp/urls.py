from django.urls import path
from . import views

app_name = 'rembanapp'
urlpatterns = [
    path('', views.IndexViewUsuarios.as_view(), name='indexUsuarios'),
    path('<int:pk>/', views.DetailViewUsuarios.as_view(), name='detailUsuarios'),
]