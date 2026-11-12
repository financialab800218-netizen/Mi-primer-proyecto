from contabilidad import supabase

print("🔧 Iniciando Cirugía Final Contable...")

# 1. Renombrar asientos viejos a cuentas oficiales
print("1. Migrando cuentas 400 y 500 a las oficiales (900 y 810)...")
supabase.table('asientos_contables').update({"cuenta_debito": "900"}).eq("cuenta_debito", "400").execute()
supabase.table('asientos_contables').update({"cuenta_credito": "900"}).eq("cuenta_credito", "400").execute()
supabase.table('asientos_contables').update({"cuenta_debito": "810"}).eq("cuenta_debito", "500").execute()
supabase.table('asientos_contables').update({"cuenta_credito": "810"}).eq("cuenta_credito", "500").execute()
print("   -> ✅ Cuentas renombradas a 900 (Ventas) y 810 (Costo de Ventas).")

# 2. Calcular el ajuste de Capital
print("2. Calculando ajuste de Patrimonio (Cta 600)...")

# Consultamos todos los asientos para ver el saldo actual
res_asientos = supabase.table('asientos_contables').select('*').execute()
saldos = {}
for a in res_asientos.data:
    monto = float(a['monto'])
    if a.get('cuenta_debito'): saldos[a['cuenta_debito']] = saldos.get(a['cuenta_debito'], 0) + monto
    if a.get('cuenta_credito'): saldos[a['cuenta_credito']] = saldos.get(a['cuenta_credito'], 0) - monto

# Capital Actual vs Capital Deseado (según Excel)
capital_actual = abs(saldos.get('600', 0))
capital_deseado = 25093937.34 
diferencia = capital_deseado - capital_actual

if abs(diferencia) > 1:
    print(f"   -> Ajustando Capital por diferencia de ${diferencia:,.2f}...")
    # Si el capital actual es mayor, hacemos un asiento de Debe 600 / Haber 999 (Resultados)
    # Si es menor, al revés.
    if diferencia < 0:
        data = [
            {"fecha": "2026-12-31", "cuenta_debito": "600", "cuenta_credito": None, "monto": abs(diferencia), "descripcion": "Ajuste Capital Excel 2025"},
            {"fecha": "2026-12-31", "cuenta_debito": None, "cuenta_credito": "999", "monto": abs(diferencia), "descripcion": "Ajuste Capital Excel 2025"}
        ]
    else:
        data = [
            {"fecha": "2026-12-31", "cuenta_debito": "999", "cuenta_credito": None, "monto": abs(diferencia), "descripcion": "Ajuste Capital Excel 2025"},
            {"fecha": "2026-12-31", "cuenta_debito": None, "cuenta_credito": "600", "monto": abs(diferencia), "descripcion": "Ajuste Capital Excel 2025"}
        ]
    supabase.table('asientos_contables').insert(data).execute()
    print("   -> ✅ Capital ajustado para cuadrar con el Excel.")
else:
    print("   -> ⚠️ El capital ya estaba correcto.")

print("🎉 ¡Cirugía terminada! Ejecuta 'reporte_final.py' de nuevo para ver la magia.")
