from django.urls import path
from . import views
from rembanapp.views import UsuarioCreateView

app_name = 'rembanapp'
urlpatterns = [
    path('', views.main, name='main'),
    path('indexUsuarios/', views.IndexViewUsuarios.as_view(), name='indexUsuarios'),
    path('indexOrdenes/', views.IndexViewOrdenes.as_view(), name='indexOrdenes'),
    path('detailUsuarios/<int:pk>/', views.DetailViewUsuarios.as_view(), name='detailUsuarios'),
    path('detailOrdenes/<int:pk>/', views.DetailViewOrdenes.as_view(), name='detailOrdenes'),
    path('usuario_form/', views.UsuarioCreateView.as_view(), name='usuario_form'),
    path('orden_form/', views.OrdenCreateView.as_view(), name='orden_form'),
    path('<int:pk>/usuario_confirm_delete/', views.UsuarioDeleteView.as_view(), name='usuario_confirm_delete'),
    path('<int:pk>/orden_confirm_delete/', views.OrdenDeleteView.as_view(), name='orden_confirm_delete'),
]