from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=120)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        verbose_name="Categoría",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    nombre = models.CharField("Nombre", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    descripcion = models.TextField("Descripción", blank=True)
    precio = models.DecimalField("Precio", max_digits=12, decimal_places=2)
    imagen = models.ImageField("Imagen", upload_to="productos/", blank=True, null=True)
    activo = models.BooleanField("Activo", default=True)
    creado = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado"]

    def __str__(self):
        return self.nombre
