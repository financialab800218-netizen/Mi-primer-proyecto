from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def raiz():
    return {
        "status": "ok",
        "proyecto": "TutorIA Cuba",
        "version": "0.1.0",
        "environment": settings.environment
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "tutoria-cuba-api",
        "version": "0.1.0"
    }
