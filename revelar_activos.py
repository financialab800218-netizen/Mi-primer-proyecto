from contabilidad import supabase

print("🏭 Iniciando Revelación de Activos Fijos uno por uno...")

# 1. LIMPIEZA PREVIA: Borramos los asientos de la cuenta 240 (padre y subcuentas) para no duplicar
print("1. Limpiando asientos antiguos de Activos Fijos...")
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240').execute()
supabase.table('asientos_contables').delete().eq('cuenta_credito', '240').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-1').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-3').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-4').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-5').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-6').execute()
supabase.table('asientos_contables').delete().eq('cuenta_debito', '240-7').execute()

# 2. LISTADO EXACTO SEGÚN EXCEL 2025 (¡Uno por uno!)
activos = [
    # EDIFICIOS (240-1)
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
    
    # MAQUINAS ENERGETICAS (240-3)
    {"cuenta": "240-3", "desc": "Computadora", "monto": 43050.00},
    {"cuenta": "240-3", "desc": "Impresora", "monto": 98400.00},
    {"cuenta": "240-3", "desc": "Fricer 220V No 1", "monto": 123000.00},
    {"cuenta": "240-3", "desc": "Fricer 220V No 2", "monto": 123000.00},
    {"cuenta": "240-3", "desc": "Camara de congelación", "monto": 639600.00},
    {"cuenta": "240-3", "desc": "Kit de placas solares No 1", "monto": 83640.00},
    {"cuenta": "240-3", "desc": "Kit de placas solares No 2", "monto": 83640.00},

    # MAQUINAS PRODUCTIVAS (240-4)
    {"cuenta": "240-4", "desc": "Molino de martillo de granos", "monto": 442800.00},
    {"cuenta": "240-4", "desc": "Mescladora de acero inoxidable", "monto": 369000.00},
    {"cuenta": "240-4", "desc": "Tornillo Elebador Transportador", "monto": 307500.00},
    {"cuenta": "240-4", "desc": "Peletizadora Estrusora", "monto": 799500.00},
    {"cuenta": "240-4", "desc": "Molino de carne eléctrico", "monto": 147600.00},
    {"cuenta": "240-4", "desc": "Bomba Sumergible solar", "monto": 430500.00},
    {"cuenta": "240-4", "desc": "Bomba sumergible con enegía solar y electrica", "monto": 295200.00},
    {"cuenta": "240-4", "desc": "Bomba de agua solar", "monto": 282900.00},
    {"cuenta": "240-4", "desc": "Sistema de airación solar", "monto": 233700.00},
    {"cuenta": "240-4", "desc": "Descamadora FISHCUTIER", "monto": 1426800.00},
    {"cuenta": "240-4", "desc": "Separadora Recuperadora WEINZE", "monto": 430500.00},
    {"cuenta": "240-4", "desc": "Deshidratadora 24 bandejas", "monto": 329640.00},

    # APARATOS ESPECIALES (240-5)
    {"cuenta": "240-5", "desc": "Elebador de Carga", "monto": 307500.00},

    # TRANSPORTE (240-6)
    {"cuenta": "240-6", "desc": "Triciclo Eléctrico de carga 0.5 tn", "monto": 467400.00},
    {"cuenta": "240-6", "desc": "Triciclo Eléctrico de carga 0.5 tn con caja frigorifica", "monto": 639600.00},

    # MUEBLES (240-7)
    {"cuenta": "240-7", "desc": "Tanque plastico con rebolbedor 2000 lts", "monto": 50000.00},
    {"cuenta": "240-7", "desc": "Tanque plastico 700 lts No 1", "monto": 15000.00},
    {"cuenta": "240-7", "desc": "Tanque plastico 700 lts No 2", "monto": 15000.00},
]

print(f"2. Insertando {len(activos)} activos individuales...")
for act in activos:
    data = [
        # Debe: El activo específico
        {"fecha": "2026-01-01", "cuenta_debito": act['cuenta'], "cuenta_credito": None, "monto": act['monto'], "descripcion": act['desc']},
        # Haber: Cuenta de Patrimonio (porque fue una inversión inicial)
        {"fecha": "2026-01-01", "cuenta_debito": None, "cuenta_credito": "600", "monto": act['monto'], "descripcion": f"Capitalización: {act['desc']}"}
    ]
    supabase.table('asientos_contables').insert(data).execute()

print("✅ ¡Los 44 activos fijos han sido revelados y registrados uno por uno!")
