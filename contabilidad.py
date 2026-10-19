import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if url and key:
    supabase: Client = create_client(url, key)
else:
    supabase = None

def registrar_asiento(fecha: str, cuenta_debito: str, cuenta_credito: str, monto: float, descripcion: str, centro_costo_id: int = 1):
    if not supabase:
        return "Error: Supabase no configurado."
    try:
        data = {
            "fecha": fecha,
            "cuenta_debito": cuenta_debito,
            "cuenta_credito": cuenta_credito,
            "monto": monto,
            "descripcion": descripcion,
            "centro_costo_id": centro_costo_id
        }
        supabase.table("asientos_contables").insert(data).execute()
        return f"OK: Asiento registrado. Debito: {cuenta_debito}, Credito: {cuenta_credito}, Monto: {monto} CUP."
    except Exception as e:
        return f"Error al registrar asiento: {str(e)}"

def obtener_estado_resultados(fecha_inicio: str, fecha_fin: str):
    if not supabase:
        return "Error: Supabase no configurado."
    try:
        ingresos = supabase.table("asientos_contables").select("monto").gte("fecha", fecha_inicio).lte("fecha", fecha_fin).like("cuenta_credito", "9%").execute()
        total_ingresos = sum(item["monto"] for item in ingresos.data)

        gastos = supabase.table("asientos_contables").select("monto").gte("fecha", fecha_inicio).lte("fecha", fecha_fin).like("cuenta_debito", "8%").execute()
        total_gastos = sum(item["monto"] for item in gastos.data)

        utilidad = total_ingresos - total_gastos

        return f"""
📊 **ESTADO DE RESULTADOS ({fecha_inicio} al {fecha_fin})**
----------------------------------------
🟢 (+) Ingresos: {total_ingresos:,.2f} CUP
🔴 (-) Gastos: {total_gastos:,.2f} CUP
----------------------------------------
💰 **Utilidad Neta: {utilidad:,.2f} CUP**
"""
    except Exception as e:
        return f"Error al calcular resultados: {str(e)}"

def obtener_balance_general():
    if not supabase:
        return "Error: Supabase no configurado."
    try:
        activos_fijos = supabase.table("activos_fijos").select("valor_adquisicion").execute()
        total_activos_fijos = sum(item["valor_adquisicion"] for item in activos_fijos.data)
        
        return f"""
🏛️ **BALANCE GENERAL (Acumulado)**
----------------------------------------
📦 **Activos Fijos (Cta 240):** {total_activos_fijos:,.2f} CUP
💵 **Efectivo en Banco (Cta 110):** [Consultar saldo real]
📉 **Pasivos (Cta 520):** [Consultar saldo real]
"""
    except Exception as e:
        return f"Error al calcular balance: {str(e)}"
