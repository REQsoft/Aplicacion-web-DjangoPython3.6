from django.urls import path
from .. views import views_05georeferenciacion

urlpatterns = [
    path('georeferenciacion/crear', views_05georeferenciacion.crear_localizacion, name='crear-localizacion'),
    path('georeferenciacion/listar', views_05georeferenciacion.listar_localizaciones, name='listar-localizaciones'),
    path('georeferenciacion/', views_05georeferenciacion.LocalizacionList.as_view(), name='serializer-localizaciones'),
]