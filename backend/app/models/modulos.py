from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Modulo(BaseModel):
    """Modulo de un curso. Puede tener creador institucional o TCP."""
    id: Optional[int] = None
    curso_id: int
    titulo: str
    descripcion: str
    orden: int
    duracion_horas: int
    creador_tipo: str  # "profesor_institucion" o "tcp_externo"
    creador_id: int  # ID del profesor o del TCP
    contenido_id: Optional[int] = None
    estado: str = "borrador"
    fecha_creacion: Optional[datetime] = None


class AsignacionTCP(BaseModel):
    """Asignacion de un TCP externo a un modulo especifico."""
    id: Optional[int] = None
    modulo_id: int
    tcp_id: int
    monto_licencia: float
    estado: str = "pendiente"  # pendiente, pagado
    fecha_asignacion: Optional[datetime] = None
    fecha_pago: Optional[datetime] = None


class ModuloContenido(BaseModel):
    """Contenido especifico de un modulo."""
    id: Optional[int] = None
    modulo_id: int
    titulo: str
    tipo: str  # video, pdf, texto, ejercicio
    url_archivo: Optional[str] = None
    orden: int
    duracion_minutos: Optional[int] = None
