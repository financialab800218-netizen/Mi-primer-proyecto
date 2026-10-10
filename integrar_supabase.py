BOT = "/root/Mi-primer-proyecto/bot_multiagent.py"
c = open(BOT).read()
open(BOT + ".bak", "w").write(c)
print("[OK] Backup")

if "from supabase_helper import" not in c:
    c = c.replace("from llm_router import", "from supabase_helper import crear_usuario, obtener_usuario\nfrom llm_router import", 1)
    print("[OK] Import")

vieja = "async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):"
nueva = """async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        u = update.effective_user
        if not obtener_usuario(u.id):
            crear_usuario(u.id, u.full_name, None, 'alumno')
            print('[SUPABASE]', u.full_name)
    except Exception as e:
        print('[SUPABASE ERR]', e)
"""

if "obtener_usuario(u.id)" not in c:
    c = c.replace(vieja, nueva, 1)
    print("[OK] cmd_start")

open(BOT, "w").write(c)
print("[OK] Listo")

