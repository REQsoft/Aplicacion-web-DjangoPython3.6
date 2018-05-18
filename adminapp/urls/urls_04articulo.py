from django.urls import path
from .. views import views_04articulo

urlpatterns = [
    path('articulo/crear', views_04articulo.ArticuloCreate.as_view(), name='crear-articulo'),
    path('articulo/listar', views_04articulo.ArticuloListView.as_view(), name='listar-articulos'),
    path('articulo/<int:pk>/editar', views_04articulo.ArticuloUpdate.as_view(), name='editar-articulo'),
    path('articulo/<int:pk>/eliminar', views_04articulo.ArticuloDeleteView.as_view(), name='eliminar-articulo'),
    path('articulo/', views_04articulo.ArticuloList.as_view(), name='serializer-articulos'),
]
