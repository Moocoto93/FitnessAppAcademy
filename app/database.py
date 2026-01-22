"""
Configuração do banco de dados
Suporta SQLite (dev) e PostgreSQL (produção)
Compatível com Render, Railway, Heroku, etc.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
import os

# Detecta se está em produção (Render, Railway, Heroku)
DATABASE_URL = os.getenv("DATABASE_URL")  # Variável padrão de plataformas cloud

if DATABASE_URL:
    # PostgreSQL em produção (Render, Railway, Heroku)
    # DATABASE_URL já vem no formato: postgresql://user:pass@host:port/db
    # Mas pode precisar ajustar para postgresql:// se vier como postgres://
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verifica conexões antes de usar
        pool_size=10,
        max_overflow=20
    )
elif settings.DB_TYPE == "postgresql":
    # PostgreSQL configurado manualmente
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )
else:
    # SQLite - para desenvolvimento
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

# Cria SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependency para obter DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
