from contabilidad import supabase

print("🔍 Validando el Saldo Final en Banco (Cta 110) con la estructura real...")

try:
    # 1. Buscar todos los movimientos donde la cuenta 110 esté en el DEBE (entradas)
    res_debe = supabase.table('asientos_contables').select('monto').eq('cuenta_debito', '110').execute()
    total_debe = sum(float(row['monto']) for row in res_debe.data)

    # 2. Buscar todos los movimientos donde la cuenta 110 esté en el HABER (salidas)
    res_haber = supabase.table('asientos_contables').select('monto').eq('cuenta_credito', '110').execute()
    total_haber = sum(float(row['monto']) for row in res_haber.data)

    # 3. Calcular el saldo real
    saldo_banco = total_debe - total_haber

    print(f"📥 Total entradas (Debe Cta 110): ${total_debe:,.2f}")
    print(f"📤 Total salidas (Haber Cta 110): ${total_haber:,.2f}")
    print(f"💰 Saldo Final en Banco: ${saldo_banco:,.2f}")

    if round(saldo_banco, 2) == 140756.58:
        print("✅ ¡EXITO! El saldo en banco es exactamente $140,756.58")
        print("🎉 CIERRE CONTABLE COMPLETADO. La contabilidad está perfecta.")
    else:
        print(f"⚠️ ATENCIÓN: El saldo es ${saldo_banco:,.2f}, se esperaba $140,756.58")
        # Verificamos si hay un problema con el signo o el formato
        if round(abs(saldo_banco), 2) == 140756.58:
            print("👉 El monto es correcto, pero está invertido. Revisa si el asiento se registró al revés.")
        else:
            print("👉 Hay una diferencia. Revisa los asientos anteriores.")

except Exception as e:
    print(f"❌ Error en la validación: {e}")
