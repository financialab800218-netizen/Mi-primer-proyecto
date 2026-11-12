import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/login.html'

print("🔧 Reparando las llaves de conexión del Login...")
url = input("1. Pega tu URL de Supabase (ej. https://xxx.supabase.co): ").strip()
key = input("2. Pega tu llave pública (la que empieza con sb_publishable_): ").strip()

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# Reemplazo exacto usando expresiones regulares
html = re.sub(r"const SUPABASE_URL = '.*?';", f"const SUPABASE_URL = '{url}';", html)
html = re.sub(r"const SUPABASE_ANON_KEY = '.*?';", f"const SUPABASE_ANON_KEY = '{key}';", html)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ ¡Llaves guardadas correctamente en el HTML!")
