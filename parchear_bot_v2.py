import re

ruta_bot = '/root/Mi-primer-proyecto/bot.py'

with open(ruta_bot, 'r', encoding='utf-8') as f:
    codigo = f.read()

if "CORTOCIRCUITO FORZADO" in codigo:
    print("⚠️ El cortocircuito ya estaba instalado.")
else:
    # Buscamos dinámicamente la primera función "async def" que contenga "update" o "message"
    # Esto captura handle_message, procesar_mensaje, handle_update, etc.
    patron = r"(async def .*?(?:update|message).*?:\n)"
    
    cortocircuito = r'''\1
    # --- CORTOCIRCUITO FORZADO PARA EL BALANCE ---
    try:
        texto_usuario = update.message.text.lower()
        if "balance" in texto_usuario or "estado de situacion" in texto_usuario:
            from reporte_contable import obtener_balance_general
            reporte = obtener_balance_general()
            await update.message.reply_text(reporte, parse_mode='Markdown')
            return
    except Exception:
        pass
    # ---------------------------------------------
'''
    codigo_nuevo, reemplazos = re.subn(patron, cortocircuito, codigo, count=1)
    
    if reemplazos > 0:
        with open(ruta_bot, 'w', encoding='utf-8') as f:
            f.write(codigo_nuevo)
        print("✅ ¡Cortocircuito instalado con éxito!")
    else:
        print("❌ No se encontró ninguna función de mensaje. Buscaremos otra estrategia.")
