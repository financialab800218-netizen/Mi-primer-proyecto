from contabilidad import supabase

def obtener_balance_general():
    try:
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

        reporte = "🏛️ **ESTADO DE SITUACIÓN (Resolución 360/2013)**\n\n"

        def bloque(titulo, cuentas_a_buscar):
            nonlocal reporte
            reporte += f"**{titulo}:**\n"
            total = 0
            for codigo in cuentas_a_buscar:
                if codigo in saldos and saldos[codigo] != 0:
                    nombre = cuentas_dict.get(codigo, "Desconocida")
                    valor = abs(saldos[codigo])
                    reporte += f"- {nombre} (Cta {codigo}): ${valor:,.2f}\n"
                    total += valor
            reporte += f"*Total {titulo}: ${total:,.2f}*\n\n"
            return total

        bloque("ACTIVOS", ["110", "240-1", "240-3", "240-4", "240-5", "240-6", "240-7", "265"])
        bloque("PASIVOS", ["520"])
        bloque("PATRIMONIO", ["600"])
        bloque("INGRESOS", ["900", "400"])
        bloque("GASTOS", ["810", "822", "835", "836", "866", "500"])

        return reporte
    except Exception as e:
        return f"[Error] No se pudo generar el balance: {str(e)}"


def consultar_manual_contable():
    """Devuelve las reglas contables básicas para el agente."""
    with open('/root/Mi-primer-proyecto/manual_contable.txt', 'r', encoding='utf-8') as f:
        return f.read()
