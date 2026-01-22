# 🚀 Guia de Deploy - Fitness App Academy API

## ⚡ Deploy Rápido (5 minutos)

### Render.com (Recomendado)

1. **Acesse**: https://render.com
2. **Crie conta** gratuita
3. **New +** → **Web Service**
4. **Conecte repositório** GitHub
5. **Configure**:
   - **Name**: `fitness-app-academy`
   - **Build Command**: `pip install -r requirements.txt && python init_db.py`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Environment Variables**:
   ```
   ENVIRONMENT=production
   DB_TYPE=sqlite
   SECRET_KEY=<gere-comando-abaixo>
   ```
7. **Deploy** e aguarde 5-10 minutos

### Gerar SECRET_KEY

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## 🐳 Deploy com Docker

### Build e Run Local

```bash
docker build -t fitness-app-academy .
docker run -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e SECRET_KEY=sua-chave-aqui \
  fitness-app-academy
```

### Docker Compose (com PostgreSQL)

```bash
docker-compose up -d
```

## 📦 Deploy em Produção

### Variáveis de Ambiente Necessárias

```bash
ENVIRONMENT=production
DB_TYPE=sqlite  # ou postgresql
SECRET_KEY=<chave-aleatoria-gerada>
DEBUG=False
```

### Para PostgreSQL

```bash
DB_TYPE=postgresql
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fitness_app
```

## ✅ Verificar Deploy

1. **Health Check**: `https://sua-api.com/health`
2. **Documentação**: `https://sua-api.com/docs`
3. **API Info**: `https://sua-api.com/api/info`

## 🔒 Segurança em Produção

1. ✅ Altere `SECRET_KEY`
2. ✅ Configure `CORS_ORIGINS` se necessário
3. ✅ Use HTTPS
4. ✅ Monitore logs
5. ✅ Configure rate limiting (se necessário)

## 📊 Monitoramento

- **Uptime Robot**: Monitora `/health`
- **Logs**: Verifique na plataforma de deploy
- **Métricas**: Response time, error rate

---

**Pronto para produção! 🎉**
