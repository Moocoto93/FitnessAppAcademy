"""
Fitness App Academy API
API completa com autenticação JWT e gerenciamento de exercícios
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import auth, exercicios, admin

# Cria as tabelas apenas fora de produção
if os.getenv("ENVIRONMENT") != "production":
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness App Academy API",
    description="API profissional para gestão de treinos e exercícios com autenticação JWT",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(exercicios.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {
        "message": "Fitness App Academy API",
        "version": "2.0.0",
        "docs": "/docs",
        "endpoints": {
            "autenticacao": "/api/auth/login",
            "exercicios": "/api/exercicios",
            "admin": "/api/admin"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
