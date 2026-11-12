ruta = '/root/Mi-primer-proyecto/documentos_legales.py'

with open(ruta, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# 1. Verificamos si el import ya existe
tiene_import = any("from contabilidad import supabase" in linea for linea in lineas)

if not tiene_import:
    # Lo inyectamos en la línea 1 (o después de los imports iniciales)
    lineas.insert(0, "from contabilidad import supabase\n")
    print("✅ Importación de 'supabase' agregada al archivo.")

# 2. Reescribimos el archivo
with open(ruta, 'w', encoding='utf-8') as f:
    f.writelines(lineas)

print("✅ Archivo documentos_legales.py reparado y listo para probar.")
