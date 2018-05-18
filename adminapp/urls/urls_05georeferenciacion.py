from django.urls import path
from .. views import views_05georeferenciacion

urlpatterns = [
    path('georeferenciacion/crear', views_05georeferenciacion.LocalizacionCreateView.as_view(), name='crear-localizacion'),
    path('georeferenciacion/listar', views_05georeferenciacion.LocalizacionListView.as_view(), name='listar-localizaciones'),
    path('georeferenciacion/<int:pk>/editar', views_05georeferenciacion.LocalizacionUpdateView.as_view(), name='editar-localizacion'),
    path('georeferenciacion/<int:pk>/eliminar', views_05georeferenciacion.LocalizacionDeleteView.as_view(), name='eliminar-localizacion'),
    path('georeferenciacion/', views_05georeferenciacion.LocalizacionList.as_view(), name='serializer-localizaciones'),
]