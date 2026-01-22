"""
Script para verificar se a API está pronta para produção
"""
import os
import sys

def verificar():
    print("🔍 Verificando se API está pronta para produção...\n")
    
    erros = []
    avisos = []
    
    # 1. Verificar arquivos essenciais
    print("📁 Verificando arquivos...")
    arquivos_essenciais = [
        "main.py",
        "app/config.py",
        "app/database.py",
        "app/models.py",
        "app/auth.py",
        "requirements.txt",
        "Dockerfile",
        ".env.example"
    ]
    
    for arquivo in arquivos_essenciais:
        if os.path.exists(arquivo):
            print(f"  ✅ {arquivo}")
        else:
            print(f"  ❌ {arquivo} - FALTANDO")
            erros.append(arquivo)
    
    # 2. Verificar SECRET_KEY
    print("\n🔐 Verificando segurança...")
    try:
        from app.config import settings
        if settings.SECRET_KEY == "fitness-app-academy-secret-key-2024-CHANGE-IN-PRODUCTION-USE-RANDOM-KEY":
            avisos.append("SECRET_KEY ainda está com valor padrão! Altere em produção.")
            print("  ⚠️  SECRET_KEY precisa ser alterada em produção")
        else:
            print("  ✅ SECRET_KEY configurada")
    except Exception as e:
        erros.append(f"Erro ao verificar config: {e}")
    
    # 3. Verificar dependências
    print("\n📦 Verificando dependências...")
    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        import jose
        import passlib
        print("  ✅ Dependências principais instaladas")
    except ImportError as e:
        erros.append(f"Dependência faltando: {e}")
        print(f"  ❌ {e}")
    
    # 4. Verificar banco de dados
    print("\n💾 Verificando banco de dados...")
    try:
        from app.database import engine, Base
        print("  ✅ Configuração do banco OK")
    except Exception as e:
        erros.append(f"Erro no banco: {e}")
        print(f"  ❌ {e}")
    
    # 5. Verificar rotas
    print("\n🛣️  Verificando rotas...")
    try:
        from app.routes import auth, exercicios, admin
        print("  ✅ Rotas importadas com sucesso")
    except Exception as e:
        erros.append(f"Erro nas rotas: {e}")
        print(f"  ❌ {e}")
    
    # Resumo
    print("\n" + "="*50)
    if erros:
        print(f"❌ {len(erros)} ERRO(S) ENCONTRADO(S):")
        for erro in erros:
            print(f"   - {erro}")
        print("\n⚠️  Corrija os erros antes de fazer deploy!")
        return False
    else:
        print("✅ VERIFICAÇÃO CONCLUÍDA!")
        if avisos:
            print(f"\n⚠️  {len(avisos)} AVISO(S):")
            for aviso in avisos:
                print(f"   - {aviso}")
        print("\n🚀 API pronta para produção!")
        print("\n📋 Próximos passos:")
        print("   1. Configure SECRET_KEY em produção")
        print("   2. Faça deploy (Render/Railway/Heroku)")
        print("   3. Siga o guia em RAPIDAPI_GUIDE.md")
        return True

if __name__ == "__main__":
    sucesso = verificar()
    sys.exit(0 if sucesso else 1)
