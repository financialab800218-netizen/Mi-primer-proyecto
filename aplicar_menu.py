import re

path = 'bot_multiagent.py'
with open(path, 'r') as f:
    code = f.read()

# 1. Añadir imports necesarios
if 'video_handler' not in code:
    code = code.replace('from telegram.ext import', 'from video_handler import enviar_respuesta_inteligente, handle_video_callback\nfrom telegram.ext import', 1)
if 'CallbackQueryHandler' not in code:
    code = code.replace('from telegram.ext import CommandHandler', 'from telegram.ext import CommandHandler, CallbackQueryHandler', 1)

# 2. Reemplazar el reply_text por nuestra función inteligente
pattern = r'(await update\.message\.reply_text\(\(respuesta or.*?\) \+ firma\))'
code = re.sub(pattern, 'await enviar_respuesta_inteligente(update, respuesta, firma, update.effective_user.id)', code)

# 3. Insertar el handler del video justo antes de 'return app'
if 'CallbackQueryHandler(handle_video_callback' not in code:
    match = re.search(r'(\n\s*return\s+app)', code)
    if match:
        insert_str = '\n    app.add_handler(CallbackQueryHandler(handle_video_callback, pattern="^vid_"))\n'
        code = code[:match.start()] + insert_str + code[match.start():]

with open(path, 'w') as f:
    f.write(code)
print("OK: Codigo modificado con exito")
