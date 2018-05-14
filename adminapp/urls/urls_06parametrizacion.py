from django.urls import path
from .. views import views_06parametrizacion

urlpatterns = [
    path('parametrizacion/listar', views_06parametrizacion.listar_parametrizaciones, name='listar-parametrizaciones'),
    path('parametrizacion/', views_06parametrizacion.ParametrizacionList.as_view(), name='serializer-parametrizaciones'),
]