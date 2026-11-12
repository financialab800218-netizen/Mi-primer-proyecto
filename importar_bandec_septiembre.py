from contabilidad import registrar_asiento

def importar_septiembre():
    print("Importando Estado de Cuenta BANDEC - Septiembre 2026...")
    
    # 1. Amortización de préstamo (Sale del banco, baja deuda)
    registrar_asiento('2026-09-08', '520', '110', 585.65, 'Amortización intereses préstamo BANDEC')
    registrar_asiento('2026-09-08', '520', '110', 100000.00, 'Amortización parte plazo préstamo BANDEC')
    
    # 2. ONAT (Impuestos y contribuciones)
    registrar_asiento('2026-09-14', '855', '110', 4130.55, 'ONAT Seguridad Social PJ y PN')
    registrar_asiento('2026-09-14', '855', '110', 502.35, 'ONAT Impuesto Ingresos Personales')
    registrar_asiento('2026-09-14', '855', '110', 1802.39, 'ONAT Impuesto Fuerza de Trabajo')
    registrar_asiento('2026-09-14', '855', '110', 1652.20, 'ONAT Seguridad Social Trabajadores')
    
    # 3. Gastos operativos
    registrar_asiento('2026-09-11', '6015', '110', 3640.00, 'Pago ETECSA Septiembre')
    registrar_asiento('2026-09-14', '601', '110', 45000.00, 'Pago salario agosto/26')
    registrar_asiento('2026-09-21', '822', '110', 10000.00, 'Pago servicios jurídicos julio y agosto')
    
    # 4. Producción en Proceso (Inversión, no gasto)
    registrar_asiento('2026-09-28', '702', '110', 120000.00, 'Pago de pescado entero (A Producción en Proceso)')
    
    # 5. Comisiones e intereses bancarios
    registrar_asiento('2026-09-14', '836', '110', 40.00, 'Comisión acreditación salario')
    registrar_asiento('2026-09-28', '836', '110', 100.00, 'Comisión Transferencia VBANDEC')
    registrar_asiento('2026-09-29', '836', '110', 100.00, 'Comisión Virtual BANDEC')
    registrar_asiento('2026-09-30', '836', '110', 1668.73, 'Intereses mes de septiembre')
    
    # 6. INGRESOS (Ventas)
    registrar_asiento('2026-09-15', '110', '900', 250000.00, 'Ingreso por venta Pienso Criollo CIMAGT')
    registrar_asiento('2026-09-28', '110', '900', 30435.00, 'Ingreso por venta de pescado a Salud Pública')
    
    print("OK: Movimientos de Septiembre importados a la contabilidad.")

if __name__ == "__main__":
    importar_septiembre()
