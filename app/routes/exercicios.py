"""
Rotas para gerenciamento de exercícios
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database import get_db
from app.models import Exercicio
from app.schemas import (
    ExercicioCreate, 
    ExercicioUpdate, 
    ExercicioResponse,
    MessageResponse
)
from app.auth import get_current_admin
from app.models import Usuario

router = APIRouter(prefix="/api/exercicios", tags=["Exercícios"])


# ========== ROTAS PÚBLICAS ==========

@router.get("/", response_model=List[ExercicioResponse])
def listar_exercicios(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    categoria: Optional[str] = None,
    dificuldade: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Lista todos os exercícios (público)
    Filtros disponíveis: categoria, dificuldade, busca por nome
    """
    query = db.query(Exercicio)
    
    # Filtro por categoria
    if categoria:
        query = query.filter(Exercicio.categoria.ilike(f"%{categoria}%"))
    
    # Filtro por dificuldade
    if dificuldade:
        query = query.filter(Exercicio.dificuldade.ilike(f"%{dificuldade}%"))
    
    # Busca por nome
    if search:
        query = query.filter(
            or_(
                Exercicio.nome.ilike(f"%{search}%"),
                Exercicio.descricao.ilike(f"%{search}%")
            )
        )
    
    exercicios = query.offset(skip).limit(limit).all()
    return exercicios


@router.get("/{exercicio_id}", response_model=ExercicioResponse)
def obter_exercicio(exercicio_id: int, db: Session = Depends(get_db)):
    """
    Obtém um exercício específico por ID (público)
    """
    exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
    if not exercicio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercício não encontrado"
        )
    return exercicio


@router.get("/categoria/{categoria}", response_model=List[ExercicioResponse])
def listar_por_categoria(categoria: str, db: Session = Depends(get_db)):
    """
    Lista exercícios por categoria (público)
    """
    exercicios = db.query(Exercicio).filter(
        Exercicio.categoria.ilike(f"%{categoria}%")
    ).all()
    return exercicios


# ========== ROTAS ADMINISTRATIVAS ==========

@router.post("/", response_model=ExercicioResponse, status_code=status.HTTP_201_CREATED)
def criar_exercicio(
    exercicio: ExercicioCreate,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(get_current_admin)
):
    """
    Cria um novo exercício (apenas admin)
    """
    novo_exercicio = Exercicio(**exercicio.dict())
    db.add(novo_exercicio)
    db.commit()
    db.refresh(novo_exercicio)
    return novo_exercicio


@router.put("/{exercicio_id}", response_model=ExercicioResponse)
def atualizar_exercicio(
    exercicio_id: int,
    exercicio_update: ExercicioUpdate,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(get_current_admin)
):
    """
    Atualiza um exercício existente (apenas admin)
    """
    exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
    if not exercicio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercício não encontrado"
        )
    
    # Atualiza apenas campos fornecidos
    update_data = exercicio_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(exercicio, field, value)
    
    db.commit()
    db.refresh(exercicio)
    return exercicio


@router.delete("/{exercicio_id}", response_model=MessageResponse)
def deletar_exercicio(
    exercicio_id: int,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(get_current_admin)
):
    """
    Deleta um exercício (apenas admin)
    """
    exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
    if not exercicio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercício não encontrado"
        )
    
    db.delete(exercicio)
    db.commit()
    return {"message": "Exercício deletado com sucesso"}


@router.post("/bulk", response_model=MessageResponse)
def criar_exercicios_em_lote(
    exercicios: List[ExercicioCreate],
    db: Session = Depends(get_db),
    admin: Usuario = Depends(get_current_admin)
):
    """
    Cria múltiplos exercícios de uma vez (apenas admin)
    """
    for exercicio_data in exercicios:
        novo_exercicio = Exercicio(**exercicio_data.dict())
        db.add(novo_exercicio)
    db.commit()
    return {"message": f"{len(exercicios)} exercícios criados com sucesso"}
