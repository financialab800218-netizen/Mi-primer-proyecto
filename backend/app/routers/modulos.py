from fastapi import APIRouter, HTTPException

from models.modulos import Modulo, AsignacionTCP, ModuloContenido

router = APIRouter(
    prefix="/api/modulos",
    tags=["Modulos - Contenido Mixto"]
)


modulos = []
asignaciones = []
contenidos_modulo = []


# ===== RUTAS FIJAS (van primero) =====

@router.get("/")
def listar_modulos():
    return {"total": len(modulos), "modulos": modulos}


@router.post("/")
def crear_modulo(datos: Modulo):
    nuevo = datos.dict()
    nuevo["id"] = len(modulos) + 1
    modulos.append(nuevo)
    return {"mensaje": "Modulo creado", "modulo": nuevo}


@router.get("/asignaciones")
def listar_asignaciones():
    return {"total": len(asignaciones), "asignaciones": asignaciones}


@router.post("/asignaciones")
def crear_asignacion(datos: AsignacionTCP):
    nueva = datos.dict()
    nueva["id"] = len(asignaciones) + 1
    asignaciones.append(nueva)
    return {"mensaje": "Asignacion creada", "asignacion": nueva}


@router.get("/contenidos")
def listar_contenidos():
    return {"total": len(contenidos_modulo), "contenidos": contenidos_modulo}


@router.post("/contenidos")
def crear_contenido(datos: ModuloContenido):
    nuevo = datos.dict()
    nuevo["id"] = len(contenidos_modulo) + 1
    contenidos_modulo.append(nuevo)
    return {"mensaje": "Contenido creado", "contenido": nuevo}


@router.get("/curso/{curso_id}")
def modulos_por_curso(curso_id: int):
    resultado = [m for m in modulos if m["curso_id"] == curso_id]
    return {"total": len(resultado), "modulos": resultado}


# ===== RUTA DINAMICA (va al final) =====

@router.get("/{modulo_id}")
def obtener_modulo(modulo_id: int):
    for m in modulos:
        if m["id"] == modulo_id:
            return m
    raise HTTPException(404, "Modulo no encontrado")
