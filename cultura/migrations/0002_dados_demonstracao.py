from datetime import date, time
from django.db import migrations


def criar_dados_demo(apps, schema_editor):
    Comunidade = apps.get_model("cultura", "Comunidade")
    Artista = apps.get_model("cultura", "Artista")
    Obra = apps.get_model("cultura", "Obra")
    Exposicao = apps.get_model("cultura", "Exposicao")
    Evento = apps.get_model("cultura", "Evento")

    comunidades = [
        {
            "nome": "Comunidade Cultural Araguaia",
            "povo": "Perfil demonstrativo",
            "estado": "TO",
            "municipio": "Tocantínia",
            "localizacao_publica": "Região central do Tocantins",
            "descricao": "Comunidade fictícia criada para demonstrar como a plataforma pode reunir memória, arte, eventos e informações culturais em um único espaço.",
            "historia": "Este perfil é exclusivamente demonstrativo. Em uma implantação real, a própria comunidade ou seus representantes autorizados escolheriam quais informações publicar.",
            "idiomas": "Português e língua tradicional (demonstração)",
        },
        {
            "nome": "Comunidade Cultural do Cerrado",
            "povo": "Perfil demonstrativo",
            "estado": "TO",
            "municipio": "Palmas",
            "localizacao_publica": "Palmas e região",
            "descricao": "Espaço fictício de divulgação de música, artesanato, pintura, oficinas e encontros culturais.",
            "historia": "Perfil de demonstração voltado a visualizar recursos de agenda cultural, artistas e exposições.",
            "idiomas": "Português (demonstração)",
        },
        {
            "nome": "Comunidade Rio Vivo",
            "povo": "Perfil demonstrativo",
            "estado": "TO",
            "municipio": "Lagoa da Confusão",
            "localizacao_publica": "Região sudoeste do Tocantins",
            "descricao": "Comunidade fictícia usada para apresentar ações ligadas a território, memória, narrativas e produção artística.",
            "historia": "Os conteúdos deste perfil são fictícios e existem apenas para preencher o protótipo.",
            "idiomas": "Português e língua tradicional (demonstração)",
        },
        {
            "nome": "Comunidade Caminhos da Mata",
            "povo": "Perfil demonstrativo",
            "estado": "PA",
            "municipio": "Conceição do Araguaia",
            "localizacao_publica": "Região do Araguaia",
            "descricao": "Perfil fictício com foco em fotografia, narrativas visuais, rodas de conversa e oficinas culturais.",
            "historia": "Criada como exemplo para demonstrar conexão entre comunidades de diferentes regiões.",
            "idiomas": "Português (demonstração)",
        },
        {
            "nome": "Comunidade Memória das Águas",
            "povo": "Perfil demonstrativo",
            "estado": "GO",
            "municipio": "São Miguel do Araguaia",
            "localizacao_publica": "Região norte de Goiás",
            "descricao": "Comunidade fictícia dedicada, neste protótipo, à literatura oral, música e preservação de memórias culturais.",
            "historia": "Perfil demonstrativo sem correspondência com uma comunidade real específica.",
            "idiomas": "Português (demonstração)",
        },
    ]

    criadas = {}
    for item in comunidades:
        obj = Comunidade.objects.create(
            **item,
            visibilidade="publico",
            ativo=True,
            demonstracao=True,
        )
        criadas[item["nome"]] = obj

    artistas_info = [
        ("Aritana", "artesanato", "Comunidade Cultural Araguaia", "Produção artística fictícia inspirada em materiais naturais, memória e identidade cultural."),
        ("Yara", "pintura", "Comunidade Cultural Araguaia", "Artista visual fictícia que trabalha com território, memória e narrativas culturais."),
        ("Kauê", "musica", "Comunidade Cultural do Cerrado", "Músico fictício participante de encontros, apresentações e atividades culturais."),
        ("Maíra", "fotografia", "Comunidade Caminhos da Mata", "Fotógrafa fictícia dedicada a registrar paisagens, cotidiano e expressões culturais."),
        ("Jaci", "literatura", "Comunidade Memória das Águas", "Autora fictícia ligada a narrativas orais, memória coletiva e criação literária."),
        ("Raoni", "audiovisual", "Comunidade Rio Vivo", "Produtor audiovisual fictício que trabalha com pequenos documentários e registros culturais."),
        ("Potira", "danca", "Comunidade Cultural do Cerrado", "Artista fictícia de dança e performances coletivas em encontros culturais."),
        ("Ubirã", "artesanato", "Comunidade Rio Vivo", "Artesão fictício com trabalhos demonstrativos em fibras, formas e texturas."),
    ]

    artistas = {}
    for nome, categoria, comunidade_nome, bio in artistas_info:
        obj = Artista.objects.create(
            nome_artistico=nome,
            categoria=categoria,
            comunidade=criadas[comunidade_nome],
            bio=bio,
            contato_publico="Contato demonstrativo pela plataforma",
            ativo=True,
            demonstracao=True,
        )
        artistas[nome] = obj

    obras_info = [
        ("Tramas do Cerrado", "Aritana", "Peça demonstrativa inspirada em texturas e formas do cerrado.", 2026),
        ("Caminhos de Terra", "Yara", "Pintura fictícia sobre deslocamento, memória e paisagem.", 2026),
        ("Vozes do Horizonte", "Kauê", "Composição musical fictícia criada para a demonstração.", 2026),
        ("Entre Rios", "Maíra", "Série fotográfica fictícia sobre água, caminhos e cotidiano.", 2025),
        ("Memórias Contadas", "Jaci", "Texto demonstrativo inspirado em narrativas de memória coletiva.", 2026),
        ("Território em Movimento", "Raoni", "Curta audiovisual fictício sobre cultura e território.", 2026),
        ("Passos da Terra", "Potira", "Performance fictícia desenvolvida para encontros culturais.", 2026),
        ("Fibras e Formas", "Ubirã", "Conjunto artesanal fictício para apresentação do catálogo.", 2026),
        ("Cores do Encontro", "Yara", "Pintura fictícia voltada ao encontro entre gerações.", 2026),
        ("Água que Guarda Histórias", "Maíra", "Fotografia fictícia para uma mostra digital.", 2026),
        ("Cantos de Memória", "Kauê", "Peça musical fictícia dedicada à memória comunitária.", 2026),
        ("Palavras da Noite", "Jaci", "Narrativa fictícia apresentada em formato de leitura coletiva.", 2026),
    ]

    obras = {}
    for titulo, artista_nome, descricao, ano in obras_info:
        obj = Obra.objects.create(
            titulo=titulo,
            artista=artistas[artista_nome],
            descricao=descricao,
            ano=ano,
            publica=True,
            demonstracao=True,
        )
        obras[titulo] = obj

    exposicoes_info = [
        (
            "Cores da Terra",
            "Comunidade Cultural Araguaia",
            "Exposição virtual fictícia reunindo pinturas, artesanato e produções inspiradas na relação entre memória e território.",
            date(2026, 9, 1),
            date(2026, 10, 30),
            True,
            ["Tramas do Cerrado", "Caminhos de Terra", "Cores do Encontro"],
        ),
        (
            "Entre Fios e Memórias",
            "Comunidade Rio Vivo",
            "Mostra fictícia de artesanato e trabalhos produzidos por artistas participantes da plataforma.",
            date(2026, 9, 15),
            date(2026, 11, 15),
            False,
            ["Fibras e Formas", "Território em Movimento"],
        ),
        (
            "Vozes do Cerrado",
            "Comunidade Cultural do Cerrado",
            "Exposição audiovisual fictícia dedicada à música, performance e memórias coletivas.",
            date(2026, 10, 3),
            date(2026, 12, 10),
            True,
            ["Vozes do Horizonte", "Passos da Terra", "Cantos de Memória"],
        ),
        (
            "Águas que Contam",
            "Comunidade Memória das Águas",
            "Galeria digital fictícia com fotografia, literatura e relatos de memória.",
            date(2026, 10, 20),
            date(2027, 1, 20),
            True,
            ["Água que Guarda Histórias", "Memórias Contadas", "Palavras da Noite"],
        ),
    ]

    for titulo, comunidade_nome, descricao, inicio, fim, virtual, titulos_obras in exposicoes_info:
        expo = Exposicao.objects.create(
            titulo=titulo,
            comunidade=criadas[comunidade_nome],
            descricao=descricao,
            data_inicio=inicio,
            data_fim=fim,
            virtual=virtual,
            publicada=True,
            demonstracao=True,
        )
        expo.obras.add(*[obras[t] for t in titulos_obras])

    eventos_info = [
        ("Feira de Arte e Saberes", "Comunidade Cultural Araguaia", "feira", "Feira cultural fictícia com exposição de produções, apresentações e atividades abertas ao público.", date(2026, 9, 12), time(17, 0), "Centro Cultural — Tocantínia/TO"),
        ("Encontro de Música e Memória", "Comunidade Cultural do Cerrado", "encontro", "Encontro fictício com música, conversa e compartilhamento de histórias.", date(2026, 9, 20), time(19, 0), "Espaço Cultural — Palmas/TO"),
        ("Oficina de Criação Visual", "Comunidade Rio Vivo", "oficina", "Oficina demonstrativa voltada a desenho, pintura e criação de narrativas visuais.", date(2026, 10, 3), time(14, 0), "Local público informado pela comunidade"),
        ("Mostra Vozes da Terra", "Comunidade Cultural do Cerrado", "apresentacao", "Apresentação fictícia de música, dança e produções audiovisuais.", date(2026, 10, 17), time(18, 30), "Auditório cultural — Palmas/TO"),
        ("Roda de Histórias", "Comunidade Memória das Águas", "palestra", "Roda de conversa fictícia sobre memória, narrativas e transmissão cultural entre gerações.", date(2026, 11, 7), time(16, 0), "Espaço comunitário público"),
        ("Festival Cultural do Cerrado", "Comunidade Caminhos da Mata", "encontro", "Evento fictício reunindo artistas, exposições, oficinas e apresentações culturais.", date(2026, 11, 21), time(15, 0), "Praça cultural — região do Araguaia"),
    ]

    for titulo, comunidade_nome, tipo, descricao, data_evento, horario, local in eventos_info:
        Evento.objects.create(
            titulo=titulo,
            comunidade=criadas[comunidade_nome],
            tipo=tipo,
            descricao=descricao,
            data=data_evento,
            horario=horario,
            local_publico=local,
            gratuito=True,
            publicado=True,
            demonstracao=True,
        )


def remover_dados_demo(apps, schema_editor):
    Comunidade = apps.get_model("cultura", "Comunidade")
    Comunidade.objects.filter(demonstracao=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cultura", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(criar_dados_demo, remover_dados_demo),
    ]
