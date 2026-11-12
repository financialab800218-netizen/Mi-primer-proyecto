from contabilidad import supabase

print("🔍 AUDITORÍA DE LA CUENTA 240 EN SUPABASE\n")

res = supabase.table('asientos_contables').select('*').eq('cuenta_debito', '240').execute()

if not res.data:
    print("⚠️ No hay asientos en la cuenta 240.")
else:
    for a in res.data:
        print(f"📌 {a['descripcion']}: ${float(a['monto']):,.2f} (Fecha: {a['fecha']})")

print("\n✅ Auditoría terminada.")
