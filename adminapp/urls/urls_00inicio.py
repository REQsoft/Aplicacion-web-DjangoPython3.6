from django.urls import path
from .. views import views_00inicio

urlpatterns = [
    path('', views_00inicio.inicio_sesion, name='inicio-sesion'),
]
