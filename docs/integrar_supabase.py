"""
integrar_supabase.py

Script para automatizar la integración del bot con Supabase.

· Respalda bot_multiagent.py antes de modificar.
· Añade el import de supabase_helper.
· Modifica la función cmd_start para registrar usuarios nuevos en Supabase con crear_usuario.
· Muestra mensajes de confirmación.

Uso:
    python integrar_supabase.py
"""

import os
import shutil

# 1. Backup del archivo original
BOT_FILE = "bot_multiagent.py"
BACKUP_SUFFIX = ".bak"
backup_file = f"{BOT_FILE}{BACKUP_SUFFIX}"

if os.path.exists(BOT_FILE):
    shutil.copy(BOT_FILE, backup_file)
    print(f"[✓] Respaldo creado: {backup_file}")
else:
    print(f"[!] ERROR: {BOT_FILE} no existe. Abortando.")
    exit(1)

# 2. Agregar import de supabase_helper al archivo bot_multiagent.py
import_line = "from supabase_helper import crear_usuario\n"

with open(BOT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

if import_line in lines:
    print("[✓] Import de supabase_helper ya presente.")
else:
    insert_index = 0
    for idx, line in enumerate(lines):
        if line.startswith("import") or line.startswith("from"):
            insert_index = idx + 1
        else:
            break
    lines.insert(insert_index, import_line)
    with open(BOT_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("[✓] Import de supabase_helper agregado.")

# 3. Modificar la función start_handler (ej: execute_start) para registrar el usuario
start_func_pattern = "def execute_start(update, context):"
with open(BOT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

if start_func_pattern in content:
    new_content = content.replace(start_func_pattern,
                                  f"{start_func_pattern}\n    user = update.effective_user\n    try:\n        crear_usuario(user.id, user.first_name)\n        update.message.reply_text('Usuario registrado en Supabase.')\n    except Exception as e:\n        update.message.reply_text(f'Error al registrar usuario: {e}')\n")
    with open(BOT_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[✓] Función 시작 modificada para registro en Supabase.")
else:
    print("[!] No se encontró la función execute_start. Debes añadir manualmente el código de registro.")

print("[✓] Integración con Supabase completada. Confirme el funcionamiento.")
