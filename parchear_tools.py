import re

ruta = '/root/Mi-primer-proyecto/tools.py'
with open(ruta, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Buscamos la definición de la función ver_balance_general (la de la IA) y la reemplazamos
patron = r"(def ver_balance_general\(.*?\):.*?(?=\ndef |\Z))"
nueva_funcion = '''def ver_balance_general():
    """Genera el Balance General con el formato exacto del Excel (VERZAT)."""
    from reporte_contable import obtener_balance_general
    return obtener_balance_general()
'''
codigo_nuevo, reemplazos = re.subn(patron, nueva_funcion, codigo, count=1, flags=re.DOTALL)

if reemplazos > 0:
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(codigo_nuevo)
    print("✅ ¡Herramienta ver_balance_general actualizada en tools.py!")
else:
    print("❌ No se encontró la función en tools.py. Buscando otra variante...")
    # Si la función tiene otro nombre en tu tools.py (ej: obtener_balance_general)
    patron_alt = r"(def obtener_balance_general\(.*?\):.*?(?=\ndef |\Z))"
    codigo_nuevo, reemplazos = re.subn(patron_alt, nueva_funcion, codigo, count=1, flags=re.DOTALL)
    if reemplazos > 0:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(codigo_nuevo)
        print("✅ ¡Herramienta obtener_balance_general actualizada en tools.py!")
    else:
        print("⚠️ No se encontró la función. Revisaremos el archivo manualmente.")
