"""
Script para inicializar dados no banco de dados em produção
Executa automaticamente quando a API inicia
"""
import os
import logging
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import Usuario, Exercicio
from app.auth import get_password_hash
import json

logger = logging.getLogger(__name__)

def init_db_on_startup():
    """Inicializa o banco de dados na primeira execução"""
    db: Session = SessionLocal()
    
    try:
        # Verifica se já tem usuários
        admin_exists = db.query(Usuario).filter(Usuario.username == "admin").first()
        
        if admin_exists:
            logger.info("✓ Admin já existe no banco. Pulando inicialização.")
            return
        
        logger.info("🔧 Inicializando banco de dados...")
        
        # Cria usuário admin
        logger.info("👤 Criando usuário admin...")
        admin_user = Usuario(
            username="admin",
            email="admin@fitnessapp.com",
            nome="Administrador",
            senha_hash=get_password_hash("admin"),
            is_admin=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        logger.info("✓ Usuário admin criado")
        
        # Popula exercícios
        logger.info("💪 Carregando exercícios...")
        
        # Tenta carregar do arquivo JSON
        try:
            exercicios_file = "exercicios_academia.json"
            if os.path.exists(exercicios_file):
                with open(exercicios_file, "r", encoding="utf-8") as f:
                    exercicios_data = json.load(f)
                
                if isinstance(exercicios_data, dict) and "exercicios" in exercicios_data:
                    exercicios_list = exercicios_data["exercicios"]
                else:
                    exercicios_list = exercicios_data if isinstance(exercicios_data, list) else []
                
                for ex_data in exercicios_list[:500]:  # Limita a 500
                    exercicio = Exercicio(
                        nome=ex_data.get("nome", ""),
                        descricao=ex_data.get("descricao", ""),
                        grupo_muscular=ex_data.get("grupo_muscular", ""),
                        dificuldade=ex_data.get("dificuldade", "intermediaria"),
                        imagem_url=ex_data.get("imagem_url", ""),
                        video_url=ex_data.get("video_url", ""),
                        series=ex_data.get("series", 3),
                        repeticoes=ex_data.get("repeticoes", 10)
                    )
                    db.add(exercicio)
                
                db.commit()
                count = len(exercicios_list)
                logger.info(f"✓ {count} exercícios carregados com sucesso")
            else:
                logger.warning("⚠ Arquivo exercicios_academia.json não encontrado")
        
        except Exception as e:
            logger.error(f"❌ Erro ao carregar exercícios: {e}")
            db.rollback()
        
        logger.info("✅ Banco de dados inicializado com sucesso!")
    
    except Exception as e:
        logger.error(f"❌ Erro ao inicializar banco: {e}")
        db.rollback()
    
    finally:
        db.close()
