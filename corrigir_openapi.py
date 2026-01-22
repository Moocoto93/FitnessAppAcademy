"""
Script para corrigir o OpenAPI e remover autenticação do login
Executa a API, baixa o OpenAPI e remove a autenticação do endpoint /auth/login
"""
import json
import requests
import time
from pathlib import Path

def corrigir_openapi():
    """
    Baixa o OpenAPI e remove autenticação do endpoint de login
    """
    print("🔧 Corrigindo especificação OpenAPI...")
    
    # Aguarda a API estar pronta
    print("⏳ Aguardando API estar pronta (10s)...")
    time.sleep(10)
    
    try:
        # Baixa o OpenAPI
        response = requests.get("http://localhost:8000/openapi.json", timeout=5)
        response.raise_for_status()
        openapi = response.json()
        
        print("✅ OpenAPI baixado com sucesso")
        
        # CORRIGE: Remove security do endpoint de login
        if "/api/auth/login" in openapi["paths"]:
            if "post" in openapi["paths"]["/api/auth/login"]:
                # Remove a require de autenticação
                endpoint = openapi["paths"]["/api/auth/login"]["post"]
                if "security" in endpoint:
                    del endpoint["security"]
                    print("✅ Authorization removida do POST /api/auth/login")
        
        # CORRIGE: Remove security do endpoint de registro
        if "/api/auth/register" in openapi["paths"]:
            if "post" in openapi["paths"]["/api/auth/register"]:
                endpoint = openapi["paths"]["/api/auth/register"]["post"]
                if "security" in endpoint:
                    del endpoint["security"]
                    print("✅ Authorization removida do POST /api/auth/register")
        
        # CORRIGE: Remove security do endpoint de health check
        if "/health" in openapi["paths"]:
            for method in openapi["paths"]["/health"]:
                if "security" in openapi["paths"]["/health"][method]:
                    del openapi["paths"]["/health"][method]["security"]
            print("✅ Authorization removida do GET /health")
        
        # Salva o OpenAPI corrigido
        output_path = Path("openapi_corrigido.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(openapi, f, indent=2)
        
        print(f"\n✅ OpenAPI corrigido salvo em: {output_path}")
        print("\n📋 Próximos passos:")
        print("1. Vá em: https://app.rapidapi.com/")
        print("2. Acesse sua API (Fitness App Academy)")
        print("3. Na aba 'API Definition', clique em 'Upload Specification'")
        print("4. Selecione o arquivo 'openapi_corrigido.json'")
        print("5. Clique em 'Upload' para sobrescrever o anterior")
        print("\n✅ Pronto! Agora o login não precisa de Authorization!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Erro: API não está rodando!")
        print("💡 Execute: python main.py")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    
    return True

if __name__ == "__main__":
    corrigir_openapi()
