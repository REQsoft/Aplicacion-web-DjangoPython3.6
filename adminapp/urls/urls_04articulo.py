from django.urls import path
from .. views import views_04articulo

urlpatterns = [
    path('articulo/crear', views_04articulo.ArticuloCreate.as_view(), name='crear-articulo'),
    path('articulo/listar', views_04articulo.listar_articulos, name='listar-articulos'),
    path('articulo/', views_04articulo.ArticuloList.as_view(), name='serializer-articulos'),
]
