from contabilidad import supabase

print("🚀 Iniciando actualización del Nomenclador Oficial (MFP 360/2013)...")

# 1. Definimos las cuentas del PDL DESSPEZ según tu Excel y la Resolución
cuentas = [
    # --- ACTIVOS ---
    {"codigo": "110", "nombre": "Efectivo en Banco", "tipo": "Activo"},
    {"codigo": "240", "nombre": "Activos Fijos Tangibles", "tipo": "Activo"},
    {"codigo": "240-1", "nombre": "Edificios", "tipo": "Activo"},
    {"codigo": "240-3", "nombre": "Máquinas y Equipos Energéticos", "tipo": "Activo"},
    {"codigo": "240-4", "nombre": "Máquinas y Equipos Productivos", "tipo": "Activo"},
    {"codigo": "240-5", "nombre": "Aparatos y Equipos Técnicos Especiales", "tipo": "Activo"},
    {"codigo": "240-6", "nombre": "Medios y Equipos de Transporte", "tipo": "Activo"},
    {"codigo": "240-7", "nombre": "Muebles y Otros Objetos", "tipo": "Activo"},
    {"codigo": "265", "nombre": "Inversiones en Proceso", "tipo": "Activo"},
    
    # --- PASIVOS ---
    {"codigo": "520", "nombre": "Préstamos Recibidos por Pagar a Largo Plazo", "tipo": "Pasivo"},
    
    # --- PATRIMONIO ---
    {"codigo": "600", "nombre": "Patrimonio", "tipo": "Patrimonio"},
    
    # --- GASTOS ---
    {"codigo": "810", "nombre": "Costo de Ventas", "tipo": "Gasto"},
    {"codigo": "822", "nombre": "Gastos Generales y de Administración", "tipo": "Gasto"},
    {"codigo": "835", "nombre": "Gastos Financieros", "tipo": "Gasto"},
    {"codigo": "836", "nombre": "Gastos Financieros - Otros", "tipo": "Gasto"},
    {"codigo": "866", "nombre": "Otros Gastos", "tipo": "Gasto"},
    
    # --- INGRESOS ---
    {"codigo": "900", "nombre": "Ventas", "tipo": "Ingreso"},
    {"codigo": "920", "nombre": "Ingresos Financieros", "tipo": "Ingreso"},
]

print("2. Verificando y actualizando cuentas...")
for cta in cuentas:
    # Buscamos si la cuenta ya existe por su código
    res = supabase.table('nomenclador_cuentas').select('codigo').eq('codigo', cta['codigo']).execute()
    
    if res.data:
        # Si existe, actualizamos el nombre y el tipo
        supabase.table('nomenclador_cuentas').update({
            "nombre": cta['nombre'],
            "tipo": cta['tipo']
        }).eq('codigo', cta['codigo']).execute()
        print(f"   -> 🔄 Actualizada: {cta['codigo']} - {cta['nombre']}")
    else:
        # Si no existe, la creamos
        supabase.table('nomenclador_cuentas').insert(cta).execute()
        print(f"   -> ✅ Creada: {cta['codigo']} - {cta['nombre']}")

print("🎉 ¡Nomenclador Oficial configurado con éxito!")
