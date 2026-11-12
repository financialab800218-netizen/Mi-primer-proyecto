from fastapi import APIRouter

router = APIRouter(
    prefix="",
    tags=["Sistema"]
)

@router.get("/")
def raiz():
    return {
        "status": "ok",
        "proyecto": "TutorIA Cuba",
        "version": "0.1.0"
    }

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "tutoria-cuba-api",
        "version": "0.1.0"
    }
