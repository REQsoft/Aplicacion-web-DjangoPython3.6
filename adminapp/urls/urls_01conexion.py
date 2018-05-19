from django.urls import path
from .. views import views_01conexion

urlpatterns = [
    path('conexion/', views_01conexion.base_conexion, name='base-conexion'),
    path('conexion/validar', views_01conexion.validar_conexion, name='validar-conexion'),
    path('conexion/crear', views_01conexion.ConexionCreateView.as_view(), name='crear-conexion'),
    path('conexion/<int:pk>/aditar', views_01conexion.ConexionUpdateView.as_view(), name='editar-conexion'),
    path('conexion/listar', views_01conexion.ConexionListView.as_view(), name='listar-conexiones'),
    path('conexion/<int:pk>/eliminar', views_01conexion.ConexionDeleteView.as_view(), name='eliminar-conexion'),
    path('conexion/listar_bd', views_01conexion.listar_bd, name='listar-bd'),
]
