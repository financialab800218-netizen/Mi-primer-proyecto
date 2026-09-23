from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class Institucion(BaseModel):
    id: Optional[int] = None
    nombre: str
    tipo: str  # universidad, centro_investigacion, escuela
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: EmailStr
    representante_legal: str
    estado: str = "activo"


class ProfesorRepresentante(BaseModel):
    """Profesor que representa a una institucion en un curso."""
    id: Optional[int] = None
    institucion_id: int
    nombre: str
    apellido: str
    email: EmailStr
    especialidad: str
    curso_id: Optional[int] = None


class CursoInstitucional(BaseModel):
    """Curso ofrecido por una institucion (maestria, diplomado, curso)."""
    id: Optional[int] = None
    institucion_id: int
    titulo: str
    descripcion: str
    tipo: str  # curso, diplomado, maestria, doctorado
    duracion_horas: int
    precio: float
    certificacion_oficial: bool = True
    fecha_inicio: Optional[datetime] = None
    estado: str = "borrador"
