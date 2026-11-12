from contabilidad import supabase

print("🏭 Iniciando Revalorización de Activos Fijos (Hoja VERZAT)...")

# 1. Limpiamos los asientos antiguos de las subcuentas de AFT para que no se dupliquen
print("1. Limpiando asientos anteriores de la Cta 240...")
for sub in ['240-1', '240-3', '240-4', '240-5', '240-6', '240-7']:
    supabase.table('asientos_contables').delete().eq('cuenta_debito', sub).execute()

# 2. LISTADO EXACTO SEGÚN HOJA VERZAT 2025
activos_verzat = [
    # EDIFICIOS (240-1) - No cambiaron
    {"cuenta": "240-1", "desc": "Caseta de Turbina Sumergible", "monto": 159300.00},
    {"cuenta": "240-1", "desc": "Secadero de materias primas de ormigón", "monto": 3025000.00},
    {"cuenta": "240-1", "desc": "Planta de Bio Productos", "monto": 648478.00},
    {"cuenta": "240-1", "desc": "Almacén de Insumos", "monto": 1133047.00},
    {"cuenta": "240-1", "desc": "Oficina", "monto": 1568332.00},
    {"cuenta": "240-1", "desc": "Planta de producción de alimento animal", "monto": 2769781.00},
    {"cuenta": "240-1", "desc": "Estanque circular pequeño Fundido No 1", "monto": 116178.00},
    {"cuenta": "240-1", "desc": "Estanque circular pequeño Fundido No 2", "monto": 116178.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular reproducción 6x3x0.5", "monto": 531310.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular reproducción 8x3x0.6", "monto": 695252.00},
    {"cuenta": "240-1", "desc": "Estanque circular reproductores fundido 3x1 No 1", "monto": 267428.00},
    {"cuenta": "240-1", "desc": "Estanque circular reproductores fundido 3x1 No 2", "monto": 267428.00},
    {"cuenta": "240-1", "desc": "Estanque circular reproductores fundido 3x1 No 3", "monto": 267428.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular fundido 4x2.5x1 No 1", "monto": 327803.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular fundido 4x2.5x1 No 2", "monto": 327803.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular fundido 4x2.5x1 No 3", "monto": 327803.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular Bloque 5x3x1", "monto": 291413.00},
    {"cuenta": "240-1", "desc": "Estanque rectangular Bloque 5x3x1.5", "monto": 1009058.00},
    {"cuenta": "240-1", "desc": "Procesadora de pescado", "monto": 3798380.00},
    {"cuenta": "240-1", "desc": "Caseta de Registro Electrico", "monto": 122950.00},

    # MAQUINAS ENERGETICAS (240-3) - Valores VERZAT
    {"cuenta": "240-3", "desc": "Computadora", "monto": 143500.00},
    {"cuenta": "240-3", "desc": "Impresora", "monto": 328000.00},
    {"cuenta": "240-3", "desc": "Fricer 220V No 1", "monto": 410000.00},
    {"cuenta": "240-3", "desc": "Fricer 220V No 2", "monto": 410000.00},
    {"cuenta": "240-3", "desc": "Camara de congelación", "monto": 2132000.00},
    {"cuenta": "240-3", "desc": "Kit de placas solares No 1", "monto": 278800.00},
    {"cuenta": "240-3", "desc": "Kit de placas solares No 2", "monto": 278800.00},

    # MAQUINAS PRODUCTIVAS (240-4) - Valores VERZAT
    {"cuenta": "240-4", "desc": "Molino de martillo de granos", "monto": 1476000.00},
    {"cuenta": "240-4", "desc": "Mescladora de acero inoxidable", "monto": 1230000.00},
    {"cuenta": "240-4", "desc": "Tornillo Elebador Transportador", "monto": 1025000.00},
    {"cuenta": "240-4", "desc": "Peletizadora Estrusora", "monto": 2665000.00},
    {"cuenta": "240-4", "desc": "Molino de carne eléctrico", "monto": 492000.00},
    {"cuenta": "240-4", "desc": "Bomba Sumergible solar", "monto": 1435000.00},
    {"cuenta": "240-4", "desc": "Bomba sumergible con enegía solar y electrica", "monto": 984000.00},
    {"cuenta": "240-4", "desc": "Bomba de agua solar", "monto": 943000.00},
    {"cuenta": "240-4", "desc": "Sistema de airación solar", "monto": 779000.00},
    {"cuenta": "240-4", "desc": "Descamadora FISHCUTIER", "monto": 4756000.00},
    {"cuenta": "240-4", "desc": "Separadora Recuperadora WEINZE", "monto": 1435000.00},
    {"cuenta": "240-4", "desc": "Deshidratadora 24 bandejas", "monto": 1098800.00},

    # APARATOS ESPECIALES (240-5) - Valores VERZAT
    {"cuenta": "240-5", "desc": "Elebador de Carga", "monto": 1025000.00},

    # TRANSPORTE (240-6) - Valores VERZAT
    {"cuenta": "240-6", "desc": "Triciclo Eléctrico de carga 0.5 tn", "monto": 1558000.00},
    {"cuenta": "240-6", "desc": "Triciclo Eléctrico de carga 0.5 tn con caja frigorifica", "monto": 2132000.00},

    # MUEBLES (240-7) - No cambiaron
    {"cuenta": "240-7", "desc": "Tanque plastico con rebolbedor 2000 lts", "monto": 50000.00},
    {"cuenta": "240-7", "desc": "Tanque plastico 700 lts No 1", "monto": 15000.00},
    {"cuenta": "240-7", "desc": "Tanque plastico 700 lts No 2", "monto": 15000.00},
]

