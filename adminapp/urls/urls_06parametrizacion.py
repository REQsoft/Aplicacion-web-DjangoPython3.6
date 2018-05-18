from django.urls import path
from .. views import views_06parametrizacion

urlpatterns = [
    path('parametrizacion/crear', views_06parametrizacion.ParametrizacionCreateView.as_view(), name='crear-parametrizacion'), 
    path('parametrizacion/listar', views_06parametrizacion.ParametrizacionListView.as_view(), name='listar-parametrizaciones'),
    path('parametrizacion/<int:pk>/editar', views_06parametrizacion.ParametrizacionUpdate.as_view(), name='editar-parametrizacion'),
    path('parametrizacion/<int:pk>/eliminar', views_06parametrizacion.ParametrizacionDeleteView.as_view(), name='eliminar-parametrizacion'),
    path('parametrizacion/', views_06parametrizacion.ParametrizacionList.as_view(), name='serializer-parametrizaciones'),
]