from contabilidad import supabase

print("1. Distribuyendo Activos Fijos en subcuentas (según Excel)...")

# Valores exactos de tu hoja "NUEVO CLASIFICADOR"
distribucion = [
    {"codigo": "240-1", "monto": 17770350.00, "desc": "Edificios"},
    {"codigo": "240-3", "monto": 1194330.00, "desc": "Máquinas Energéticas"},
    {"codigo": "240-4", "monto": 5495640.00, "desc": "Máquinas Productivas"},
    {"codigo": "240-5", "monto": 307500.00, "desc": "Aparatos Técnicos"},
    {"codigo": "240-6", "monto": 1107000.00, "desc": "Equipos de Transporte"},
    {"codigo": "240-7", "monto": 80000.00, "desc": "Muebles y Otros"}
]

# Primero, verificamos si ya se distribuyó para no duplicar
res_check = supabase.table('asientos_contables').select('*').eq('cuenta_debito', '240-1').execute()

if not res_check.data:
    for item in distribucion:
        data = [
            # Debe: Subcuenta (Ej. 240-1)
            {"fecha": "2026-01-01", "cuenta_debito": item['codigo'], "cuenta_credito": None, "monto": item['monto'], "descripcion": f"Distribución AFT - {item['desc']}"},
            # Haber: Cuenta padre 240 (para que el total siga dando 25,954,820)
            {"fecha": "2026-01-01", "cuenta_debito": None, "cuenta_credito": "240", "monto": item['monto'], "descripcion": f"Distribución AFT - {item['desc']}"}
        ]
        supabase.table('asientos_contables').insert(data).execute()
    print("   -> ✅ Activos distribuidos correctamente.")
else:
    print("   -> ⚠️ Los activos ya estaban distribuidos. Saltando paso.")

print("2. Generando Reporte de Estado de Situación...")

# Consultamos todas las cuentas con sus nombres
res_cuentas = supabase.table('nomenclador_cuentas').select('*').execute()
cuentas_dict = {c['codigo']: c['nombre'] for c in res_cuentas.data}

# Consultamos todos los asientos
res_asientos = supabase.table('asientos_contables').select('*').execute()

# Calculamos saldos (Debe - Haber)
saldos = {}
for a in res_asientos.data:
    monto = float(a['monto'])
    
    cta_d = a.get('cuenta_debito')
    if cta_d:
        saldos[cta_d] = saldos.get(cta_d, 0) + monto
        
    cta_h = a.get('cuenta_credito')
    if cta_h:
        saldos[cta_h] = saldos.get(cta_h, 0) - monto

# Formateamos el reporte
print("\n=======================================================")
print("📊 ESTADO DE SITUACIÓN (Basado en Resolución 360/2013)")
print("=======================================================\n")

def imprimir_bloque(titulo, prefijos):
    print(f"**{titulo}:**")
    total_bloque = 0
    for codigo, saldo in sorted(saldos.items()):
        if any(codigo.startswith(p) for p in prefijos) and saldo != 0:
            nombre = cuentas_dict.get(codigo, "Desconocida")
            # Si es Pasivo/Patrimonio/Ingreso, el saldo natural es negativo en nuestra formula
            saldo_mostrar = abs(saldo)
            print(f"- {nombre} (Cta {codigo}): ${saldo_mostrar:,.2f}")
            total_bloque += saldo_mostrar
    print(f"*Total {titulo}: ${total_bloque:,.2f}*\n")

imprimir_bloque("ACTIVOS", ["1"])
imprimir_bloque("PASIVOS", ["4", "5"])
imprimir_bloque("PATRIMONIO", ["6"])
imprimir_bloque("INGRESOS", ["9"])
imprimir_bloque("GASTOS", ["8"])

print("=======================================================")
print("¡Listo para integrar en el bot de Telegram!")
