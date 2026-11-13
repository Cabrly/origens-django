from django.contrib import admin
from .models import Artista, Comunidade, Evento, Exposicao, Obra


@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "povo", "estado", "municipio", "visibilidade", "demonstracao", "ativo")
    search_fields = ("nome", "povo", "municipio")
    list_filter = ("estado", "visibilidade", "demonstracao", "ativo")


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome_artistico", "categoria", "comunidade", "demonstracao", "ativo")
    search_fields = ("nome_artistico",)
    list_filter = ("categoria", "demonstracao", "ativo")


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "comunidade", "data", "gratuito", "publicado")
    list_filter = ("tipo", "gratuito", "publicado", "demonstracao")
    search_fields = ("titulo", "local_publico")


admin.site.register(Obra)
admin.site.register(Exposicao)
