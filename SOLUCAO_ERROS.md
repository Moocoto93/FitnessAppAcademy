# 🔧 Solução de Erros Comuns

## Erro: "no such column: exercicios.descricao"

**Causa:** Banco de dados antigo com estrutura diferente.

**Solução:**
1. Delete manualmente o arquivo `fitness_app.db`
2. Execute novamente: `python init_db.py`

Ou simplesmente execute o script novamente - ele agora remove automaticamente o banco antigo.

## Erro: "bcrypt version" ou "AttributeError: module 'bcrypt' has no attribute '__about__'"

**Causa:** Versão incompatível do bcrypt.

**Solução:**
```bash
pip uninstall bcrypt
pip install bcrypt==4.0.1
pip install -r requirements.txt
```

## Erro: "PermissionError" ao deletar banco

**Causa:** O banco está sendo usado por outro processo.

**Solução:**
1. Feche todas as instâncias do servidor (Ctrl+C)
2. Feche o VSCode se estiver aberto
3. Delete manualmente o arquivo `fitness_app.db`
4. Execute novamente: `python init_db.py`

## Erro: "ModuleNotFoundError"

**Causa:** Dependências não instaladas.

**Solução:**
```bash
pip install -r requirements.txt
```

## Erro: "FileNotFoundError: exercicios_academia.json"

**Causa:** Arquivo JSON não encontrado.

**Solução:**
Certifique-se de que o arquivo `exercicios_academia.json` está na pasta raiz do projeto.

## Reset Completo do Banco

Se quiser resetar tudo do zero:

```bash
# Windows
del fitness_app.db
python init_db.py

# Linux/Mac
rm fitness_app.db
python init_db.py
```

## Verificar se está funcionando

Após inicializar, teste:

```bash
# 1. Inicie o servidor
uvicorn main:app --reload

# 2. Em outro terminal, teste
python test_api.py
```

Ou acesse: http://localhost:8000/docs
