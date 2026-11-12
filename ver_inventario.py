from contabilidad import supabase

print("📋 REVISANDO EL INVENTARIO DE ACTIVOS FIJOS...\n")

# Consultamos los asientos de las subcuentas de la 240
res = supabase.table('asientos_contables').select('*').like('cuenta_debito', '240-%').execute()

total = 0
for a in res.data:
    print(f"[{a['cuenta_debito']}] {a['descripcion']}: ${float(a['monto']):,.2f}")
    total += float(a['monto'])

print(f"\n💰 TOTAL VALIDADO EN CONTABILIDAD: ${total:,.2f}")