print(f"2. Insertando {len(activos_verzat)} activos revalorizados...")
for act in activos_verzat:
    data = [
        {"fecha": "2026-01-01", "cuenta_debito": act['cuenta'], "cuenta_credito": None, "monto": act['monto'], "descripcion": act['desc']},
        {"fecha": "2026-01-01", "cuenta_debito": None, "cuenta_credito": "600", "monto": act['monto'], "descripcion": f"Capitalización VERZAT: {act['desc']}"}
    ]
    supabase.table('asientos_contables').insert(data).execute()

print("✅ Activos actualizados con los valores VERZAT.")

# 3. Ajuste automático del Patrimonio para que cuadre al centavo
print("3. Ajustando el Patrimonio (Cta 600)...")
res = supabase.table('asientos_contables').select('*').or_('cuenta_debito.eq.600,cuenta_credito.eq.600').execute()
saldo_actual = 0
for a in res.data:
    monto = float(a['monto'])
    if a.get('cuenta_debito') == '600': saldo_actual -= monto
    if a.get('cuenta_credito') == '600': saldo_actual += monto

# Nuevo Patrimonio correcto: Activos Totales - Pasivos Totales
# Activos = 44,865,250 (AFT) + 140,756.58 (Banco) = 45,006,006.58
# Pasivos = 1,001,639.24
patrimonio_correcto = 45006006.58 - 1001639.24 
diferencia = saldo_actual - patrimonio_correcto

if abs(diferencia) > 1:
    print(f"   -> Ajustando diferencia de Patrimonio: -${diferencia:,.2f}")
    data_ajuste = [
        {"fecha": "2026-12-31", "cuenta_debito": "600", "cuenta_credito": None, "monto": abs(diferencia), "descripcion": "Ajuste Revalorización VERZAT"},
        {"fecha": "2026-12-31", "cuenta_debito": None, "cuenta_credito": "999", "monto": abs(diferencia), "descripcion": "Ajuste Revalorización VERZAT"}
    ]
    supabase.table('asientos_contables').insert(data_ajuste).execute()
    print("   -> ✅ Patrimonio ajustado.")
else:
    print("   -> ✅ El patrimonio ya está en el valor correcto.")

print("🎉 ¡Proceso de revalorización terminado!")
