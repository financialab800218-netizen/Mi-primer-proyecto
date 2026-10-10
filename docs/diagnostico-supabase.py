import os
import httpx
from dotenv import load_dotenv

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')

url = os.getenv('SUPABASE_URL', '').strip()
key = os.getenv('SUPABASE_KEY', '').strip()

print("=== DIAGNOSTICO SUPABASE ===")
print(f"URL len: {len(url)}")
print(f"URL repr: {repr(url)}")
print(f"KEY len: {len(key)}")
print(f"KEY repr: {repr(key[:30])}")

if not url:
    print("ERROR: URL vacia")
    exit()

if not key:
    print("ERROR: KEY vacia")
    exit()

# Limpiar posibles barras dobles
url_limpia = url.rstrip('/')

print(f"\nURL limpia: {url_limpia}")

# Prueba 1: ping a la API
print("\n=== PRUEBA 1: ping API ===")
try:
    r = httpx.get(f'{url_limpia}/rest/v1/', headers={'apikey': key, 'Authorization': f'Bearer {key}'}, timeout=10)
    print(f"Status: {r.status_code}")
    print(f"Respuesta: {r.text[:200]}")
except Exception as e:
    print(f"ERROR: {e}")

# Prueba 2: consultar tabla usuarios
print("\n=== PRUEBA 2: tabla usuarios ===")
try:
    r = httpx.get(f'{url_limpia}/rest/v1/usuarios?limit=1', headers={'apikey': key, 'Authorization': f'Bearer {key}'}, timeout=10)
    print(f"Status: {r.status_code}")
    print(f"Respuesta: {r.text[:300]}")
except Exception as e:
    print(f"ERROR: {e}")

# Prueba 3: intentar crear usuario
print("\n=== PRUEBA 3: crear usuario ===")
try:
    r = httpx.post(
        f'{url_limpia}/rest/v1/usuarios',
        headers={'apikey': key, 'Authorization': f'Bearer {key}', 'Content-Type': 'application/json', 'Prefer': 'return=representation'},
        json={'telegram_id': '5063000001', 'nombre': 'Test Marta', 'rol': 'admin'},
        timeout=15
    )
    print(f"Status: {r.status_code}")
    print(f"Respuesta: {r.text[:300]}")
except Exception as e:
    print(f"ERROR: {e}")