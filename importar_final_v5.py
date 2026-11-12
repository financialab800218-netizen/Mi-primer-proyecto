import csv
from contabilidad import supabase, registrar_asiento

def cargar_datos_real():
    print("Iniciando importacion REAL v5 (Solo Banco y Produccion)...")
    archivo = 'datos 2026.csv'
    
    # 1. Limpiamos la tabla (dejando los asientos de apertura del 01-01)
    supabase.table('asientos_contables').delete().neq('fecha', '2026-01-01').execute()
    
    count = 0
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for _ in range(5): next(reader, None) # Saltar encabezados
                
            for row in reader:
                if not row or len(row) < 9: continue
                
                try:
                    dia = row[0].strip()
                    mes = row[1].strip()
                    desc = row[8].strip()
                    
                    if not dia or not mes or not desc or desc == '""': continue
                    
                    fecha = f"2026-{int(mes):02d}-{int(dia):02d}"
                    
                    # Extraer el Monto (último número válido de la fila)
                    monto = 0.0
                    for valor in reversed(row):
                        valor = valor.strip().replace('"', '')
                        if valor:
                            try:
                                monto = float(valor)
                                break
                            except ValueError:
                                pass
                        
                    if monto <= 0: continue
                    
                    desc_lower = desc.lower()
                    
                    # --- CLASIFICACION CONTABLE ---
                    
                    # 1. ENTRADAS (Ventas o Cobros)
                    if "ingr" in desc_lower or "venta" in desc_lower or "cobro de venta" in desc_lower or "cobro de intereses" in desc_lower:
                        registrar_asiento(fecha, '110', '900', monto, desc)
                        count += 1
                        
                    # 2. DEVOLUCION DE AMORTIZACION (Entra al banco)
                    elif "debolucion" in desc_lower or "devolucion" in desc_lower:
                        registrar_asiento(fecha, '110', '520', monto, desc)
                        count += 1
                        
                    # 3. PAGOS DE MATERIAS PRIMAS (Sale del banco, entra a Produccion 702)
                    elif "mat primas" in desc_lower or "pescado entero" in desc_lower or "prod pescado" in desc_lower:
                        registrar_asiento(fecha, '702', '110', monto, desc)
                        count += 1
                        
                    # 4. AMORTIZACION DE DEUDA (Sale del banco, baja pasivo 520)
                    elif "amortiz deuda" in desc_lower:
                        registrar_asiento(fecha, '520', '110', monto, desc)
                        count += 1
                        
                    # 5. GASTOS OPERATIVOS (Salen del banco)
                    elif "onat" in desc_lower:
                        registrar_asiento(fecha, '855', '110', monto, desc)
                        count += 1
                    elif "salario" in desc_lower:
                        registrar_asiento(fecha, '601', '110', monto, desc)
                        count += 1
                    elif "serv juridico" in desc_lower or "servic juridico" in desc_lower:
                        registrar_asiento(fecha, '822', '110', monto, desc)
                        count += 1
                    elif "etecsa" in desc_lower:
                        registrar_asiento(fecha, '6015', '110', monto, desc)
                        count += 1
                    elif "uac" in desc_lower:
                        registrar_asiento(fecha, '871', '110', monto, desc)
                        count += 1
                    elif "nutrivida" in desc_lower:
                        registrar_asiento(fecha, '870', '110', monto, desc)
                        count += 1
                    elif "com" in desc_lower and "banc" in desc_lower:
                        registrar_asiento(fecha, '836', '110', monto, desc)
                        count += 1
                    elif "intereses bancarios" in desc_lower:
                        registrar_asiento(fecha, '836', '110', monto, desc)
                        count += 1
                    else:
                        # Cualquier otra salida se va a Gastos Generales
                        registrar_asiento(fecha, '822', '110', monto, desc)
                        count += 1
                        
                except Exception as e:
                    continue
                    
        print(f"Total de filas importadas exitosamente: {count}")
        
    except FileNotFoundError:
        print("Error: No se encontro el archivo.")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    cargar_datos_real()
