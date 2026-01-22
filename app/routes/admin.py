"""
Rotas administrativas
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Usuario, Exercicio
from app.schemas import MessageResponse
from app.auth import get_current_admin

router = APIRouter(prefix="/api/admin", tags=["Administração"])


@router.get("/stats", response_model=dict)
def obter_estatisticas(
    db: Session = Depends(get_db),
    admin: Usuario = Depends(get_current_admin)
):
    """
    Obtém estatísticas do sistema (apenas admin)
    """
    total_exercicios = db.query(Exercicio).count()
    total_usuarios = db.query(Usuario).count()
    
    # Contagem por categoria
    categorias = db.query(Exercicio.categoria).distinct().all()
    categorias_count = {}
    for cat in categorias:
        if cat[0]:
            count = db.query(Exercicio).filter(Exercicio.categoria == cat[0]).count()
            categorias_count[cat[0]] = count
    
    return {
        "total_exercicios": total_exercicios,
        "total_usuarios": total_usuarios,
        "exercicios_por_categoria": categorias_count
    }
