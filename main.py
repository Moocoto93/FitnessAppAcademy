"""
Fitness App Academy API
API completa com autenticação JWT e gerenciamento de exercícios
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import auth, exercicios, admin

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="Fitness App Academy API",
    description="API profissional para gestão de treinos e exercícios com autenticação JWT",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(auth.router)
app.include_router(exercicios.router)
app.include_router(admin.router)


@app.get("/")
def root():
    """Endpoint raiz"""
    return {
        "message": "Fitness App Academy API",
        "version": "2.0.0",
        "docs": "/docs",
        "endpoints": {
            "autenticacao": "/api/auth/login",
            "exercicios": "/api/exercicios",
            "admin": "/api/admin"
        }
    }


@app.get("/health")
def health_check():
    """Endpoint de verificação de saúde"""
    return {"status": "healthy", "message": "API está funcionando"}
