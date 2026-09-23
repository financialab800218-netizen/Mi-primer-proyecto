from fastapi import APIRouter, HTTPException

from models.base import Institucion, ProfesorRepresentante, CursoInstitucional

router = APIRouter(
    prefix="/api/institucional",
    tags=["Institucional"]
)


instituciones = []
profesores = []
cursos = []


@router.post("/instituciones")
def registrar_institucion(datos: Institucion):
    for inst in instituciones:
        if inst["email"] == datos.email:
            raise HTTPException(400, "Institucion ya registrada")
    nueva = datos.dict()
    nueva["id"] = len(instituciones) + 1
    instituciones.append(nueva)
    return {"mensaje": "Institucion registrada", "institucion": nueva}


@router.get("/instituciones")
def listar_instituciones():
    return {"total": len(instituciones), "instituciones": instituciones}


@router.post("/profesores")
def registrar_profesor(datos: ProfesorRepresentante):
    nuevo = datos.dict()
    nuevo["id"] = len(profesores) + 1
    profesores.append(nuevo)
    return {"mensaje": "Profesor registrado", "profesor": nuevo}


@router.get("/profesores")
def listar_profesores():
    return {"total": len(profesores), "profesores": profesores}


@router.post("/cursos")
def crear_curso(datos: CursoInstitucional):
    nuevo = datos.dict()
    nuevo["id"] = len(cursos) + 1
    cursos.append(nuevo)
    return {"mensaje": "Curso creado", "curso": nuevo}


@router.get("/cursos")
def listar_cursos():
    return {"total": len(cursos), "cursos": cursos}
