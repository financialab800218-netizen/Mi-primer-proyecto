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
        # Traer todas las transacciones
        res = supabase.table("asientos_contables").select("*").execute()
        asientos = res.data

        def calcular_saldo(cuenta_buscada):
            debe = sum(float(a['monto']) for a in asientos if str(a['cuenta_debito']) == str(cuenta_buscada))
            haber = sum(float(a['monto']) for a in asientos if str(a['cuenta_credito']) == str(cuenta_buscada))
            return debe, haber

        # 1. Banco (110) - Activo (Deudor)
        debe_110, haber_110 = calcular_saldo('110')
        saldo_banco = debe_110 - haber_110

        # 2. Pasivo (520) - Acreedor
        debe_520, haber_520 = calcular_saldo('520')
        saldo_pasivo = haber_520 - debe_520

        # 3. Patrimonio Inicial (600) - Acreedor
        debe_600, haber_600 = calcular_saldo('600')
        saldo_capital = haber_600 - debe_600

        # 4. Resultados (Ingresos - Gastos)
        # Ingresos (900)
        debe_900, haber_900 = calcular_saldo('900')
        ingresos = haber_900 - debe_900
        
        # Gastos (Cuentas que empiezan por 8)
        gastos = 0
        for a in asientos:
            if str(a['cuenta_debito']).startswith('8'):
                gastos += float(a['monto'])
        
        resultado_periodo = ingresos - gastos
        
        # Activos Fijos (De la tabla activos_fijos)
        activos_fijos_res = supabase.table("activos_fijos").select("valor_adquisicion").execute()
        total_activos_fijos = sum(float(item['valor_adquisicion']) for item in activos_fijos_res.data)

        total_activos = total_activos_fijos + saldo_banco
        total_pasivo_patrimonio = saldo_pasivo + saldo_capital + resultado_periodo

        return f"""
🏛️ **BALANCE GENERAL (Acumulado)**
----------------------------------------
**ACTIVOS:**
📦 Activos Fijos (Cta 240): {total_activos_fijos:,.2f} CUP
💵 Efectivo en Banco (Cta 110): {saldo_banco:,.2f} CUP
*Total Activos: {total_activos:,.2f} CUP*

**PASIVOS:**
📉 Préstamos (Cta 520): {saldo_pasivo:,.2f} CUP
*Total Pasivos: {saldo_pasivo:,.2f} CUP*

**PATRIMONIO:**
💼 Capital Inicial (Cta 600): {saldo_capital:,.2f} CUP
📊 Resultado del Periodo: {resultado_periodo:,.2f} CUP
*Total Patrimonio: {(saldo_capital + resultado_periodo):,.2f} CUP*
----------------------------------------
"""
    except Exception as e:
        return f"Error al calcular balance: {str(e)}"


def obtener_saldo_cuenta(codigo_cuenta: str):
    """Calcula el saldo real de una cuenta (Debitos - Creditos)."""
    if not supabase:
        return "Error: Supabase no configurado."
    try:
        # Sumar debitos
        debitos = supabase.table("asientos_contables").select("monto").eq("cuenta_debito", codigo_cuenta).execute()
        total_debito = sum(item["monto"] for item in debitos.data)
        
        # Sumar creditos
        creditos = supabase.table("asientos_contables").select("monto").eq("cuenta_credito", codigo_cuenta).execute()
        total_credito = sum(item["monto"] for item in creditos.data)
        
        saldo = total_debito - total_credito
        return f"El saldo de la cuenta {codigo_cuenta} es: {saldo:,.2f} CUP."
    except Exception as e:
        return f"Error al consultar saldo: {str(e)}"
