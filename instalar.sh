#!/bin/bash

echo "========================================"
echo "Fitness App Academy - Instalação"
echo "========================================"
echo ""

echo "[1/3] Instalando dependências..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao instalar dependências"
    exit 1
fi

echo ""
echo "[2/3] Corrigindo bcrypt..."
pip uninstall bcrypt -y
pip install bcrypt==4.0.1

echo ""
echo "[3/3] Inicializando banco de dados..."
python init_db.py
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao inicializar banco"
    exit 1
fi

echo ""
echo "========================================"
echo "Instalação concluída com sucesso!"
echo "========================================"
echo ""
echo "Para iniciar a API, execute:"
echo "  uvicorn main:app --reload"
echo ""
