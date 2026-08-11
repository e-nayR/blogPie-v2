# 🍰🐍 Blog Pie

Projeto de estudos de um Blog para criar e interagir com publicações, categorias e comentários.

## 🚀 Versão 2 — API REST com Django REST Framework

A v2 reescreve o projeto como uma **API REST**: o back-end passa a expor dados em **JSON** e deixa de renderizar HTML. Qualquer front-end (React, mobile, etc.) pode consumir a mesma API.

### ✨ O que mudou / novas implementações
- **Django REST Framework** no lugar dos templates — respostas em **JSON** e API navegável do DRF.
- **ViewSets + Router**: cada recurso é um `ModelViewSet` e o `DefaultRouter` gera automaticamente as rotas de CRUD (`list`, `create`, `retrieve`, `update`, `destroy`).
- **Serializers** para conversão model ⇄ JSON e validação (substituem os Django Forms).
- **Model `User` customizado** (`AUTH_USER_MODEL`), estendendo `AbstractUser` com campos de perfil.
- **PostgreSQL 17** no lugar do SQLite.
- **Docker + Docker Compose** (serviços `web` + `db`) para subir tudo com um comando.
- **Configuração por `.env`** (`python-dotenv`): `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` e credenciais do banco.
- **Permissões e autenticação** do DRF: leitura pública, escrita autenticada; cadastro de usuário público.
- **Upload de mídia** (`ImageField` + `MEDIA_ROOT`) para foto de perfil e imagem das postagens.
- Models organizados por app com `verbose_name` e responsabilidade única.

### 🔀 v1 × v2 em resumo
| Aspecto        | v1                          | v2                                 |
|----------------|-----------------------------|------------------------------------|
| Camada de view | Templates HTML (SSR)        | API REST em JSON                   |
| Views          | Função + `render()`         | `ModelViewSet` + Router            |
| Entrada/saída  | Django Forms + HTML         | Serializers + JSON                 |
| Banco          | SQLite                      | PostgreSQL 17                      |
| Usuário        | `auth.User` padrão          | `accounts.User` customizado        |
| Execução       | `runserver` local           | Docker Compose (`web` + `db`)      |
| Config         | Hardcoded no `settings.py`  | Variáveis de ambiente (`.env`)     |

---

## 🛠️ Tecnologias
- Python 3.13 · Django 5.1 · **Django REST Framework**
- **PostgreSQL 17** · Docker / Docker Compose · Pillow (upload de imagens)

## 📦 Apps
- `accounts` — modelo de **User customizado** (`AUTH_USER_MODEL`)
- `categories` — categorias das postagens
- `posts` — publicações
- `comments` — comentários das publicações

### 👤 Model `User` (accounts)
Estende `AbstractUser` e adiciona os campos solicitados:

| Campo pedido      | Campo no model    | Origem                    |
|-------------------|-------------------|---------------------------|
| nome              | `first_name`      | AbstractUser              |
| sobrenome         | `last_name`       | AbstractUser              |
| idade             | `age`             | customizado               |
| nome de usuário   | `username`        | AbstractUser              |
| cidade            | `city`            | customizado               |
| email             | `email`           | AbstractUser              |
| senha             | `password`        | AbstractUser (com hash)   |
| último login      | `last_login`      | AbstractUser              |
| criado em         | `created_at`      | customizado               |
| atualizado em     | `updated_at`      | customizado               |
| foto de perfil    | `profile_photo`   | customizado (ImageField)  |

## 🔌 Endpoints (base `/api/`)
| Recurso     | Rota                 | ViewSet            |
|-------------|----------------------|--------------------|
| Usuários    | `/api/users/`        | `UserViewSet`      |
| Categorias  | `/api/categories/`   | `CategoryViewSet`  |
| Postagens   | `/api/posts/`        | `PostViewSet`      |
| Comentários | `/api/comments/`     | `CommentViewSet`   |

- Admin do Django: `/admin/`
- Login da API navegável (DRF): `/api-auth/`
- Filtros: `GET /api/posts/?category=<id>` e `GET /api/comments/?post=<id>`
- Permissões: leitura pública; escrita exige autenticação. O **cadastro** de usuário (`POST /api/users/`) é público.

## ▶️ Como rodar (Docker)
1. Crie o `.env` a partir do exemplo:
   ```bash
   cp .env.example .env
   ```
2. Suba a stack (web + Postgres):
   ```bash
   docker compose up --build
   ```
3. Aplique as migrations (primeira execução):
   ```bash
   docker compose run --rm web python manage.py migrate
   ```
4. (Opcional) Crie um superusuário para acessar o `/admin/`:
   ```bash
   docker compose run --rm web python manage.py createsuperuser
   ```

A API fica disponível em `http://localhost:8000/api/`.

## 📋 Funcionalidades
- CRUD de Usuários (cadastro público, foto de perfil)
- CRUD de Publicações
- CRUD de Categorias
- CRUD de Comentários nas Publicações
- Listar Publicações por Categoria

---

## 🧭 Próximos passos / melhorias
Ideias já mapeadas para a evolução do projeto:

- **🔎 Busca semântica com banco vetorial**
  Indexar o conteúdo das postagens como *embeddings* e usar um banco/índice vetorial
  (ex.: **pgvector** no próprio PostgreSQL, ou Qdrant/Weaviate) para permitir busca por
  significado — não apenas por palavra exata como na busca atual (`title__icontains`).
  Ex.: encontrar posts sobre "receitas de sobremesa" mesmo sem essas palavras no texto.

- **❤️ Engajamento**
  Permitir e medir interações dos usuários com as postagens, como curtir, comentar, salvar e compartilhar

- **🌍 Integração com API externa de endereços/localização**
  Consumir uma API externa para popular e validar **cidade, estado e país** do usuário
  (ex.: IBGE para cidades/estados do Brasil, REST Countries para países, ou ViaCEP para
  autocompletar endereço por CEP), evitando digitação livre e padronizando os dados de perfil.

> Outras ideias naturais na sequência: autenticação por **Token/JWT**, testes automatizados,
> paginação/filtros mais ricos e documentação com **OpenAPI/Swagger**.
