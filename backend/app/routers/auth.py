from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Optional
import bcrypt, jwt
from config import settings
from datetime import datetime, timedelta
from supabase import create_client

router = APIRouter(prefix="/auth", tags=["auth"])

SUPABASE_URL = settings.supabase_url
SUPABASE_KEY = settings.supabase_key
JWT_SECRET = settings.jwt_secret or "cambiar-este-secreto-urgente"
JWT_ALGO = "HS256"
JWT_EXPIRA_HORAS = 168

sb = create_client(SUPABASE_URL, SUPABASE_KEY)


class RegistroIn(BaseModel):
    email: str
    nombre: str
    password: str
    rol: Optional[str] = "alumno"


class LoginIn(BaseModel):
    email: str
    password: str


def hash_password(p: str) -> str:
    return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()


def verificar_password(p: str, h: str) -> bool:
    return bcrypt.checkpw(p.encode(), h.encode())


def crear_token(usuario_id: str) -> str:
    payload = {
        "sub": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=JWT_EXPIRA_HORAS)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)


def usuario_actual(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Falta token")
    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Token invalido")
    user_id = payload.get("sub")
    r = sb.table("usuarios").select("*").eq("id", user_id).execute()
    if not r.data:
        raise HTTPException(404, "Usuario no encontrado")
    return r.data[0]


@router.post("/registro")
def registro(data: RegistroIn):
    existe = sb.table("usuarios").select("id").eq("email", data.email).execute()
    if existe.data:
        raise HTTPException(400, "Email ya registrado")
    nuevo = {
        "email": data.email,
        "nombre": data.nombre,
        "password_hash": hash_password(data.password),
        "proveedor": "email",
        "rol": data.rol,
    }
    r = sb.table("usuarios").insert(nuevo).execute()
    user = r.data[0]
    return {"token": crear_token(user["id"]), "usuario": user}


@router.post("/login")
def login(data: LoginIn):
    r = sb.table("usuarios").select("*").eq("email", data.email).execute()
    if not r.data:
        raise HTTPException(401, "Credenciales invalidas")
    user = r.data[0]
    if not user.get("password_hash") or not verificar_password(data.password, user["password_hash"]):
        raise HTTPException(401, "Credenciales invalidas")
    sb.table("usuarios").update(
        {"ultimo_login": datetime.utcnow().isoformat()}
    ).eq("id", user["id"]).execute()
    return {"token": crear_token(user["id"]), "usuario": user}


@router.get("/me")
def me(user=Depends(usuario_actual)):
    return user
