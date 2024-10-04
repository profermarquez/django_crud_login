from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

# Vista para la landing page
def landing_page(request):
    productos = Producto.objects.all()
    return render(request, 'productos/landing.html', {'productos': productos})

# Listado de productos
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

# Agregar producto
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

# Editar producto
@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

# Eliminar producto
@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

from .models import ItemCarrito

@login_required
def agregar_al_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    item, created = ItemCarrito.objects.get_or_create(usuario=request.user, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('landing_page')

@login_required
def ver_carrito(request):
    items = ItemCarrito.objects.filter(usuario=request.user)
    return render(request, 'productos/carrito.html', {'items': items})

@login_required
def eliminar_del_carrito(request, pk):
    item = get_object_or_404(ItemCarrito, pk=pk, usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

# productos/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

# Lista de productos (se muestra en la landing page)
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/landing.html'
    context_object_name = 'productos'

# Crear producto
@method_decorator(login_required, name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:landing')

# Actualizar producto
@method_decorator(login_required, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:landing')

# Eliminar producto
@method_decorator(login_required, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('productos:landing')
