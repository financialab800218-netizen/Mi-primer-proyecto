from contabilidad import supabase, registrar_asiento

print("1. Registrando Ingresos por Ventas 2026...")
registrar_asiento('2026-12-31', '110', '400', 4070556.34, 'Ingresos por Ventas 2026')

print("2. Registrando Gastos Totales 2026...")
registrar_asiento('2026-12-31', '500', '110', 5148848.44, 'Gastos Totales 2026 (Incluye Materias Primas)')

print("3. Validando matemática final...")
# Verificar saldo del banco
res = supabase.table('asientos_contables').select('debe, haber').eq('cuenta_codigo', '110').execute()
saldo_banco = sum(float(row['debe']) - float(row['haber']) for row in res.data)

if round(saldo_banco, 2) == 140756.58:
    print(f"✅ EXITO: El saldo en banco es ${saldo_banco:,.2f}")
    print("🎉 CIERRE CONTABLE COMPLETADO. El sistema ahora refleja la Utilidad Real.")
else:
    print(f"❌ ERROR: El saldo del banco es ${saldo_banco:,.2f}, se esperaba $140,756.58")
    print("Revisa los asientos registrados.")
