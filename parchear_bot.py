import re

ruta_bot = '/root/Mi-primer-proyecto/bot.py'

with open(ruta_bot, 'r', encoding='utf-8') as f:
    codigo = f.read()

if "CORTOCIRCUITO FORZADO" in codigo:
    print("⚠️ El cortocircuito ya estaba instalado. No se hizo nada.")
else:
    # Buscamos el inicio de la función handle_message
    patron = r"(async def handle_message.*?:\n)"
    cortocircuito = r'''\1
    # --- CORTOCIRCUITO FORZADO PARA EL BALANCE ---
    texto_usuario = update.message.text.lower()
    if "balance" in texto_usuario or "estado de situacion" in texto_usuario:
        from reporte_contable import obtener_balance_general
        reporte = obtener_balance_general()
        await update.message.reply_text(reporte, parse_mode='Markdown')
        return
    # ---------------------------------------------
'''
    codigo_nuevo, reemplazos = re.subn(patron, cortocircuito, codigo, count=1)
    
    if reemplazos > 0:
        with open(ruta_bot, 'w', encoding='utf-8') as f:
            f.write(codigo_nuevo)
        print("✅ ¡Cortocircuito instalado con éxito en bot.py!")
    else:
        print("❌ No se encontró la función 'async def handle_message'.")
        print("   -> Intentando con 'async def message_handler'...")
        patron_alt = r"(async def message_handler.*?:\n)"
        codigo_nuevo, reemplazos = re.subn(patron_alt, cortocircuito, codigo, count=1)
        if reemplazos > 0:
            with open(ruta_bot, 'w', encoding='utf-8') as f:
                f.write(codigo_nuevo)
            print("✅ ¡Cortocircuito instalado con éxito en 'message_handler'!")
        else:
            print("❌ No se encontró. Revisa el archivo manualmente.")
