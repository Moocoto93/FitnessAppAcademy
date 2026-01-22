"""
Script para corrigir o OpenAPI e remover autenticação dos endpoints públicos
Remove autenticação de: login, register, health, root, info
"""
import json
import requests
import time
from pathlib import Path

def corrigir_openapi():
    """
    Baixa o OpenAPI e remove autenticação dos endpoints públicos
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
        
        # Lista de endpoints públicos (não precisam de autenticação)
        endpoints_publicos = [
            "/api/auth/login",
            "/api/auth/register",
            "/health",
            "/",
            "/api/info"
        ]
        
        # Remove security de todos os endpoints públicos
        for path in endpoints_publicos:
            if path in openapi["paths"]:
                for method in openapi["paths"][path]:
                    if method in ["get", "post", "put", "delete", "patch"]:
                        endpoint = openapi["paths"][path][method]
                        if "security" in endpoint:
                            del endpoint["security"]
                            print(f"✅ Authorization removida do {method.upper()} {path}")
                        else:
                            print(f"⚪ {method.upper()} {path} já era público")
        
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
        print("6. Refresh a página (F5)")
        print("\n✅ Pronto! Agora todos os endpoints públicos funcionam sem Authorization!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Erro: API não está rodando!")
        print("💡 Execute em outro terminal: uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    
    return True

if __name__ == "__main__":
    corrigir_openapi()
