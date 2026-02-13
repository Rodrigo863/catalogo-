from django.urls import path
from .views import lista_productos, detalle_producto

app_name = "tienda"

urlpatterns = [
    path("", lista_productos, name="lista_productos"),
    path("producto/<slug:slug>/", detalle_producto, name="detalle_producto"),
]
