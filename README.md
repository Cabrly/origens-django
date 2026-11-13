# Origens — Protótipo com dados demonstrativos

Esta versão já inclui dados fictícios que são inseridos automaticamente quando você executa:

```bash
python manage.py migrate
```

## Conteúdo de demonstração

- 5 comunidades fictícias
- 8 artistas fictícios
- 12 obras fictícias
- 4 exposições fictícias
- 6 eventos fictícios

Todos os registros de exemplo possuem o campo `demonstracao=True`.

## Maneira mais fácil de iniciar no Windows

Dê dois cliques em:

`INICIAR.bat`

Na primeira execução ele:

1. cria o ambiente virtual;
2. instala o Django;
3. cria o banco;
4. cadastra automaticamente os dados de demonstração;
5. inicia o servidor.

Depois abra:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Criar usuário administrador

Depois de executar o sistema pelo menos uma vez, dê dois cliques em:

`CRIAR_ADMIN.bat`

A senha não aparece na tela enquanto você digita. Isso é normal.

## Rodar manualmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Observação importante

Os nomes, descrições, artistas, obras e eventos incluídos neste protótipo são fictícios.
Eles servem apenas para visualizar o conceito do software.

Em uma implantação real, dados culturais e localização devem ser publicados somente com
autorização e participação da comunidade correspondente.
