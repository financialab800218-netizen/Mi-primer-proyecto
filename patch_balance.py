import re

with open('contabilidad.py', 'r') as f:
    code = f.read()

nueva_funcion = '''def obtener_balance_general():
    if not supabase:
        return "Error: Supabase no configurado."
    try:
        # Traer todas las transacciones
        res = supabase.table("asientos_contables").select("*").execute()
        asientos = res.data

        def calcular_saldo(cuenta_buscada):
            debe = sum(float(a['monto']) for a in asientos if str(a['cuenta_debito']) == str(cuenta_buscada))
            haber = sum(float(a['monto']) for a in asientos if str(a['cuenta_credito']) == str(cuenta_buscada))
            return debe, haber

        # 1. Banco (110) - Activo (Deudor)
        debe_110, haber_110 = calcular_saldo('110')
        saldo_banco = debe_110 - haber_110

        # 2. Pasivo (520) - Acreedor
        debe_520, haber_520 = calcular_saldo('520')
        saldo_pasivo = haber_520 - debe_520

        # 3. Patrimonio Inicial (600) - Acreedor
        debe_600, haber_600 = calcular_saldo('600')
        saldo_capital = haber_600 - debe_600

        # 4. Resultados (Ingresos - Gastos)
        # Ingresos (900)
        debe_900, haber_900 = calcular_saldo('900')
        ingresos = haber_900 - debe_900
        
        # Gastos (Cuentas que empiezan por 8)
        gastos = 0
        for a in asientos:
            if str(a['cuenta_debito']).startswith('8'):
                gastos += float(a['monto'])
        
        resultado_periodo = ingresos - gastos
        
        # Activos Fijos (De la tabla activos_fijos)
        activos_fijos_res = supabase.table("activos_fijos").select("valor_adquisicion").execute()
        total_activos_fijos = sum(float(item['valor_adquisicion']) for item in activos_fijos_res.data)

        total_activos = total_activos_fijos + saldo_banco
        total_pasivo_patrimonio = saldo_pasivo + saldo_capital + resultado_periodo

        return f"""
🏛️ **BALANCE GENERAL (Acumulado)**
----------------------------------------
**ACTIVOS:**
📦 Activos Fijos (Cta 240): {total_activos_fijos:,.2f} CUP
💵 Efectivo en Banco (Cta 110): {saldo_banco:,.2f} CUP
*Total Activos: {total_activos:,.2f} CUP*

**PASIVOS:**
📉 Préstamos (Cta 520): {saldo_pasivo:,.2f} CUP
*Total Pasivos: {saldo_pasivo:,.2f} CUP*

**PATRIMONIO:**
💼 Capital Inicial (Cta 600): {saldo_capital:,.2f} CUP
📊 Resultado del Periodo: {resultado_periodo:,.2f} CUP
*Total Patrimonio: {(saldo_capital + resultado_periodo):,.2f} CUP*
----------------------------------------
"""
    except Exception as e:
        return f"Error al calcular balance: {str(e)}"
'''

# Reemplazar la función vieja por la nueva
pattern = re.compile(r'def obtener_balance_general\(\):.*?(?=\ndef |\Z)', re.DOTALL)
match = pattern.search(code)
if match:
    code = code[:match.start()] + nueva_funcion + '\n' + code[match.end():]
    with open('contabilidad.py', 'w') as f:
        f.write(code)
    print("OK: Funcion de Balance General actualizada con matematica real.")
else:
    print("ERROR: No se encontro la funcion vieja.")
