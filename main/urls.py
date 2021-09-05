from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Inicio'),
    path('inicio', views.index, name='Inicio'),
    path('analisis/<empresa_param>', views.analisis, name='Analisis'),
    path('analisis_firts', views.analisis_firts, name='Analisis_First'),
    path('bases', views.bases, name='Bases'),
]