import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
RUTA_DOCS = "/root/Mi-primer-proyecto/backend/app/static/docs"


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

def subir_archivo_a_nube(ruta_local, nombre_archivo):
    try:
        from contabilidad import supabase
        with open(ruta_local, 'rb') as f:
            supabase.storage.from_('Documentos').upload(nombre_archivo, f, file_options={"content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
        url = supabase.storage.from_('Documentos').get_public_url(nombre_archivo)
        return f"[OK] Archivo subido: {url}"
    except Exception as e:
        return f"[Error] Falló la subida: {e}"
