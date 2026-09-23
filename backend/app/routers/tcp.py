from fastapi import APIRouter, HTTPException

from models.tcp import TCP, TCPLogin, ContenidoTCP, LicenciaTCP

router = APIRouter(
    prefix="/api/tcp",
    tags=["TCP - Profesores Independientes"]
)


tcp_registrados = []
contenidos = []
licencias = []


# ===== RUTAS FIJAS (van primero) =====

@router.get("/")
def listar_tcp():
    return {"total": len(tcp_registrados), "tcp": tcp_registrados}


@router.post("/registro")
def registrar_tcp(datos: TCP):
    for t in tcp_registrados:
        if t["email"] == datos.email:
            raise HTTPException(400, "TCP ya registrado")
    nuevo = datos.dict()
    nuevo["id"] = len(tcp_registrados) + 1
    tcp_registrados.append(nuevo)
    return {"mensaje": "TCP registrado", "tcp": nuevo}


@router.post("/login")
def login_tcp(datos: TCPLogin):
    for t in tcp_registrados:
        if t["email"] == datos.email:
            return {"mensaje": "Login exitoso", "tcp": t}
    raise HTTPException(401, "Credenciales incorrectas")


@router.post("/contenido")
def crear_contenido(datos: ContenidoTCP):
    nuevo = datos.dict()
    nuevo["id"] = len(contenidos) + 1
    contenidos.append(nuevo)
    return {"mensaje": "Contenido creado", "contenido": nuevo}


@router.get("/contenido")
def listar_contenido():
    return {"total": len(contenidos), "contenidos": contenidos}


@router.post("/licencia")
def crear_licencia(datos: LicenciaTCP):
    nueva = datos.dict()
    nueva["id"] = len(licencias) + 1
    licencias.append(nueva)
    return {"mensaje": "Licencia creada", "licencia": nueva}


@router.get("/licencia")
def listar_licencias():
    return {"total": len(licencias), "licencias": licencias}


# ===== RUTA DINAMICA (va al final) =====

@router.get("/{tcp_id}")
def obtener_tcp(tcp_id: int):
    for t in tcp_registrados:
        if t["id"] == tcp_id:
            return t
    raise HTTPException(404, "TCP no encontrado")
