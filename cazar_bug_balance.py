# Leer el archivo bot.py
with open('/root/Mi-primer-proyecto/bot.py', 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# Creamos una nueva lista de líneas, omitiendo las líneas 65 y 66 (índices 64 y 65)
nuevas_lineas = []
for i, linea in enumerate(lineas):
    # Si es la línea 65 o 66 (contando desde 1), la saltamos
    if i == 64 or i == 65:
        print(f"🗑️ Eliminando línea {i+1}: {linea.strip()}")
        continue
    nuevas_lineas.append(linea)

# Escribir el archivo corregido
with open('/root/Mi-primer-proyecto/bot.py', 'w', encoding='utf-8') as f:
    f.writelines(nuevas_lineas)

print("✅ ¡Código duplicado eliminado! El bot ahora usará la respuesta real.")
