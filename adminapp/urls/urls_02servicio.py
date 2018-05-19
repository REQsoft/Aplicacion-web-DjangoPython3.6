from django.urls import path
from .. views import views_02servicio 

urlpatterns = [
    path('servicios/crear', views_02servicio.SQLCreateView.as_view(), name='crear-servicio'),
    path('servicio/listar', views_02servicio.SQLListView.as_view(), name='listar-servicios'),
    path('servicio/<int:pk>/editar', views_02servicio.SQLUpdateView.as_view(), name='editar-servicio'),
    path('servicio/<int:pk>/eliminar', views_02servicio.ServicioDeleteView.as_view(), name='eliminar-servicio'),
    path('servicio/<int:id_servicio>/', views_02servicio.ServicioList.as_view(), name='serializers-servicios'),
]
