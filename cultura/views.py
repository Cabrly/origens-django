from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Artista, Comunidade, Evento, Exposicao


def home(request):
    comunidades = Comunidade.objects.filter(
        ativo=True,
        visibilidade=Comunidade.Visibilidade.PUBLICO
    )[:6]
    eventos = Evento.objects.filter(publicado=True).select_related("comunidade")[:6]
    artistas = Artista.objects.filter(ativo=True).select_related("comunidade")[:6]
    exposicoes = Exposicao.objects.filter(publicada=True).select_related("comunidade")[:4]

    return render(request, "cultura/home.html", {
        "comunidades": comunidades,
        "eventos": eventos,
        "artistas": artistas,
        "exposicoes": exposicoes,
        "total_comunidades": Comunidade.objects.filter(
            ativo=True,
            visibilidade=Comunidade.Visibilidade.PUBLICO
        ).count(),
        "total_eventos": Evento.objects.filter(publicado=True).count(),
        "total_artistas": Artista.objects.filter(ativo=True).count(),
        "total_exposicoes": Exposicao.objects.filter(publicada=True).count(),
    })


def comunidades(request):
    termo = request.GET.get("q", "").strip()
    lista = Comunidade.objects.filter(
        ativo=True,
        visibilidade=Comunidade.Visibilidade.PUBLICO
    )

    if termo:
        lista = lista.filter(
            Q(nome__icontains=termo) |
            Q(povo__icontains=termo) |
            Q(municipio__icontains=termo)
        )

    return render(request, "cultura/comunidades.html", {
        "comunidades": lista,
        "termo": termo
    })


def comunidade_detalhe(request, pk):
    comunidade = get_object_or_404(
        Comunidade,
        pk=pk,
        ativo=True,
        visibilidade=Comunidade.Visibilidade.PUBLICO
    )
    return render(request, "cultura/comunidade_detalhe.html", {
        "comunidade": comunidade,
        "artistas": comunidade.artistas.filter(ativo=True),
        "eventos": comunidade.eventos.filter(publicado=True),
        "exposicoes": comunidade.exposicoes.filter(publicada=True),
    })


def eventos(request):
    return render(request, "cultura/eventos.html", {
        "eventos": Evento.objects.filter(publicado=True).select_related("comunidade")
    })


def artistas(request):
    return render(request, "cultura/artistas.html", {
        "artistas": Artista.objects.filter(ativo=True).select_related("comunidade")
    })


def exposicoes(request):
    return render(request, "cultura/exposicoes.html", {
        "exposicoes": Exposicao.objects.filter(publicada=True).select_related("comunidade")
    })
