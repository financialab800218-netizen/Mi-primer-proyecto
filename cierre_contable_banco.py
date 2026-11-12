from contabilidad import supabase, registrar_asiento

print("1. Borrando contabilidad anterior...")
supabase.table('asientos_contables').delete().neq('id', '00000000-0000-0000-0000-000000000000').execute()

print("2. Registrando Apertura (Activos Fijos 2025)...")
registrar_asiento('2026-01-01', '240', '600', 25954820.00, 'Apertura Activos Fijos')

print("3. Registrando Saldo Real del Banco (Sin quedarse en 0)...")
registrar_asiento('2026-12-31', '110', '600', 140756.58, 'Saldo Final Real Banco (Excel)')

print("4. Registrando Deuda del Fideicomiso...")
registrar_asiento('2026-12-31', '600', '520', 1001639.24, 'Deuda Fideicomiso Pendiente')

print("OK: Contabilidad cerrada con la realidad del banco.")
