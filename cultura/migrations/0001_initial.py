from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comunidade",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=120)),
                ("povo", models.CharField(blank=True, max_length=120)),
                ("estado", models.CharField(max_length=2)),
                ("municipio", models.CharField(blank=True, max_length=120)),
                ("localizacao_publica", models.CharField(blank=True, help_text="Use somente localização que a comunidade autorizou divulgar.", max_length=180)),
                ("descricao", models.TextField()),
                ("historia", models.TextField(blank=True)),
                ("idiomas", models.CharField(blank=True, max_length=200)),
                ("visibilidade", models.CharField(choices=[("publico", "Público"), ("membros", "Somente membros"), ("restrito", "Restrito")], default="publico", max_length=20)),
                ("ativo", models.BooleanField(default=True)),
                ("demonstracao", models.BooleanField(default=False)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["nome"]},
        ),
        migrations.CreateModel(
            name="Artista",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome_artistico", models.CharField(max_length=120)),
                ("categoria", models.CharField(choices=[("musica", "Música"), ("artesanato", "Artesanato"), ("pintura", "Pintura"), ("fotografia", "Fotografia"), ("literatura", "Literatura"), ("danca", "Dança"), ("audiovisual", "Audiovisual"), ("outro", "Outro")], max_length=30)),
                ("bio", models.TextField()),
                ("contato_publico", models.CharField(blank=True, max_length=150)),
                ("ativo", models.BooleanField(default=True)),
                ("demonstracao", models.BooleanField(default=False)),
                ("comunidade", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="artistas", to="cultura.comunidade")),
            ],
            options={"ordering": ["nome_artistico"]},
        ),
        migrations.CreateModel(
            name="Obra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=150)),
                ("descricao", models.TextField(blank=True)),
                ("ano", models.PositiveIntegerField(blank=True, null=True)),
                ("publica", models.BooleanField(default=True)),
                ("demonstracao", models.BooleanField(default=False)),
                ("artista", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="obras", to="cultura.artista")),
            ],
            options={"ordering": ["titulo"]},
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=150)),
                ("tipo", models.CharField(choices=[("feira", "Feira cultural"), ("oficina", "Oficina"), ("apresentacao", "Apresentação"), ("encontro", "Encontro"), ("exposicao", "Exposição"), ("palestra", "Palestra / conversa")], max_length=30)),
                ("descricao", models.TextField()),
                ("data", models.DateField()),
                ("horario", models.TimeField(blank=True, null=True)),
                ("local_publico", models.CharField(max_length=180)),
                ("gratuito", models.BooleanField(default=True)),
                ("publicado", models.BooleanField(default=True)),
                ("demonstracao", models.BooleanField(default=False)),
                ("comunidade", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="eventos", to="cultura.comunidade")),
            ],
            options={"ordering": ["data", "horario"]},
        ),
        migrations.CreateModel(
            name="Exposicao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=150)),
                ("descricao", models.TextField()),
                ("data_inicio", models.DateField(blank=True, null=True)),
                ("data_fim", models.DateField(blank=True, null=True)),
                ("virtual", models.BooleanField(default=True)),
                ("publicada", models.BooleanField(default=True)),
                ("demonstracao", models.BooleanField(default=False)),
                ("comunidade", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="exposicoes", to="cultura.comunidade")),
                ("obras", models.ManyToManyField(blank=True, related_name="exposicoes", to="cultura.obra")),
            ],
            options={"ordering": ["-data_inicio", "titulo"]},
        ),
    ]
