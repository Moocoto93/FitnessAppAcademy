# 🚀 Guia Rápido - Fitness App Academy API

## ⚡ Início Rápido (5 minutos)

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Inicializar banco de dados
```bash
python init_db.py
```

### 3. Iniciar servidor
```bash
uvicorn main:app --reload
```

### 4. Acessar documentação
Abra no navegador: http://localhost:8000/docs

## 🔑 Credenciais Padrão

- **Username**: `admin`
- **Password**: `admin`

## 📝 Teste Rápido

### 1. Fazer Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}'
```

Copie o `access_token` da resposta.

### 2. Listar Exercícios
```bash
curl "http://localhost:8000/api/exercicios?limit=5"
```

### 3. Criar Exercício (Admin)
```bash
curl -X POST "http://localhost:8000/api/exercicios" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Teste",
    "categoria": "Teste",
    "descricao": "Exercício de teste"
  }'
```

## 🌐 Publicar no RapidAPI - Passo a Passo

### Passo 1: Deploy da API

**Opção mais fácil - Render.com (Gratuito):**

1. Acesse: https://render.com
2. Crie uma conta gratuita
3. Clique em "New +" → "Web Service"
4. Conecte seu repositório GitHub (ou faça upload)
5. Configure:
   - **Name**: fitness-app-academy
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python init_db.py`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Clique em "Create Web Service"
7. Aguarde o deploy (5-10 minutos)
8. Copie a URL: `https://fitness-app-academy.onrender.com`

### Passo 2: Publicar no RapidAPI

1. **Acesse RapidAPI Provider**
   - Vá para: https://rapidapi.com/provider
   - Faça login ou crie conta

2. **Adicione Nova API**
   - Clique em "Add New API"
   - Preencha:
     - **Name**: Fitness App Academy
     - **Description**: API completa com 500+ exercícios de academia
     - **Category**: Health & Fitness
     - **Base URL**: Sua URL do Render (ex: https://fitness-app-academy.onrender.com)
     - **API Type**: REST

3. **Configure Endpoints**
   - RapidAPI pode escanear automaticamente via OpenAPI
   - Ou adicione manualmente:
     - `POST /api/auth/login` - Autenticação
     - `GET /api/exercicios` - Listar exercícios
     - `GET /api/exercicios/{id}` - Obter exercício
     - `POST /api/exercicios` - Criar exercício (admin)
     - `PUT /api/exercicios/{id}` - Atualizar (admin)
     - `DELETE /api/exercicios/{id}` - Deletar (admin)

4. **Configure Preços**
   - **Free Plan**: 100 requisições/dia
   - **Basic Plan**: 1.000 requisições/dia - $5/mês
   - **Pro Plan**: 10.000 requisições/dia - $20/mês
   - **Ultra Plan**: Ilimitado - $50/mês

5. **Teste e Publique**
   - Teste cada endpoint
   - Adicione exemplos de uso
   - Publique a API

### Passo 3: Documentação Adicional

Adicione na descrição da API:

```
# Fitness App Academy API

## Sobre
API RESTful completa para gerenciamento de exercícios de academia com 500+ exercícios pré-cadastrados.

## Autenticação
1. Faça login em POST /api/auth/login com:
   - username: admin
   - password: admin
2. Use o token retornado no header: Authorization: Bearer {token}

## Endpoints Principais
- GET /api/exercicios - Lista todos os exercícios (público)
- GET /api/exercicios/{id} - Detalhes de um exercício (público)
- POST /api/exercicios - Criar exercício (admin)
- PUT /api/exercicios/{id} - Atualizar exercício (admin)
- DELETE /api/exercicios/{id} - Deletar exercício (admin)

## Filtros
- ?categoria=Peito - Filtrar por categoria
- ?dificuldade=Intermediário - Filtrar por dificuldade
- ?search=supino - Buscar por nome
- ?limit=10&skip=0 - Paginação
```

## 💰 Monetização

### Estratégia de Preços Sugerida

1. **Free Tier**: 100 requisições/dia
   - Acesso básico para testes

2. **Starter**: $5/mês - 1.000 requisições/dia
   - Para apps pequenos

3. **Business**: $20/mês - 10.000 requisições/dia
   - Para apps médios

4. **Enterprise**: $50/mês - Ilimitado
   - Para apps grandes

### Dicas de Marketing

- Adicione tags: fitness, gym, workout, exercises, health
- Crie exemplos de código em múltiplas linguagens
- Adicione screenshots da documentação
- Responda rapidamente a perguntas de usuários

## 🔒 Segurança em Produção

⚠️ **IMPORTANTE**: Antes de publicar, altere:

1. **SECRET_KEY** em `app/auth.py`:
```python
SECRET_KEY = "gere-uma-chave-aleatoria-aqui-com-32-caracteres"
```

2. **Senha do admin**: Crie um script para alterar a senha padrão

3. **CORS**: Configure adequadamente em `main.py` se necessário

## 📊 Monitoramento

Use ferramentas como:
- **Uptime Robot**: Monitorar disponibilidade
- **Sentry**: Monitorar erros
- **Google Analytics**: Acompanhar uso

## ✅ Checklist de Deploy

- [ ] Alterar SECRET_KEY
- [ ] Testar todos os endpoints
- [ ] Configurar CORS adequadamente
- [ ] Fazer deploy em produção
- [ ] Testar URL de produção
- [ ] Adicionar no RapidAPI
- [ ] Configurar preços
- [ ] Adicionar documentação
- [ ] Testar autenticação
- [ ] Publicar API

---

**Boa sorte com sua API! 🚀**
