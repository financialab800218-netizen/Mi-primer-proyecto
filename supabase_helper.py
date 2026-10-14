"""Cliente para interactuar con Supabase."""
import os
import httpx
from dotenv import load_dotenv

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

def _headers():
    return {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }

def crear_usuario(telegram_id, nombre, email=None, rol='alumno'):
    """Crea un nuevo usuario en Supabase."""
    datos = {
        'telegram_id': str(telegram_id),
        'nombre': nombre,
        'email': email,
        'rol': rol
    }
    r = httpx.post(f'{SUPABASE_URL}/rest/v1/usuarios', headers=_headers(), json=datos, timeout=15)
    if r.status_code in (200, 201):
        return r.json()
    return {'error': r.status_code, 'detalle': r.text}

def obtener_usuario(telegram_id):
    """Busca un usuario por su ID de Telegram."""
    r = httpx.get(f'{SUPABASE_URL}/rest/v1/usuarios?telegram_id=eq.{telegram_id}', headers=_headers(), timeout=15)
    if r.status_code == 200:
        usuarios = r.json()
        return usuarios[0] if usuarios else None
    return None

def guardar_contenido(creador_id, creador_tipo, titulo, tipo, url, descripcion=None, materia=None, nivel=None):
    """Guarda contenido educativo."""
    datos = {
        'creador_id': str(creador_id),
        'creador_tipo': creador_tipo,
        'titulo': titulo,
        'tipo': tipo,
        'url': url,
        'descripcion': descripcion,
        'materia': materia,
        'nivel': nivel
    }
    r = httpx.post(f'{SUPABASE_URL}/rest/v1/contenido', headers=_headers(), json=datos, timeout=15)
    if r.status_code in (200, 201):
        return r.json()
    return {'error': r.status_code, 'detalle': r.text}
