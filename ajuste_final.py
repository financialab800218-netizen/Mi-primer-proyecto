from contabilidad import supabase

print("🔧 Aplicando ajuste final del Ingreso Adelantado...")

# Buscamos el asiento exacto del Ingreso Adelantado en el Debe
res = supabase.table('asientos_contables').select('id').eq('cuenta_debito', '110').eq('monto', 1103725.00).execute()

if res.data:
    for row in res.data:
        supabase.table('asientos_contables').delete().eq('id', row['id']).execute()
    print("✅ Se eliminó la entrada duplicada de $1,103,725.00 en el banco.")
else:
    print("⚠️ No se encontró el asiento a eliminar.")

print("🔍 Validando saldo final...")
res_debe = supabase.table('asientos_contables').select('monto').eq('cuenta_debito', '110').execute()
total_debe = sum(float(row['monto']) for row in res_debe.data)

res_haber = supabase.table('asientos_contables').select('monto').eq('cuenta_credito', '110').execute()
total_haber = sum(float(row['monto']) for row in res_haber.data)

saldo = total_debe - total_haber
print(f"💰 Entradas (Debe 110): ${total_debe:,.2f}")
print(f"📤 Salidas (Haber 110): ${total_haber:,.2f}")
print(f"🏦 Saldo Final Banco: ${saldo:,.2f}")

if round(saldo, 2) == 140756.58:
    print("🎉 ¡PERFECTO! El banco cuadra exactamente en $140,756.58.")
    print("🚀 La contabilidad está lista. Puedes pasar al siguiente paso.")
else:
    print("⚠️ Aún hay una pequeña diferencia. Revisar.")
