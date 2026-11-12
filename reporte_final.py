from contabilidad import supabase

print("📊 Generando Reporte Final (Formato PDL DESSPEZ)...\n")

# Consultamos catálogo y asientos
res_cuentas = supabase.table('nomenclador_cuentas').select('*').execute()
cuentas_dict = {c['codigo']: c['nombre'] for c in res_cuentas.data}

res_asientos = supabase.table('asientos_contables').select('*').execute()

saldos = {}
for a in res_asientos.data:
    monto = float(a['monto'])
    cta_d = a.get('cuenta_debito')
    cta_h = a.get('cuenta_credito')
    
    if cta_d: saldos[cta_d] = saldos.get(cta_d, 0) + monto
    if cta_h: saldos[cta_h] = saldos.get(cta_h, 0) - monto

# --- FUNCIÓN PARA IMPRIMIR BLOQUES ---
def imprimir_bloque(titulo, cuentas_a_buscar):
    print(f"**{titulo}:**")
    total = 0
    for codigo in cuentas_a_buscar:
        if codigo in saldos and saldos[codigo] != 0:
            nombre = cuentas_dict.get(codigo, "Desconocida")
            valor = abs(saldos[codigo])
            print(f"- {nombre} (Cta {codigo}): ${valor:,.2f}")
            total += valor
    print(f"*Total {titulo}: ${total:,.2f}*\n")
    return total

print("=======================================================")
print("🏛️ ESTADO DE SITUACIÓN (Resolución 360/2013)")
print("=======================================================\n")

# 1. ACTIVOS (Sumamos manualmente las subcuentas para evitar el error del padre)
imprimir_bloque("ACTIVOS", ["110", "240-1", "240-3", "240-4", "240-5", "240-6", "240-7", "265"])

# 2. PASIVOS (Solo la cuenta 520, la 400 y 500 las ignoramos aquí)
imprimir_bloque("PASIVOS", ["520"])

# 3. PATRIMONIO
imprimir_bloque("PATRIMONIO", ["600"])

# 4. INGRESOS (Aquí metemos la 400 vieja y la 900 nueva)
imprimir_bloque("INGRESOS", ["900", "400"])

# 5. GASTOS (Aquí metemos la 500 vieja y las de la resolución)
imprimir_bloque("GASTOS", ["810", "822", "835", "836", "866", "500"])

print("=======================================================")
print("✅ Reporte generado correctamente.")
