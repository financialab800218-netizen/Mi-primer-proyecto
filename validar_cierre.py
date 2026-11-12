from contabilidad import supabase

print("🔍 Validando el Saldo Final en Banco (Cta 110)...")

try:
    # Hacemos una consulta de 1 solo registro para ver qué columnas existen
    res_muestra = supabase.table('asientos_contables').select('*').limit(1).execute()
    
    if not res_muestra.data:
        print("⚠️ La tabla está vacía. No hay asientos para validar.")
    else:
        # Obtenemos los nombres reales de las columnas
        columnas = list(res_muestra.data[0].keys())
        print(f"ℹ️ Columnas detectadas en tu tabla: {columnas}")
        
        # Buscamos los nombres correctos (por si tienen sufijos o prefijos)
        col_debe = next((c for c in columnas if 'debe' in c.lower()), None)
        col_haber = next((c for c in columnas if 'haber' in c.lower()), None)
        col_cuenta = next((c for c in columnas if 'cuenta' in c.lower() or 'codigo' in c.lower()), None)
        
        if not col_debe or not col_haber or not col_cuenta:
            print(f"❌ No se pudieron identificar las columnas automáticamente. Debe:{col_debe}, Haber:{col_haber}, Cuenta:{col_cuenta}")
        else:
            print(f"✅ Usando columnas: Cuenta='{col_cuenta}', Debe='{col_debe}', Haber='{col_haber}'")
            
            # Consultamos todos los asientos de la cuenta 110 (Banco)
            # OJO: si tu código de cuenta es un número, cambiamos '110' por 110
            res_banco = supabase.table('asientos_contables').select(f"{col_debe}, {col_haber}").eq(col_cuenta, '110').execute()
            
            # Si no encuentra con '110', intenta con 110 (numérico)
            if not res_banco.data:
                 res_banco = supabase.table('asientos_contables').select(f"{col_debe}, {col_haber}").eq(col_cuenta, 110).execute()

            saldo_banco = sum(float(row[col_debe] or 0) - float(row[col_haber] or 0) for row in res_banco.data)
            
            print(f"💰 Saldo calculado en Banco (Cta 110): ${saldo_banco:,.2f}")

            if round(saldo_banco, 2) == 140756.58:
                print("✅ EXITO: El saldo en banco es exactamente $140,756.58")
                print("🎉 CIERRE CONTABLE COMPLETADO. El sistema ya refleja la realidad.")
            else:
                print(f"⚠️ ATENCIÓN: El saldo es ${saldo_banco:,.2f}, se esperaba $140,756.58")
                print("Revisa si el script anterior (cierre_maestro.py) dejó el saldo inicial correcto.")

except Exception as e:
    print(f"❌ Error en la validación: {e}")
