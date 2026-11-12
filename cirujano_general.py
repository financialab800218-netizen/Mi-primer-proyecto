import re
import os

print("🩺 Iniciando cirugía de reparación...")

# --- 1. Arreglar documentos.py (Excel) ---
ruta_doc = '/root/Mi-primer-proyecto/documentos.py'
if os.path.exists(ruta_doc):
    with open(ruta_doc, 'r', encoding='utf-8') as f:
        doc_code = f.read()
    
    # Verificamos si existe la función de subir
    if "def subir_archivo_a_nube" not in doc_code:
        print("🔧 Inyectando función 'subir_archivo_a_nube' en documentos.py...")
        # Creamos una función simple de subida usando la configuración actual
        funcion_subida = '''
def subir_archivo_a_nube(ruta_local, nombre_archivo):
    try:
        from contabilidad import supabase
        with open(ruta_local, 'rb') as f:
            supabase.storage.from_('Documentos').upload(nombre_archivo, f, file_options={"content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
        url = supabase.storage.from_('Documentos').get_public_url(nombre_archivo)
        return f"[OK] Archivo subido: {url}"
    except Exception as e:
        return f"[Error] Falló la subida: {e}"
'''
        doc_code += "\n" + funcion_subida
        with open(ruta_doc, 'w', encoding='utf-8') as f:
            f.write(doc_code)
    else:
        print("✅ documentos.py ya tiene la función de subida.")

# --- 2. Arreglar tools.py (Error de Agnes) ---
ruta_tools = '/root/Mi-primer-proyecto/tools.py'
with open(ruta_tools, 'r', encoding='utf-8') as f:
    tools_code = f.read()

# Buscamos el import que está rompiendo todo
if "from contabilidad import registrar_asiento, obtener_estado_resultados" in tools_code:
    print("🔧 Quitando import roto de 'obtener_estado_resultados' en tools.py...")
    tools_code = tools_code.replace(
        "from contabilidad import registrar_asiento, obtener_estado_resultados", 
        "from contabilidad import registrar_asiento"
    )
    with open(ruta_tools, 'w', encoding='utf-8') as f:
        f.write(tools_code)
    print("✅ tools.py reparado. Agnes ya no debería dar error.")

print("🎉 Cirugía terminada. Reinicia el bot y prueba.")
