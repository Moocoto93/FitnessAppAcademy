# Fitness App Academy API

API completa para gerenciamento de exercícios de academia com autenticação JWT e painel administrativo.

## 🚀 Características

- ✅ Autenticação JWT com Bearer Token
- ✅ Painel administrativo para CRUD de exercícios
- ✅ Banco de dados SQLite embutido
- ✅ 500 exercícios pré-cadastrados
- ✅ API RESTful completa
- ✅ Documentação automática (Swagger/OpenAPI)
- ✅ Pronta para deploy no RapidAPI

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Configuração

### 1. Clone ou baixe o projeto

```bash
cd FitnessAppAcademy
```

### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicialize o banco de dados

```bash
python init_db.py
```

Este script irá:
- Criar o banco de dados SQLite (`fitness_app.db`)
- Criar o usuário admin (username: `admin`, password: `admin`)
- Popular o banco com os 500 exercícios do arquivo JSON

### 5. Inicie o servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após iniciar o servidor, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Autenticação

### Login

**Endpoint:** `POST /api/auth/login`

**Body:**
```json
{
  "username": "admin",
  "password": "admin"
}
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "username": "admin",
  "is_admin": true
}
```

### Usar o Token

Para acessar rotas protegidas, inclua o token no header:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## 📡 Endpoints Principais

### Públicos (sem autenticação)

- `GET /api/exercicios` - Lista todos os exercícios
- `GET /api/exercicios/{id}` - Obtém um exercício específico
- `GET /api/exercicios/categoria/{categoria}` - Lista por categoria

**Parâmetros de query:**
- `skip`: Número de registros para pular (padrão: 0)
- `limit`: Número máximo de registros (padrão: 100, máx: 500)
- `categoria`: Filtrar por categoria
- `dificuldade`: Filtrar por dificuldade
- `search`: Buscar por nome ou descrição

**Exemplo:**
```
GET /api/exercicios?categoria=Peito&limit=10
GET /api/exercicios?search=supino&dificuldade=Intermediário
```

### Administrativos (requer autenticação)

- `POST /api/exercicios` - Criar novo exercício
- `PUT /api/exercicios/{id}` - Atualizar exercício
- `DELETE /api/exercicios/{id}` - Deletar exercício
- `POST /api/exercicios/bulk` - Criar múltiplos exercícios
- `GET /api/admin/stats` - Estatísticas do sistema

## 📝 Exemplos de Uso

### Criar um exercício (Admin)

```bash
curl -X POST "http://localhost:8000/api/exercicios" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Agachamento Livre",
    "descricao": "Exercício fundamental para pernas",
    "musculos": ["Quadríceps", "Glúteos"],
    "equipamento": "Nenhum",
    "categoria": "Pernas",
    "dificuldade": "Intermediário",
    "link_execucao": "https://www.youtube.com/watch?v=..."
  }'
```

### Listar exercícios

```bash
curl "http://localhost:8000/api/exercicios?categoria=Peito&limit=5"
```

### Atualizar exercício (Admin)

```bash
curl -X PUT "http://localhost:8000/api/exercicios/1" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "descricao": "Nova descrição atualizada"
  }'
```

## 🌐 Publicar no RapidAPI

### Passo 1: Preparar para Produção

1. **Altere a SECRET_KEY** em `app/auth.py` para uma chave segura:
```python
SECRET_KEY = "sua-chave-super-secreta-aqui-mude-isso"
```

2. **Configure CORS** adequadamente em `main.py` se necessário

### Passo 2: Deploy da API

Você pode usar várias opções:

#### Opção A: Heroku (Gratuito)

1. Crie uma conta em [Heroku](https://www.heroku.com)
2. Instale o Heroku CLI
3. Crie arquivo `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```
4. Deploy:
```bash
heroku create sua-api-fitness
git push heroku main
```

#### Opção B: Railway (Gratuito)

1. Crie conta em [Railway](https://railway.app)
2. Conecte seu repositório GitHub
3. Configure o comando de start: `uvicorn main:app --host 0.0.0.0 --port $PORT`

#### Opção C: Render (Gratuito)

1. Crie conta em [Render](https://render.com)
2. Crie novo Web Service
3. Configure:
   - Build Command: `pip install -r requirements.txt && python init_db.py`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

#### Opção D: PythonAnywhere

1. Crie conta em [PythonAnywhere](https://www.pythonanywhere.com)
2. Faça upload dos arquivos
3. Configure o WSGI

### Passo 3: Publicar no RapidAPI

1. **Acesse RapidAPI Provider Portal**
   - Vá para: https://rapidapi.com/provider
   - Faça login ou crie uma conta

2. **Crie uma Nova API**
   - Clique em "Add New API"
   - Preencha:
     - **Name**: Fitness App Academy
     - **Description**: API completa para gerenciamento de exercícios de academia
     - **Category**: Health & Fitness
     - **Base URL**: Sua URL de produção (ex: https://sua-api.herokuapp.com)

3. **Configure os Endpoints**
   - RapidAPI irá escanear automaticamente sua API se ela tiver documentação OpenAPI
   - Ou adicione manualmente os endpoints principais

4. **Configure Preços**
   - Defina planos (Free, Basic, Pro, etc.)
   - Configure limites de requisições

5. **Teste e Publique**
   - Teste todos os endpoints
   - Publique a API

### Passo 4: Documentação Adicional

Adicione um arquivo `rapidapi-info.md` com informações para o RapidAPI:

```markdown
# Fitness App Academy API

## Descrição
API completa para gerenciamento de exercícios de academia com 500+ exercícios pré-cadastrados.

## Autenticação
Use Bearer Token obtido através do endpoint /api/auth/login

## Endpoints Principais
- GET /api/exercicios - Lista exercícios
- GET /api/exercicios/{id} - Detalhes do exercício
- POST /api/exercicios - Criar exercício (admin)
```

## 🗂️ Estrutura do Projeto

```
FitnessAppAcademy/
├── app/
│   ├── __init__.py
│   ├── database.py          # Configuração do banco
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Schemas Pydantic
│   ├── auth.py              # Utilitários JWT
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Rotas de autenticação
│       ├── exercicios.py     # Rotas de exercícios
│       └── admin.py         # Rotas administrativas
├── main.py                  # Aplicação principal
├── init_db.py              # Script de inicialização
├── requirements.txt        # Dependências
├── exercicios_academia.json # Dados dos exercícios
└── README.md               # Este arquivo
```

## 🔒 Segurança

- ✅ Senhas são hasheadas com bcrypt
- ✅ Tokens JWT com expiração
- ✅ Rotas administrativas protegidas
- ⚠️ **IMPORTANTE**: Altere a SECRET_KEY em produção!

## 📊 Banco de Dados

O banco de dados SQLite (`fitness_app.db`) contém:

- **Tabela `usuarios`**: Usuários do sistema
- **Tabela `exercicios`**: Exercícios cadastrados

## 🛠️ Desenvolvimento

### Executar em modo desenvolvimento

```bash
uvicorn main:app --reload
```

### Resetar banco de dados

```bash
# Delete o arquivo fitness_app.db e execute novamente:
python init_db.py
```

## 📄 Licença

Este projeto está disponível para uso comercial.

## 🤝 Suporte

Para dúvidas ou problemas, consulte a documentação em `/docs` ou entre em contato.

---

**Desenvolvido com ❤️ para Fitness App Academy**
