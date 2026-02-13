from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Producto, Categoria


def lista_productos(request):
    texto = request.GET.get("q", "").strip()
    categoria_slug = request.GET.get("categoria", "").strip()

    productos = Producto.objects.filter(activo=True).select_related("categoria")

    if texto:
        productos = productos.filter(
            Q(nombre__icontains=texto) |
            Q(descripcion__icontains=texto)
        )

    if categoria_slug:
        productos = productos.filter(categoria__slug=categoria_slug)

    categorias = Categoria.objects.all()

    return render(request, "tienda/lista_productos.html", {
        "productos": productos,
        "categorias": categorias,
        "texto": texto,
        "categoria_actual": categoria_slug,
    })


def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, activo=True)
    return render(request, "tienda/detalle_producto.html", {
        "producto": producto
    })
