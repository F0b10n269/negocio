from django.contrib import admin

from .models import Categoria, Plato


class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 1
    fields = (
        "nombre",
        "descripcion",
        "precio",
        "disponible",
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    ordering = ("nombre",)
    inlines = [PlatoInline]


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "categoria",
        "precio",
        "disponible",
    )
    list_filter = ("categoria", "disponible")
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


admin.site.site_header = "Administración del restaurante"
admin.site.site_title = "Panel del restaurante"
admin.site.index_title = "Gestión del catálogo"