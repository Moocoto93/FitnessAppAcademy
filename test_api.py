"""
Script de teste rápido da API
Execute após iniciar o servidor
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("🧪 Testando Fitness App Academy API\n")
    
    # 1. Teste de Health
    print("1. Testando health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"   ✅ Health: {response.json()}\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
        return
    
    # 2. Login
    print("2. Fazendo login...")
    try:
        login_data = {"username": "admin", "password": "admin"}
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
        if response.status_code == 200:
            token_data = response.json()
            token = token_data["access_token"]
            print(f"   ✅ Login realizado! Token obtido.\n")
        else:
            print(f"   ❌ Erro no login: {response.text}\n")
            return
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
        return
    
    # 3. Listar exercícios
    print("3. Listando exercícios...")
    try:
        response = requests.get(f"{BASE_URL}/api/exercicios?limit=5")
        if response.status_code == 200:
            exercicios = response.json()
            print(f"   ✅ {len(exercicios)} exercícios retornados")
            if exercicios:
                print(f"   📋 Primeiro exercício: {exercicios[0]['nome']}\n")
        else:
            print(f"   ❌ Erro: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
    
    # 4. Obter exercício específico
    print("4. Obtendo exercício ID 1...")
    try:
        response = requests.get(f"{BASE_URL}/api/exercicios/1")
        if response.status_code == 200:
            exercicio = response.json()
            print(f"   ✅ Exercício encontrado: {exercicio['nome']}\n")
        else:
            print(f"   ❌ Erro: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
    
    # 5. Criar exercício (admin)
    print("5. Criando novo exercício (admin)...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        novo_exercicio = {
            "nome": "Teste API",
            "descricao": "Exercício criado via teste",
            "musculos": ["Teste"],
            "equipamento": "Nenhum",
            "categoria": "Teste",
            "dificuldade": "Iniciante",
            "link_execucao": "https://example.com"
        }
        response = requests.post(
            f"{BASE_URL}/api/exercicios",
            json=novo_exercicio,
            headers=headers
        )
        if response.status_code == 201:
            exercicio_criado = response.json()
            exercicio_id = exercicio_criado["id"]
            print(f"   ✅ Exercício criado com ID: {exercicio_id}\n")
            
            # 6. Deletar exercício de teste
            print("6. Deletando exercício de teste...")
            response = requests.delete(
                f"{BASE_URL}/api/exercicios/{exercicio_id}",
                headers=headers
            )
            if response.status_code == 200:
                print(f"   ✅ Exercício deletado\n")
        else:
            print(f"   ❌ Erro: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
    
    # 7. Estatísticas (admin)
    print("7. Obtendo estatísticas (admin)...")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{BASE_URL}/api/admin/stats", headers=headers)
        if response.status_code == 200:
            stats = response.json()
            print(f"   ✅ Estatísticas:")
            print(f"      - Total de exercícios: {stats['total_exercicios']}")
            print(f"      - Total de usuários: {stats['total_usuarios']}")
            print(f"      - Categorias: {len(stats['exercicios_por_categoria'])}\n")
        else:
            print(f"   ❌ Erro: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Erro: {e}\n")
    
    print("✅ Testes concluídos!")

if __name__ == "__main__":
    test_api()
