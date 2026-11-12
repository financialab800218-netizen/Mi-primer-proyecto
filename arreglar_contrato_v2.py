import re

with open('bot_multiagent.py', 'r') as f:
    code = f.read()

# El bloque simplificado (Sin regex compleja)
bloque_directo = '''
    # CORTOCIRCUITO PARA CONTRATOS (Extraccion simple)
    if mensaje and ("contrato" in mensaje.lower() and "tcp" in mensaje.lower()):
        from documentos_legales import generar_contrato_tcp
        
        # Logica simple: buscar palabras clave y tomar las 2 siguientes
        palabras = mensaje.split()
        nombre_extraido = "Profesor Prueba"
        for i, p in enumerate(palabras):
            if p.lower() in ["profesor", "profesora", "para"]:
                if i + 2 < len(palabras):
                    nombre_extraido = f"{palabras[i+1]} {palabras[i+2]}"
                elif i + 1 < len(palabras):
                    nombre_extraido = palabras[i+1]
                break
                
        enlace = generar_contrato_tcp(nombre_extraido, "Universitario", "Plata", 40.0, 2290.0)
        await update.message.reply_text(f"Contrato generado para {nombre_extraido}: {enlace}")
        return
'''

# Buscamos y reemplazamos cualquier bloque anterior que mencione CORTOCIRCUITO PARA CONTRATOS
pattern = re.compile(r'# CORTOCIRCUITO PARA CONTRATOS.*?return\n', re.DOTALL)
if pattern.search(code):
    code = pattern.sub(bloque_directo + '\n', code)
    with open('bot_multiagent.py', 'w') as f:
        f.write(code)
    print('OK: Bloque reemplazado con la logica simple.')
else:
    print('ERROR: No se encontro el bloque anterior.')
