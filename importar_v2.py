import csv
from contabilidad import supabase, registrar_asiento

def cargar_datos_inteligente():
    print("Iniciando lectura quirurgica del CSV...")
    archivo = 'datos 2026.csv'
    
    # 1. Obtener los IDs de los centros de costo reales
    centros_res = supabase.table('centros_costo').select('id', 'nombre').execute()
    cc = {item['nombre']: item['id'] for item in centros_res.data}
    
    count = 0
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Saltamos las 4 primeras filas de encabezados
            for _ in range(4): next(reader, None)
                
            for row in reader:
                if not row or len(row) < 9: continue
                
                try:
                    dia = row[0].strip()
                    mes = row[1].strip()
                    desc = row[8].strip()
                    
                    if not dia or not mes or not desc or desc == '""': continue
                    
                    fecha = f"2026-{int(mes):02d}-{int(dia):02d}"
                    
                    # Extraer el monto (buscamos el último número válido)
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
                    cta_debe = "822" 
                    cta_haber = "110" 
                    centro_costo = cc.get('PDL_DESSPEZ_GENERAL', 1)
                    
                    if "ingr" in desc_lower or "venta" in desc_lower or "cobro de venta" in desc_lower:
                        cta_debe = "110"
                        cta_haber = "900"
                        if "pescado" in desc_lower or "filet" in desc_lower:
                            centro_costo = cc.get('Procesado_Pescado', 1)
                        elif "pienso" in desc_lower:
                            centro_costo = cc.get('Pienso_Criollo', 1)
                    elif "cobro de intereses" in desc_lower:
                        cta_debe = "110"
                        cta_haber = "920"
                    elif "debolucion de la amortizacion" in desc_lower:
                        cta_debe = "110"
                        cta_haber = "520" 
                    elif "amortiz deuda" in desc_lower:
                        cta_debe = "520"
                        cta_haber = "110"
                    elif "onat" in desc_lower:
                        cta_debe = "855"
                    elif "salario" in desc_lower:
                        cta_debe = "601"
                    elif "comision" in desc_lower or "com banc" in desc_lower or "comic banc" in desc_lower:
                        cta_debe = "836"
                    elif "uac" in desc_lower:
                        cta_debe = "871"
                    elif "nutrivida" in desc_lower:
                        cta_debe = "870"
                    elif "versat" in desc_lower:
                        cta_debe = "826"
                    elif "etecsa" in desc_lower:
                        cta_debe = "6015"
                    elif "pago de pescado entero" in desc_lower or "mat primas" in desc_lower:
                        cta_debe = "810"
                        centro_costo = cc.get('Procesado_Pescado', 1)
                    
                    if "aquaponica" in desc_lower or "aquapónica" in desc_lower:
                        centro_costo = cc.get('Inversion_Fideicomiso_Construccion', 1) # Ajustado a un centro real

                    registrar_asiento(fecha, cta_debe, cta_haber, monto, desc, centro_costo)
                    count += 1
                    
                except Exception as e:
                    pass
                    
        print(f"Total de filas importadas exitosamente: {count}")
        
    except FileNotFoundError:
        print("Error: No se encontro el archivo 'datos 2026.csv'")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    cargar_datos_inteligente()
