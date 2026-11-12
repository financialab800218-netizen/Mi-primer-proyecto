from contabilidad import supabase

print("🔧 Calculando ajuste definitivo para el Patrimonio...")

# 1. Calculamos el saldo actual real de la cuenta 600
res = supabase.table('asientos_contables').select('*').or_('cuenta_debito.eq.600,cuenta_credito.eq.600').execute()
saldo_actual = 0
for a in res.data:
    monto = float(a['monto'])
    if a.get('cuenta_debito') == '600': saldo_actual -= monto
    if a.get('cuenta_credito') == '600': saldo_actual += monto

print(f"   -> Saldo actual en Supabase: ${saldo_actual:,.2f}")

# 2. El valor que debe tener según el Excel del 2025
patrimonio_correcto = 25093937.34
diferencia = saldo_actual - patrimonio_correcto

if abs(diferencia) > 1:
    print(f"   -> Ajustando diferencia de: -${diferencia:,.2f}")
    # Creamos un asiento que reste del Patrimonio (Debe 600) y lo mande a Resultados (Haber 999)
    data = [
        {"fecha": "2026-12-31", "cuenta_debito": "600", "cuenta_credito": None, "monto": abs(diferencia), "descripcion": "Ajuste por duplicidad en revelación de AFT"},
        {"fecha": "2026-12-31", "cuenta_debito": None, "cuenta_credito": "999", "monto": abs(diferencia), "descripcion": "Ajuste por duplicidad en revelación de AFT"}
    ]
    supabase.table('asientos_contables').insert(data).execute()
    print("   -> ✅ Asiento de ajuste insertado en la base de datos.")
else:
    print("   -> ✅ El patrimonio ya está en el valor correcto.")

print("\n🎉 Proceso terminado. Ejecuta el reporte para validar.")
