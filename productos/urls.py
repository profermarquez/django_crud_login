from django.urls import path
from . import views

from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
path('carrito/agregar/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
path('carrito/eliminar/<int:pk>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),


]
