"""
Modelos do banco de dados
"""
from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base


class Exercicio(Base):
    __tablename__ = "exercicios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), nullable=False, index=True)
    descricao = Column(Text)
    musculos = Column(JSON)  # Lista de músculos
    equipamento = Column(String(200))
    categoria = Column(String(100), index=True)
    dificuldade = Column(String(50))
    link_execucao = Column(String(500))


class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    is_admin = Column(Integer, default=0)  # 0 = usuário comum, 1 = admin
