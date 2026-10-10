"""
Script para integrar Supabase con el bot de Telegram.
Ejecutar en el VPS: python3 docs/integrar_supabase.py
"""

import os
import re

BOT_PATH = "/root/Mi-primer-proyecto/bot_multiagent.py"
BACKUP_PATH = "/root/Mi-primer-proyecto/bot_multiagent.py.backup_supabase"

# Leer el archivo actual
with open(BOT_PATH, 'r') as f:
    contenido = f.read()

# Backup
with open(BACKUP_PATH, 'w') as f:
    f.write(contenido)
print(f"[OK] Backup creado en {BACKUP_PATH}")

# 1. Añadir import de supabase_helper
if 'from supabase_helper import' not in contenido:
    # Insertar después del último 'from X import'
    import_line = "\n# Importar helper de Supabase\nfrom supabase_helper import crear_usuario, obtener_usuario\n"
    # Buscar el último 'from llm_router import*
    patron = re.compile(r'(from llm_router import[^\n]+\n)')
    contenido = patron.sub(r'\1' + import_line, contenido, count=1)
    print("[OK] Import de supabase_helper añadido")
else:
    print("[SKIP] Import ya existe")

# 2. Modificar cmd_start para registrar usuarios
viejo_start = '''async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):'''

nuevo_start = '''async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Registrar usuario en Supabase
    try:
        user = update.effective_user
        usuario_existente = obtener_usuario(user.id)
        if not usuario_existente:
            crear_usuario(user.id, user.full_name, None, 'alumno')
            print(f"[SUPABASE] Nuevo usuario registrado: {user.full_name} ({user.id})")
        else:
            print(f"[SUPABASE] Usuario existente: {user.full_name}")
    except Exception as e:
        print(f"[SUPABASE ERROR] {e}")
'''

if 'Registrar usuario en Supabase' not in contenido:
    contenido = contenido.replace(viejo_start, nuevo_start, 1)
    print("[OK] cmd_start modificado")
else:
    print("[SKIP] cmd_start ya modificado")

# Guardar cambios
with open(BOT_PATH, 'w') as f:
    f.write(contenido)

print("[OK] bot_multiagent.py actualizado")
print("Ahora ejecuta: systemctl restart tutoria-bot.service")