import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

RUTA_DOCS = "/root/Mi-primer-proyecto/backend/app/static/docs"

def generar_excel_asientos():
    """Genera un Excel con todos los asientos contables de Supabase."""
    if not supabase:
        return "Error: Base de datos no conectada."
    
    try:
        os.makedirs(RUTA_DOCS, exist_ok=True)
        # 1. Traer datos
        res = supabase.table("asientos_contables").select("*").execute()
        
        if not res.data:
            return "No hay movimientos contables para exportar."
            
        # 2. Convertir a DataFrame
        df = pd.DataFrame(res.data)
        
        # 3. Guardar en Excel
        nombre_archivo = "reporte_contable.xlsx"
        ruta_completa = os.path.join(RUTA_DOCS, nombre_archivo)
        df.to_excel(ruta_completa, index=False)
        
        # 4. Devolver URL publica
        url = f"https://lens-portside-masses.ngrok-free.dev/docs/{nombre_archivo}"
        return f"Excel generado con exito. Puedes descargarlo aqui: {url}"
    except Exception as e:
        return f"Error al generar Excel: {str(e)}"
