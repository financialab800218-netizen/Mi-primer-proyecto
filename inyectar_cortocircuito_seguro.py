import re

ruta = '/root/Mi-primer-proyecto/bot.py'

with open(ruta, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Buscamos la función que maneja los mensajes (handle_message)
patron_func = r'(async def handle_message\(.*?\):\n)'

# Creamos el bloque de código que queremos inyectar
bloque_inyectar = r'''\1
    try:
        texto_usuario = update.message.text.lower()
        
        # 1. CORTOCIRCUITO PARA EL BALANCE (Solo si no pide Excel, imagen o video)
        if ("balance" in texto_usuario or "estado de situacion" in texto_usuario) and not any(p in texto_usuario for p in ["excel", "imagen", "video", "pdf", "documento", "word"]):
            from reporte_contable import obtener_balance_general
            await update.message.reply_text(obtener_balance_general(), parse_mode='Markdown')
            return

        # 2. SI PIDE EXCEL O IMAGEN, DEJAMOS PASAR A LA IA
        # (El resto del código de la IA se encargará de esto)
        
    except Exception as e:
        print(f"Error en cortocircuito: {e}")
'''

# Si el cortocircuito no está, lo inyectamos justo después de la definición de la función
if "CORTOCIRCUITO PARA EL BALANCE" not in codigo:
    codigo = re.sub(patron_func, bloque_inyectar, codigo, count=1)
    print("✅ Cortocircuito seguro inyectado en handle_message.")
else:
    print("⚠️ El cortocircuito ya estaba inyectado.")

# Guardamos los cambios
with open(ruta, 'w', encoding='utf-8') as f:
    f.write(codigo)

print("✅ Proceso terminado. Reinicia el bot para probar.")
