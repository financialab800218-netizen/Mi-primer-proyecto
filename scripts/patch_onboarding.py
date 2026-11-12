"""Aplica los cambios de onboarding a bot_multiagent.py."""
from pathlib import Path
import re

BOT = Path("/root/Mi-primer-proyecto/bot_multiagent.py")
c = BOT.read_text(encoding='utf-8')

# 1. Añadir import de onboarding (si no existe)
if "from onboarding import" not in c:
    c = c.replace(
        "from telegram.ext import",
        "from onboarding import (\n    es_usuario_nuevo, registrar_usuario, enviar_bienvenida,\n    handle_onboarding_callback, marcar_completado,\n)\nfrom telegram.ext import",
        1,
    )
    print("OK: import anadido")

# 2. Reemplazar cuerpo de cmd_start
nuevo_cmd_start = '''async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    user_agents[user_id] = "pablo"

    if es_usuario_nuevo(user_id):
        registrar_usuario(user_id, user.first_name or "amigo", user.username)
        await enviar_bienvenida(update)
        return

    estado_ia = "ACTIVA" if tiene_llm() else "PENDIENTE"
    nombre = user.first_name or "amigo"
    mensaje = (
        f"Hola {nombre}. Bienvenido al Ecosistema Mayabeque.\\n\\n"
        f"IA: {estado_ia}\\n\\n"
        "Soy Pablo, Director Adjunto.\\n"
        "Agentes disponibles:\\n"
    )
    for key, agente in listar_agentes():
        mensaje += f"  /{key} - {agente['cargo']}\\n"
    mensaje += (
        "\\nOtros comandos:\\n"
        "  /ayuda  - Ver esta lista\\n"
        "  /quien  - Con quien hablo\\n"
        "  /salir  - Volver a Pablo\\n"
    )
    await update.message.reply_text(mensaje)
'''

patron_cmd_start = re.compile(
    r'async def cmd_start\(.*?\n(?=async def )',
    re.DOTALL,
)
if patron_cmd_start.search(c):
    c = patron_cmd_start.sub(nuevo_cmd_start + "\n\n", c, count=1)
    print("OK: cmd_start reemplazado")

# 3. Registrar CallbackQueryHandler
if "CallbackQueryHandler" not in c:
    c = c.replace(
        "from telegram.ext import",
        "from telegram.ext import CallbackQueryHandler,",
        1,
    )
if "onb:" not in c:
    c = c.replace(
        'app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))',
        'app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))\n    app.add_handler(CallbackQueryHandler(handle_onboarding_callback, pattern="^onb:"))',
        1,
    )
    print("OK: callback handler registrado")

BOT.write_text(c, encoding='utf-8')
print("PATCH COMPLETO")

