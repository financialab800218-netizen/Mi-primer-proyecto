import re

ruta = '/root/Mi-primer-proyecto/bot.py'

with open(ruta, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# Vamos a filtrar las líneas que estén duplicadas o rotas
lineas_limpias = []
saltar = False

for i, linea in enumerate(lineas):
    # Si encontramos una línea de error de sintaxis conocida o duplicada
    if "reporte_actualizado = obtener_balance_general()" in linea:
        if saltar:
            continue
        saltar = True
    else:
        saltar = False
        
    lineas_limpias.append(linea)

# Reescribimos el archivo limpio
with open(ruta, 'w', encoding='utf-8') as f:
    f.writelines(lineas_limpias)

print("✅ Bot.py limpiado de líneas duplicadas.")
