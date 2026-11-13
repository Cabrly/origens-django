from django.db import models


class Comunidade(models.Model):
    class Visibilidade(models.TextChoices):
        PUBLICO = "publico", "Público"
        MEMBROS = "membros", "Somente membros"
        RESTRITO = "restrito", "Restrito"

    nome = models.CharField(max_length=120)
    povo = models.CharField(max_length=120, blank=True)
    estado = models.CharField(max_length=2)
    municipio = models.CharField(max_length=120, blank=True)
    localizacao_publica = models.CharField(
        max_length=180,
        blank=True,
        help_text="Use somente localização que a comunidade autorizou divulgar."
    )
    descricao = models.TextField()
    historia = models.TextField(blank=True)
    idiomas = models.CharField(max_length=200, blank=True)
    visibilidade = models.CharField(
        max_length=20,
        choices=Visibilidade.choices,
        default=Visibilidade.PUBLICO
    )
    ativo = models.BooleanField(default=True)
    demonstracao = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Artista(models.Model):
    class Categoria(models.TextChoices):
        MUSICA = "musica", "Música"
        ARTESANATO = "artesanato", "Artesanato"
        PINTURA = "pintura", "Pintura"
        FOTOGRAFIA = "fotografia", "Fotografia"
        LITERATURA = "literatura", "Literatura"
        DANCA = "danca", "Dança"
        AUDIOVISUAL = "audiovisual", "Audiovisual"
        OUTRO = "outro", "Outro"

    nome_artistico = models.CharField(max_length=120)
    comunidade = models.ForeignKey(
        Comunidade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="artistas"
    )
    categoria = models.CharField(max_length=30, choices=Categoria.choices)
    bio = models.TextField()
    contato_publico = models.CharField(max_length=150, blank=True)
    ativo = models.BooleanField(default=True)
    demonstracao = models.BooleanField(default=False)

    class Meta:
        ordering = ["nome_artistico"]

    def __str__(self):
        return self.nome_artistico


class Obra(models.Model):
    titulo = models.CharField(max_length=150)
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="obras"
    )
    descricao = models.TextField(blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)
    publica = models.BooleanField(default=True)
    demonstracao = models.BooleanField(default=False)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Exposicao(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    comunidade = models.ForeignKey(
        Comunidade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="exposicoes"
    )
    obras = models.ManyToManyField(Obra, blank=True, related_name="exposicoes")
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    virtual = models.BooleanField(default=True)
    publicada = models.BooleanField(default=True)
    demonstracao = models.BooleanField(default=False)

    class Meta:
        ordering = ["-data_inicio", "titulo"]

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    class Tipo(models.TextChoices):
        FEIRA = "feira", "Feira cultural"
        OFICINA = "oficina", "Oficina"
        APRESENTACAO = "apresentacao", "Apresentação"
        ENCONTRO = "encontro", "Encontro"
        EXPOSICAO = "exposicao", "Exposição"
        PALESTRA = "palestra", "Palestra / conversa"

    titulo = models.CharField(max_length=150)
    comunidade = models.ForeignKey(
        Comunidade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="eventos"
    )
    tipo = models.CharField(max_length=30, choices=Tipo.choices)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField(null=True, blank=True)
    local_publico = models.CharField(max_length=180)
    gratuito = models.BooleanField(default=True)
    publicado = models.BooleanField(default=True)
    demonstracao = models.BooleanField(default=False)

    class Meta:
        ordering = ["data", "horario"]

    def __str__(self):
        return self.titulo
