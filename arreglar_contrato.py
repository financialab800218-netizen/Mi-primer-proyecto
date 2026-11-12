import re

with open('bot_multiagent.py', 'r') as f:
    code = f.read()

# El bloque correcto con los escapes dobles
bloque_directo = '''
    # CORTOCIRCUITO PARA CONTRATOS (Con extraccion de nombre)
    if mensaje and ("contrato" in mensaje.lower() and "tcp" in mensaje.lower()):
        import re
        from documentos_legales import generar_contrato_tcp
        # Busca un nombre propio despues de 'para' o 'profesor'
        match = re.search(r'(?:para la|para el|profesor|profesora)\\s+([A-Z][a-zá-ú]+(?:\\s+[A-Z][a-zá-ú]+)*)', mensaje)
        nombre_extraido = match.group(1) if match else "Profesor Prueba"
        
        enlace = generar_contrato_tcp(nombre_extraido, "Universitario", "Plata", 40.0, 2290.0)
        await update.message.reply_text(f"Contrato generado: {enlace}")
        return
'''

# Buscamos el bloque viejo (el que causo el error) y lo reemplazamos
pattern = re.compile(r'# CORTOCIRCUITO PARA CONTRATOS.*?return\n', re.DOTALL)
if pattern.search(code):
    code = pattern.sub(bloque_directo + '\n', code)
    with open('bot_multiagent.py', 'w') as f:
        f.write(code)
    print('OK: Bloque de contratos reemplazado sin errores de sintaxis.')
else:
    print('INFO: No se encontro el bloque viejo, inyectando uno nuevo.')
    # Si no lo encuentra, lo inyecta antes del LLM
    code = code.replace('if tiene_llm():', bloque_directo + '\n    if tiene_llm():', 1)
    with open('bot_multiagent.py', 'w') as f:
        f.write(code)
    print('OK: Bloque inyectado correctamente.')
