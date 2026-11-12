# Leer el archivo bot.py
with open('/root/Mi-primer-proyecto/bot.py', 'r', encoding='utf-8') as f:
    lineas = f.readlines()

nuevas_lineas = []
saltando = False

for linea in lineas:
    # Detectamos el inicio del cortocircuito viejo (línea 57 aprox)
    if "if \"balance\" in texto_usuario" in linea:
        saltando = True
        print("🗑️ Iniciando eliminación del bloque viejo...")
        continue
    
    # Si estamos saltando, buscamos donde termina el bloque (generalmente antes de un 'return' o un 'else:')
    if saltando:
        if "return" in linea:
            saltando = False
            print("✅ Bloque viejo eliminado. Cerrando cirugía.")
            continue
        # Si encontramos código del cortocircuito nuevo, paramos de saltar
        if "CORTOCIRCUITO FORZADO" in linea:
            saltando = False
            
    if not saltando:
        nuevas_lineas.append(linea)

# Escribir el archivo corregido
with open('/root/Mi-primer-proyecto/bot.py', 'w', encoding='utf-8') as f:
    f.writelines(nuevas_lineas)

print("✅ Archivo bot.py limpiado.")
