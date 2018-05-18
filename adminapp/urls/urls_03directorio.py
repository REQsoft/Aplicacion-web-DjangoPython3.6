from django.urls import path
from .. views import views_03directorio

urlpatterns = [
    path('directorio/crear', views_03directorio.DirectorioCreateView.as_view(), name='crear-directorio'),
    path('directorio/listar', views_03directorio.DirecotorioListView.as_view(), name='listar-directorios'),
    path('directorio/<int:pk>/editar', views_03directorio.DirectorioUpdateView.as_view(), name='editar-directorio'),
    path('directorio/<int:pk>/eliminar', views_03directorio.DirectorioDeleteView.as_view(), name='eliminar-directorio'),
    path('directorio/', views_03directorio.DirectorioList.as_view(), name='serializers-directorios'),
]