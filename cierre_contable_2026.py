import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY") # Usa la Service Role Key para evitar problemas de RLS

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: Faltan las credenciales de Supabase en el .env")
    sys.exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def ejecutar_cierre():
    print("🚀 Iniciando Cierre Contable 2026 - PDL DESSPEZ...")
    
    try:
        # 1. BACKUP DE SEGURIDAD
        print("📦 Haciendo backup de los asientos actuales...")
        backup_asientos = supabase.table("asientos_contables").select("*").execute()
        with open(f"backup_asientos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            import json
            json.dump(backup_asientos.data, f)
        print(f"✅ Backup guardado con {len(backup_asientos.data)} registros.")

        # NOTA: Para este cierre, lo ideal es limpiar los asientos de prueba anteriores 
        # (los que dejaron el banco en 140k pero borraron ingresos).
        print("🧹 Limpiando asientos de prueba anteriores...")
        supabase.table("asientos_contables").delete().neq("id", 0).execute()

        # 2. PREPARAR LOS ASIENTOS
        fecha_cierre = "2026-10-21"
        asientos_a_insertar = []

        # --- APERTURA ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "110", "debe": 1219048.68, "haber": 0, "concepto": "Apertura - Saldo Inicial en Banco"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "600", "debe": 0, "haber": 1219048.68, "concepto": "Apertura - Capital Inicial"})

        # --- DEVENGADO ADELANTO ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "110", "debe": 1103725.00, "haber": 0, "concepto": "Devengo - Ingreso Adelantado Dic 2025"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "400", "debe": 0, "haber": 1103725.00, "concepto": "Devengo - Ingreso Adelantado Dic 2025"})

        # --- INGRESOS POR VENTAS ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "110", "debe": 4070556.34, "haber": 0, "concepto": "Ingresos por Ventas 2026"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "400", "debe": 0, "haber": 4070556.34, "concepto": "Ingresos por Ventas 2026"})

        # --- GASTOS TOTALES ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "500", "debe": 5148848.44, "haber": 0, "concepto": "Gastos Totales 2026 (Incluye Materias Primas)"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "110", "debe": 0, "haber": 5148848.44, "concepto": "Gastos Totales 2026 (Incluye Materias Primas)"})

        # --- ACTIVOS FIJOS Y PASIVOS ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "240", "debe": 25954820.00, "haber": 0, "concepto": "Activos Fijos"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "600", "debe": 0, "haber": 25954820.00, "concepto": "Capital por Activos Fijos"})
        
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "600", "debe": 1001639.24, "haber": 0, "concepto": "Ajuste Pasivo Fideicomiso"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "520", "debe": 0, "haber": 1001639.24, "concepto": "Pasivo Fideicomiso"})

        # --- CIERRE DE UTILIDAD ---
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "300", "debe": 25432.90, "haber": 0, "concepto": "Cierre - Resultado del Ejercicio"})
        asientos_a_insertar.append({"fecha": fecha_cierre, "cuenta_codigo": "600", "debe": 0, "haber": 25432.90, "concepto": "Cierre - Resultado del Ejercicio"})

        # 3. INSERTAR EN SUPABASE
        print("💾 Insertando asientos contables en Supabase...")
        for asiento in asientos_a_insertar:
            supabase.table("asientos_contables").insert(asiento).execute()
        
        print("✅ Asientos insertados correctamente.")

        # 4. VALIDACIÓN MATEMÁTICA
        print("🔍 Ejecutando validación matemática (Partida Doble)...")
        
        # Calcular saldo final del banco (Cta 110)
        res_banco = supabase.table("asientos_contables").select("debe, haber").eq("cuenta_codigo", "110").execute()
        saldo_banco = sum(row["debe"] - row["haber"] for row in res_banco.data)
        
        # Calcular suma total del Debe y Haber
        res_totales = supabase.table("asientos_contables").select("debe, haber").execute()
        total_debe = sum(row["debe"] for row in res_totales.data)
        total_haber = sum(row["haber"] for row in res_totales.data)

        print(f"💰 Saldo Final en Banco: ${saldo_banco:,.2f}")
        print(f"⚖️ Total Debe: ${total_debe:,.2f} | Total Haber: ${total_haber:,.2f}")

        if round(saldo_banco, 2) != 140756.58:
            raise ValueError(f"❌ ERROR: El saldo del banco no es 140,756.58. Es {saldo_banco}")

        if round(total_debe, 2) != round(total_haber, 2):
            raise ValueError(f"❌ ERROR: Descuadre contable. Debe: {total_debe} | Haber: {total_haber}")

        # 5. ACTUALIZAR ACTIVOS FIJOS
        print("🏭 Actualizando tabla de activos fijos...")
        supabase.table("activos_fijos").delete().neq("id", 0).execute()
        supabase.table("activos_fijos").insert({"nombre": "Activos Fijos Totales PDL DESSPEZ", "valor": 25954820.00}).execute()

        print("🎉 ¡CIERRE CONTABLE EXITOSO! El sistema ya refleja la ganancia real de +$25,432.90 CUP.")

    except Exception as e:
        print(f"\n🚨 ERROR CRÍTICO: {e}")
        print("⏪ Iniciando ROLLBACK... Restaurando backup.")
        # Restaurar backup
        try:
            supabase.table("asientos_contables").delete().neq("id", 0).execute()
            for asiento in backup_asientos.data:
                supabase.table("asientos_contables").insert(asiento).execute()
            print("✅ Base de datos restaurada al estado anterior.")
        except Exception as rollback_error:
            print(f"❌ FALLO EN EL ROLLBACK: {rollback_error}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_cierre()

