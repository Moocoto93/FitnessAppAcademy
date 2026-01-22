"""
Configurações da aplicação
Suporta variáveis de ambiente para produção
"""
import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configurações da aplicação"""
    
    # API
    API_TITLE: str = "Fitness App Academy API"
    API_VERSION: str = "2.0.0"
    API_DESCRIPTION: str = "API profissional para gestão de exercícios de academia com 500+ exercícios pré-cadastrados"
    
    # Database
    DATABASE_URL: Optional[str] = None
    DB_TYPE: str = os.getenv("DB_TYPE", "sqlite")  # sqlite ou postgresql
    
    # JWT
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", 
        "fitness-app-academy-secret-key-2024-CHANGE-IN-PRODUCTION-USE-RANDOM-KEY"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 horas
    
    # CORS
    CORS_ORIGINS: list = ["*"]  # Em produção, especifique domínios
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # development ou production
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # RapidAPI
    RAPIDAPI_KEY: Optional[str] = os.getenv("RAPIDAPI_KEY", None)
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Instância global de configurações
settings = Settings()

# Configura URL do banco baseado no tipo
if settings.DATABASE_URL is None:
    if settings.DB_TYPE == "postgresql":
        # PostgreSQL (para produção)
        db_user = os.getenv("DB_USER", "postgres")
        db_password = os.getenv("DB_PASSWORD", "")
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("DB_NAME", "fitness_app")
        settings.DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    else:
        # SQLite (para desenvolvimento)
        settings.DATABASE_URL = "sqlite:///./fitness_app.db"
