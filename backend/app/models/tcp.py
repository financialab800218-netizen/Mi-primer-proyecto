from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class TCP(BaseModel):
    """Trabajador por Cuenta Propia - Profesor individual."""
    id: Optional[int] = None
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    especialidad: str
    nivel: str  # primaria, secundaria, preuniversitario, universidad
    licencia_tcp: Optional[str] = None  # Numero de licencia ONAT
    estado: str = "activo"
    fecha_registro: Optional[datetime] = None


class TCPLogin(BaseModel):
    """Credenciales de login del TCP."""
    email: EmailStr
    password: str


class ContenidoTCP(BaseModel):
    """Contenido educativo creado por un TCP."""
    id: Optional[int] = None
    tcp_id: int
    titulo: str
    descripcion: str
    tipo: str  # video, pdf, texto, ejercicio
    materia: str
    nivel: str
    url_archivo: Optional[str] = None
    precio_licencia: float = 0.0
    estado: str = "borrador"  # borrador, publicado, archivado
    fecha_creacion: Optional[datetime] = None


class LicenciaTCP(BaseModel):
    """Licencia de contenido de un TCP a la plataforma."""
    id: Optional[int] = None
    tcp_id: int
    contenido_id: int
    monto: float
    estado: str = "pendiente"  # pendiente, pagado
    fecha_licencia: Optional[datetime] = None
    fecha_pago: Optional[datetime] = None
