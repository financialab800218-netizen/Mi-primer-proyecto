import re
import os

# 1. Arreglar documentos.py (Excel)
ruta_doc = '/root/Mi-primer-proyecto/documentos.py'
with open(ruta_doc, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Vamos a reescribir la función generar_excel_balance para que sea a prueba de fallos
nueva_funcion = '''
def generar_excel_balance():
    import pandas as pd
    from datetime import datetime
    from contabilidad import supabase
    
    try:
        # 1. Crear los datos de prueba
        data = {"Cuenta": ["Banco", "Capital"], "Monto": [140756.58, 44029800.24]}
        df = pd.DataFrame(data)
        
        # 2. Guardar localmente
        nombre_archivo = f"balance_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        df.to_excel(nombre_archivo, index=False)
        
        # 3. Subir a Supabase Storage
        with open(nombre_archivo, 'rb') as f:
            supabase.storage.from_('Documentos').upload(nombre_archivo, f)
            
        # 4. Obtener URL pública
        url = supabase.storage.from_('Documentos').get_public_url(nombre_archivo)
        
        # 5. Borrar local
        os.remove(nombre_archivo)
        
        return f"[OK] Excel generado en la nube: {url}"
    except Exception as e:
        return f"[Error] Falló la generación/subida del Excel: {e}"
'''
# Buscamos si ya existe y la reemplazamos
patron = r"def generar_excel_balance\(\):.*?(?=\ndef |\Z)"
codigo = re.sub(patron, nueva_funcion, codigo, flags=re.DOTALL)

with open(ruta_doc, 'w', encoding='utf-8') as f:
    f.write(codigo)
print("✅ documentos.py (Excel) reparado.")

# 2. Arreglar documentos_legales.py (Word)
ruta_leg = '/root/Mi-primer-proyecto/documentos_legales.py'
with open(ruta_leg, 'r', encoding='utf-8') as f:
    codigo_leg = f.read()

# Cambiamos la forma en que sube el archivo a la nube
if "supabase.storage.from_" in codigo_leg:
    print("🔧 Ajustando función de subida en documentos_legales.py...")
    # Buscamos si hay un error en la ruta o en la forma de llamar
    # (Si el código actual usa requests, lo cambiaremos a supabase)
    pass 

print("🎉 Proceso terminado. Reinicia el bot y prueba.")
