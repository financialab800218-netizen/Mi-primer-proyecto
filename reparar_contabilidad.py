from contabilidad import supabase

print("🚨 Iniciando reparación profunda de la contabilidad...")

# 1. Limpiar los asientos
print("1. Borrando asientos anteriores...")
supabase.table('asientos_contables').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()

# 2. Asegurar que las cuentas existan (Añadiendo el campo 'tipo' obligatorio)
print("2. Verificando catálogo de cuentas (Nomenclador)...")
cuentas_necesarias = [
    {"codigo": "110", "nombre": "Banco", "tipo": "Activo"},
    {"codigo": "240", "nombre": "Activos Fijos", "tipo": "Activo"},
    {"codigo": "400", "nombre": "Ingresos", "tipo": "Ingreso"},
    {"codigo": "500", "nombre": "Gastos", "tipo": "Gasto"},
    {"codigo": "520", "nombre": "Pasivo Fideicomiso", "tipo": "Pasivo"},
    {"codigo": "600", "nombre": "Patrimonio / Capital", "tipo": "Patrimonio"}
]

for cuenta in cuentas_necesarias:
    # Verificamos si la cuenta ya existe
    res = supabase.table('nomenclador_cuentas').select('*').eq('codigo', cuenta['codigo']).execute()
    if not res.data:
        print(f"   -> Creando cuenta {cuenta['codigo']} - {cuenta['nombre']} (Tipo: {cuenta['tipo']})")
        supabase.table('nomenclador_cuentas').insert(cuenta).execute()
    else:
        print(f"   -> La cuenta {cuenta['codigo']} ya existe. OK.")

# 3. Función para insertar (sin cambios)
def insertar_par(fecha, cta_debe, cta_haber, monto, desc):
    data = [
        {"fecha": fecha, "cuenta_debito": cta_debe, "cuenta_credito": None, "monto": monto, "descripcion": f"{desc} (Debe)"},
        {"fecha": fecha, "cuenta_debito": None, "cuenta_credito": cta_haber, "monto": monto, "descripcion": f"{desc} (Haber)"}
    ]
    supabase.table('asientos_contables').insert(data).execute()

print("3. Registrando asientos...")
insertar_par('2026-01-01', '110', '600', 1219048.68, 'Apertura - Saldo Inicial Banco')
insertar_par('2026-12-31', '110', '400', 1103725.00, 'Ingreso Adelantado Devengado')
insertar_par('2026-12-31', '110', '400', 4070556.34, 'Ingresos por Ventas 2026')
insertar_par('2026-12-31', '500', '110', 5148848.44, 'Gastos Totales 2026')
insertar_par('2026-01-01', '240', '600', 25954820.00, 'Apertura Activos Fijos')
insertar_par('2026-12-31', '600', '520', 1001639.24, 'Deuda Fideicomiso CAM')

print("✅ Asientos registrados. Validando...")

# 4. Validación final
res_debe = supabase.table('asientos_contables').select('monto').eq('cuenta_debito', '110').execute()
total_debe = sum(float(row['monto']) for row in res_debe.data)

res_haber = supabase.table('asientos_contables').select('monto').eq('cuenta_credito', '110').execute()
total_haber = sum(float(row['monto']) for row in res_haber.data)

saldo = total_debe - total_haber
print(f"💰 Entradas (Debe 110): ${total_debe:,.2f}")
print(f"📤 Salidas (Haber 110): ${total_haber:,.2f}")
print(f"🏦 Saldo Final Banco: ${saldo:,.2f}")

if round(saldo, 2) == 140756.58:
    print("🎉 ¡REPARACIÓN EXITOSA! El banco cuadra perfecto en $140,756.58.")
else:
    print("⚠️ Todavía hay una diferencia.")
