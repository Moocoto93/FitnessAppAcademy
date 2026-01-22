"""
Script para inicializar dados no banco de dados em produção
Executa automaticamente quando a API inicia
"""
import os
import logging
import json
from pathlib import Path
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import Usuario, Exercicio
from app.auth import get_password_hash

logger = logging.getLogger(__name__)

def init_db_on_startup():
    """Inicializa o banco de dados na primeira execução"""
    db: Session = SessionLocal()
    
    try:
        # Verifica se já tem usuários
        admin_exists = db.query(Usuario).filter(Usuario.username == "admin").first()
        exercicios_count = db.query(Exercicio).count()
        
        if admin_exists and exercicios_count > 0:
            logger.info(f"✓ Banco já inicializado. {exercicios_count} exercícios encontrados.")
            return
        
        logger.info("🔧 Inicializando banco de dados...")
        
        # Cria usuário admin se não existir
        if not admin_exists:
            logger.info("👤 Criando usuário admin...")
            admin_user = Usuario(
                username="admin",
                senha_hash=get_password_hash("admin"),
                is_admin=1
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            logger.info("✓ Usuário admin criado")
        
        # Popula exercícios se não existirem
        if exercicios_count == 0:
            logger.info("💪 Carregando exercícios...")
            
            try:
                # Tenta carregar do arquivo JSON
                exercicios_data = load_exercicios_from_file()
                
                if exercicios_data:
                    # Insere os exercícios
                    for ex_data in exercicios_data:
                        # Mapeia os campos conforme o modelo Exercicio
                        exercicio = Exercicio(
                            nome=ex_data.get("nome", ""),
                            descricao=ex_data.get("descricao", ""),
                            musculos=ex_data.get("musculos", []),  # JSON com lista de músculos
                            equipamento=ex_data.get("equipamento", ""),
                            categoria=ex_data.get("categoria", ""),
                            dificuldade=ex_data.get("dificuldade", "intermediaria"),
                            link_execucao=ex_data.get("link_execucao", "")
                        )
                        db.add(exercicio)
                    
                    db.commit()
                    count = db.query(Exercicio).count()
                    logger.info(f"✓ {count} exercícios carregados com sucesso!")
                else:
                    logger.warning("⚠ Nenhum exercício foi carregado")
            
            except Exception as e:
                logger.error(f"❌ Erro ao carregar exercícios: {e}", exc_info=True)
                db.rollback()
        else:
            logger.info(f"✓ {exercicios_count} exercícios já existem no banco")
        
        logger.info("✅ Banco de dados inicializado com sucesso!")
    
    except Exception as e:
        logger.error(f"❌ Erro ao inicializar banco: {e}", exc_info=True)
        db.rollback()
    
    finally:
        db.close()


def load_exercicios_from_file():
    """Carrega exercícios do arquivo JSON"""
    
    # Tenta diferentes caminhos possíveis
    possible_paths = [
        "exercicios_academia.json",
        "./exercicios_academia.json",
        Path(__file__).parent.parent / "exercicios_academia.json",
        Path(__file__).parent.parent.parent / "exercicios_academia.json",
    ]
    
    for path in possible_paths:
        try:
            if isinstance(path, Path):
                path_str = str(path)
            else:
                path_str = path
            
            if os.path.exists(path_str):
                logger.info(f"📂 Carregando JSON de: {path_str}")
                with open(path_str, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # Trata diferentes formatos de JSON
                if isinstance(data, dict):
                    if "exercicios" in data:
                        return data["exercicios"]
                    elif "data" in data:
                        return data["data"]
                    else:
                        return list(data.values()) if data else []
                elif isinstance(data, list):
                    return data
                else:
                    return []
        
        except Exception as e:
            logger.debug(f"⚠ Erro ao carregar de {path}: {e}")
            continue
    
    logger.warning("⚠ Arquivo exercicios_academia.json não encontrado em nenhum caminho")
    return None

