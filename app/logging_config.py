"""
Configuração de logging
"""
import logging
import sys
from app.config import settings

def setup_logging():
    """Configura o sistema de logging"""
    
    # Nível de log baseado no ambiente
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    
    # Formato de log
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Configura logging
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Reduz log verboso de algumas bibliotecas
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging configurado - Nível: {logging.getLevelName(log_level)}")
    
    return logger
