from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import health, ia, institucional, tcp, modulos, auth, agentes

app = FastAPI(
    title="TutorIA Cuba API",
    description="Plataforma tecnologica educativa - Backend API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(health.router)
app.include_router(ia.router)
app.include_router(institucional.router)
app.include_router(tcp.router)
app.include_router(modulos.router)
app.include_router(auth.router)
app.include_router(agentes.router)
