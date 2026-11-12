# configurar_login.py
ruta = '/root/Mi-primer-proyecto/backend/app/static/login.html'

print("🔧 Configurando la conexión de la pantalla de Login...")
url = input("1. Pega tu Project URL de Supabase (ej. https://xxx.supabase.co): ").strip()
key = input("2. Pega tu anon public Key (la que empieza con sb_publishable_): ").strip()

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# Reemplazamos los textos de ejemplo por las llaves reales
html = html.replace("https://TU_PROYECTO.supabase.co", url)
html = html.replace("TU_ANON_KEY", key)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ ¡Login configurado con éxito con tus llaves reales!")
