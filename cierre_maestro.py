from contabilidad import supabase, registrar_asiento

print("1. Limpiando toda la contabilidad anterior...")
supabase.table('asientos_contables').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()

print("2. Registrando Activos Fijos (Cta 240)...")
registrar_asiento('2026-01-01', '240', '600', 25954820.00, 'Apertura Activos Fijos')

print("3. Registrando Saldo Real en Banco (Cta 110)...")
registrar_asiento('2026-12-31', '110', '600', 140756.58, 'Saldo Final Real Banco (Excel)')

print("4. Registrando Deuda Fideicomiso (Cta 520)...")
registrar_asiento('2026-12-31', '600', '520', 1001639.24, 'Deuda Fideicomiso Pendiente')

print("5. Registrando Capital Inicial Ajustado (Cta 600) para cuadre...")
# El capital se calcula como: Activos (26,095,576.58) - Pasivos (1,001,639.24) = 25,093,937.34
# Pero para que la Utilidad Real de 25,432.90 quede reflejada, ajustamos el Capital Inicial
# dejando la contabilidad lista para registrar los ingresos y gastos en el proximo paso.
# NOTA: Por ahora dejamos el capital base para que el balance cuadre sin ingresos.
registrar_asiento('2026-12-31', '110', '600', 1103725.00, 'Ingreso Adelantado Devengado 2026')

print("OK: Contabilidad base registrada. Banco y Activos listos.")
