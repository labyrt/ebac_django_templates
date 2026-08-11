# Meu Blog — Django Templates

Projeto desenvolvido para o exercício de Django da EBAC. A aplicação usa
herança de templates para apresentar a lista de posts, o detalhe de cada post e
uma barra lateral reutilizável.

## Tecnologias

- Python 3.12
- Django 5.2 LTS
- pytest
- pytest-django
- SQLite

## Preparação do ambiente

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python manage.py migrate
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`.

## Executar o projeto

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.

## Executar os testes

```bash
pytest
```

Os testes automatizados validam o modelo `Post`, a listagem somente de posts
publicados, a página de detalhes e os templates compartilhados.
