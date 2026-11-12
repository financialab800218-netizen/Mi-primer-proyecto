from contabilidad import supabase

print("🧹 Haciendo Limpieza Total de Activos Fijos...")

# 1. Borramos TODOS los asientos donde aparezca 240, 240-1, 240-3, etc.
cuentas_aft = ['240', '240-1', '240-3', '240-4', '240-5', '240-6', '240-7']
for cta in cuentas_aft:
    supabase.table('asientos_contables').delete().eq('cuenta_debito', cta).execute()
    supabase.table('asientos_contables').delete().eq('cuenta_credito', cta).execute()

print("   -> ✅ Cuentas 240 limpias.")

# 2. Insertamos los valores de VERZAT de nuevo (de forma resumida para no hacer el script tan largo)
activos_verzat = [
    # EDIFICIOS (240-1)
    {"cuenta": "240-1", "desc": "Varios Edificios", "monto": 17770350.00},
    # MAQUINAS ENERGETICAS (240-3)
    {"cuenta": "240-3", "desc": "Equipos Energéticos (VERZAT)", "monto": 3981100.00},
    # MAQUINAS PRODUCTIVAS (240-4)
    {"cuenta": "240-4", "desc": "Equipos Productivos (VERZAT)", "monto": 18318800.00},
    # APARATOS ESPECIALES (240-5)
    {"cuenta": "240-5", "desc": "Aparatos Especiales (VERZAT)", "monto": 1025000.00},
    # TRANSPORTE (240-6)
    {"cuenta": "240-6", "desc": "Equipos de Transporte (VERZAT)", "monto": 3690000.00},
    # MUEBLES (240-7)
    {"cuenta": "240-7", "desc": "Muebles y Otros (VERZAT)", "monto": 80000.00},
]

print("   -> Insertando valores VERZAT...")
for act in activos_verzat:
    data = [
        {"fecha": "2026-01-01", "cuenta_debito": act['cuenta'], "cuenta_credito": None, "monto": act['monto'], "descripcion": act['desc']},
        {"fecha": "2026-01-01", "cuenta_debito": None, "cuenta_credito": "600", "monto": act['monto'], "descripcion": f"Capitalización: {act['desc']}"}
    ]
    supabase.table('asientos_contables').insert(data).execute()

# 3. Ajuste Final del Patrimonio
print("   -> Ajustando Patrimonio...")
# Patrimonio ideal = Total Activos - Pasivos
# Activos = 44,865,250 (AFT) + 140,756.58 (Banco) = 45,006,006.58
# Pasivos = 1,001,639.24
patrimonio_correcto = 45006006.58 - 1001639.24

res = supabase.table('asientos_contables').select('*').or_('cuenta_debito.eq.600,cuenta_credito.eq.600').execute()
saldo_actual = 0
for a in res.data:
    monto = float(a['monto'])
    if a.get('cuenta_debito') == '600': saldo_actual -= monto
    if a.get('cuenta_credito') == '600': saldo_actual += monto

diferencia = saldo_actual - patrimonio_correcto
if abs(diferencia) > 1:
    data_ajuste = [
        {"fecha": "2026-12-31", "cuenta_debito": "600", "cuenta_credito": None, "monto": abs(diferencia), "descripcion": "Ajuste Final VERZAT"},
        {"fecha": "2026-12-31", "cuenta_debito": None, "cuenta_credito": "999", "monto": abs(diferencia), "descripcion": "Ajuste Final VERZAT"}
    ]
    supabase.table('asientos_contables').insert(data_ajuste).execute()

print("🎉 ¡Base de datos limpia y actualizada con VERZAT!")
