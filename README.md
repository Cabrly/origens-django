# Origens

Protótipo de uma plataforma para dar visibilidade à cultura e à arte de povos indígenas: comunidades, artistas,
obras, exposições e eventos, com um painel administrativo para quem cuida do conteúdo.

Feito em Django, com dados **fictícios** de demonstração, só para visualizar o conceito.

## O que tem

- **Comunidades**, com página de detalhe, idiomas e localização pública (a localização exata nunca aparece).
- **Artistas** por categoria, ligados à comunidade.
- **Obras** e **exposições** (uma exposição reúne várias obras).
- **Eventos**.
- **Admin do Django** configurado para cadastrar e ocultar conteúdo (`visibilidade`, `ativo`, `publica`).
- Dados de exemplo criados por migração (5 comunidades, 8 artistas, 12 obras, 4 exposições, 6 eventos), todos
  marcados com `demonstracao=True` para serem fáceis de remover.

Páginas: `/`, `/comunidades/`, `/comunidades/<id>/`, `/artistas/`, `/exposicoes/`, `/eventos/`, `/admin/`.

## Como rodar

Windows: dê dois cliques em `INICIAR.bat` (cria o ambiente, instala o Django, migra e sobe o servidor).
Para criar o administrador, rode `CRIAR_ADMIN.bat`.

Manualmente:

```bash
python -m venv venv
venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra http://127.0.0.1:8000/

## Estrutura

| Pasta | Papel |
|---|---|
| `config/` | configurações e rotas do projeto |
| `cultura/models.py` | Comunidade, Artista, Obra, Exposição, Evento |
| `cultura/migrations/0002_dados_demonstracao.py` | dados fictícios |
| `cultura/templates/` | páginas |

## Cuidado importante

Todos os nomes, descrições e obras deste protótipo são inventados. Em uso real, dados culturais e localização só
devem ser publicados com autorização e participação da comunidade correspondente.

A `SECRET_KEY` em `config/settings.py` é só de demonstração local. Troque antes de qualquer publicação.
