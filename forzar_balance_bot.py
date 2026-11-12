import re

ruta = '/root/Mi-primer-proyecto/bot.py'

with open(ruta, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Buscamos si hay alguna memoria de historial y la limpiamos
# (Buscamos variables que guarden el historial de chat)
codigo = re.sub(r'historial_chat\s*=\s*\[\]', 'historial_chat = [] # Limpiado', codigo)
codigo = re.sub(r'conversation_history\s*=\s*\[\]', 'conversation_history = [] # Limpiado', codigo)

# Vamos a buscar la función que maneja el texto y le inyectamos una orden forzada
# si el usuario pide "balance"
patron_balance = r'(if\s+.*?"balance"\s+in\s+.*?texto.*?:\n)'
inyeccion = r'''\1
        # --- FORZAR LECTURA DE DATOS ACTUALIZADOS ---
        from reporte_contable import obtener_balance_general
        reporte_actualizado = obtener_balance_general()
        await update.message.reply_text(reporte_actualizado, parse_mode='Markdown')
        return
        # --------------------------------------------
'''

# Aplicamos la inyección (solo si no está ya inyectado)
if "FORZAR LECTURA DE DATOS" not in codigo:
    codigo = re.sub(patron_balance, inyeccion, codigo, count=1)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(codigo)

print("✅ Bot parcheado. Ahora forzará la lectura de los datos nuevos.")
