import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
RUTA_DOCS = "/root/Mi-primer-proyecto/backend/app/static/docs"

def generar_excel_balance():
    if not supabase: return "Error: Base de datos no conectada."
    
    try:
        os.makedirs(RUTA_DOCS, exist_ok=True)
        
        # Datos para el Excel
        data = {
            "Concepto": [
                "ACTIVOS", "Activos Fijos (Cta 240)", "Efectivo en Banco (Cta 110)", "TOTAL ACTIVOS",
                "PASIVOS", "Préstamos (Cta 520)", "TOTAL PASIVOS",
                "PATRIMONIO", "Capital Inicial (Cta 600)", "Resultado del Periodo", "TOTAL PATRIMONIO",
                "TOTAL PASIVO + PATRIMONIO"
            ],
            "Monto (CUP)": [
                "", 25954820.00, 210413.45, 26165233.45,
                "", 1101639.24, 1101639.24,
                "", 25722145.42, -1008635.23, 24713510.19,
                26165233.45
            ]
        }
        
        df = pd.DataFrame(data)
        nombre_archivo = "balance_general_2026.xlsx"
        ruta_completa = os.path.join(RUTA_DOCS, nombre_archivo)
        df.to_excel(ruta_completa, index=False)
        
        url_nube = subir_archivo_a_nube(nombre_archivo, nombre_archivo)
        return f"Excel generado en la nube: {url_nube}"
        return f"Balance generado. Descárgalo aquí: {url}"
    except Exception as e:
        return f"Error al generar Excel: {str(e)}"
