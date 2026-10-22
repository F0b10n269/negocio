from django.shortcuts import get_object_or_404, render

from .models import Categoria, Plato


def inicio(request):
    platos = (
        Plato.objects
        .select_related("categoria")
        .filter(disponible=True)
    )

    contexto = {
        "platos": platos,
        "categorias": Categoria.objects.all(),
    }

    return render(
        request,
        "catalogo/inicio.html",
        contexto,
    )


def detalle(request, id):
    plato = get_object_or_404(
        Plato.objects.select_related("categoria"),
        id=id,
        disponible=True,
    )

    return render(
        request,
        "catalogo/detalle.html",
        {"plato": plato},
    )