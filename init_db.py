"""
Script de inicialização do banco de dados
Cria usuário admin e popula com os 500 exercícios
"""
import json
import os
import time
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models import Usuario, Exercicio
from app.auth import get_password_hash

def init_db():
    """Inicializa o banco de dados"""
    db_file = "fitness_app.db"
    
    # Remove banco antigo se existir (para garantir estrutura correta)
    if os.path.exists(db_file):
        print("⚠ Banco de dados antigo encontrado. Removendo para recriar...")
        try:
            # Fecha todas as conexões existentes
            engine.dispose()
            # Aguarda um pouco para garantir que o arquivo foi liberado
            time.sleep(0.5)
            os.remove(db_file)
            print("✓ Banco antigo removido")
        except PermissionError:
            print("⚠ Erro: O banco está em uso. Feche todas as conexões e tente novamente.")
            print("  Ou delete manualmente o arquivo 'fitness_app.db' e execute novamente.")
            return
        except Exception as e:
            print(f"⚠ Aviso: Não foi possível remover banco antigo: {e}")
            print("  Tentando continuar mesmo assim...")
    
    # Cria todas as tabelas (drop_all primeiro para garantir estrutura limpa)
    print("📦 Criando estrutura do banco de dados...")
    try:
        Base.metadata.drop_all(bind=engine)  # Remove tabelas antigas
    except Exception as e:
        print(f"⚠ Aviso ao remover tabelas antigas: {e}")
    
    Base.metadata.create_all(bind=engine)  # Cria tabelas novas
    print("✓ Tabelas criadas com sucesso")
    
    db: Session = SessionLocal()
    
    try:
        # Cria usuário admin
        print("👤 Criando usuário admin...")
        admin_user = Usuario(
            username="admin",
            senha_hash=get_password_hash("admin"),
            is_admin=1
        )
        db.add(admin_user)
        db.commit()
        print("✓ Usuário admin criado (username: admin, password: admin)")
        
        # Carrega exercícios do JSON
        print("📚 Carregando exercícios...")
        exercicios_count = 0
        try:
            with open("exercicios_academia.json", "r", encoding="utf-8") as f:
                exercicios_data = json.load(f)
            
            # Insere exercícios no banco
            print(f"  Inserindo {len(exercicios_data)} exercícios...")
            for i, ex_data in enumerate(exercicios_data, 1):
                exercicio = Exercicio(
                    id=ex_data.get("id"),
                    nome=ex_data.get("nome", ""),
                    descricao=ex_data.get("descricao"),
                    musculos=ex_data.get("musculos", []),
                    equipamento=ex_data.get("equipamento"),
                    categoria=ex_data.get("categoria", ""),
                    dificuldade=ex_data.get("dificuldade"),
                    link_execucao=ex_data.get("link_execucao")
                )
                db.add(exercicio)
                
                # Commit a cada 100 exercícios para melhor performance
                if i % 100 == 0:
                    db.commit()
                    print(f"  ✓ {i}/{len(exercicios_data)} exercícios inseridos...")
            
            db.commit()
            exercicios_count = len(exercicios_data)
            print(f"✓ {exercicios_count} exercícios inseridos no banco de dados")
        except FileNotFoundError:
            print("⚠ Arquivo exercicios_academia.json não encontrado")
            print("  O banco será criado, mas sem exercícios iniciais")
        except Exception as e:
            print(f"⚠ Erro ao carregar exercícios: {e}")
            db.rollback()
        
        print("\n✅ Inicialização concluída com sucesso!")
        print("\n📋 Credenciais de acesso:")
        print("   Username: admin")
        print("   Password: admin")
        print("\n🚀 Para iniciar a API, execute: uvicorn main:app --reload")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inicializar banco: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
