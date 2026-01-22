"""
Schemas Pydantic para validação de dados
"""
from pydantic import BaseModel
from typing import List, Optional


class ExercicioBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    musculos: List[str] = []
    equipamento: Optional[str] = None
    categoria: str
    dificuldade: Optional[str] = None
    link_execucao: Optional[str] = None


class ExercicioCreate(ExercicioBase):
    pass


class ExercicioUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    musculos: Optional[List[str]] = None
    equipamento: Optional[str] = None
    categoria: Optional[str] = None
    dificuldade: Optional[str] = None
    link_execucao: Optional[str] = None


class ExercicioResponse(ExercicioBase):
    id: int
    
    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    is_admin: bool


class MessageResponse(BaseModel):
    message: str
