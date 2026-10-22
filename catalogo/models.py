from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=80,
        unique=True,
    )
    descripcion = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="platos",
    )
    nombre = models.CharField(
        max_length=120,
    )
    descripcion = models.TextField(
        blank=True,
    )
    precio = models.PositiveIntegerField(
        help_text="Precio en pesos chilenos, sin puntos ni decimales.",
    )
    disponible = models.BooleanField(
        default=True,
    )
    creado = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "plato"
        verbose_name_plural = "platos"

    def __str__(self):
        return self.nombre