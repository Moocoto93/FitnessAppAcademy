"""
Fitness App Academy API
API completa com autenticação JWT e gerenciamento de exercícios
Pronta para produção e RapidAPI
"""
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app.routes import auth, exercicios, admin
from app.config import settings
from app.logging_config import setup_logging
from app.middleware import LoggingMiddleware, SecurityHeadersMiddleware
import logging

# Configura logging
logger = setup_logging()

# Importa models para garantir que são registrados
from app.models import Exercicio, Usuario

# Cria as tabelas no banco de dados
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Banco de dados inicializado")
except Exception as e:
    logger.error(f"Erro ao inicializar banco de dados: {e}")

# Inicializa a aplicação FastAPI
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Middlewares
app.add_middleware(LoggingMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handler de exceções global
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handler global para exceções não tratadas"""
    logger.error(f"Erro não tratado: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Ocorreu um erro interno. Por favor, tente novamente mais tarde.",
            "detail": str(exc) if settings.DEBUG else None
        }
    )

# Registra as rotas
app.include_router(auth.router)
app.include_router(exercicios.router)
app.include_router(admin.router)


@app.get("/")
def root():
    """Endpoint raiz"""
    return {
        "message": settings.API_TITLE,
        "version": settings.API_VERSION,
        "docs": "/docs",
        "endpoints": {
            "autenticacao": "/api/auth/login",
            "exercicios": "/api/exercicios",
            "admin": "/api/admin"
        }
    }


@app.get("/health")
def health_check():
    """Endpoint de verificação de saúde"""
    return {
        "status": "healthy",
        "message": "API está funcionando",
        "version": settings.API_VERSION,
        "environment": settings.ENVIRONMENT
    }


@app.get("/api/info")
def api_info():
    """Informações sobre a API"""
    return {
        "name": settings.API_TITLE,
        "version": settings.API_VERSION,
        "description": settings.API_DESCRIPTION,
        "endpoints": {
            "autenticacao": "/api/auth/login",
            "exercicios": "/api/exercicios",
            "admin": "/api/admin",
            "docs": "/docs"
        },
        "features": [
            "Autenticação JWT",
            "500+ exercícios pré-cadastrados",
            "CRUD completo de exercícios",
            "Filtros e busca avançada",
            "Painel administrativo"
        ]
    }
