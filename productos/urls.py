from django.urls import path


from .views import (
    landing_page,
    lista_productos,
    agregar_producto,
    editar_producto,
    eliminar_producto,
    ver_carrito,
    agregar_al_carrito,
    eliminar_del_carrito,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)


app_name = 'productos'  # Para usar el namespace

urlpatterns = [
    path('', landing_page, name='landing'),  # Ruta para la landing page
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:pk>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:pk>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),
]