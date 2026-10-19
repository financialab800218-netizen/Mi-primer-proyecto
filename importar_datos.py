import csv
from contabilidad import registrar_asiento

def cargar_datos_csv():
    print("Iniciando lectura del archivo CSV...")
    archivo = 'datos 2026.csv'
    count = 0
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            # Saltamos las primeras 4 filas (titulos y encabezados)
            for _ in range(4):
                next(reader, None)
                
            for row in reader:
                if not row or len(row) < 10:
                    continue
                
                try:
                    # 1. Extraer Fecha (D y M)
                    dia = row[0].strip()
                    mes = row[1].strip()
                    descripcion = row[8].strip()
                    
                    # Si no hay dia, mes o descripcion, saltamos la fila
                    if not dia or not mes or not descripcion or descripcion == '""':
                        continue
                    
                    # Formatear fecha (asumiendo año 2026)
                    fecha = f"2026-{int(mes):02d}-{int(dia):02d}"
                    
                    # 2. Extraer el Monto (Buscamos el último número válido en la fila)
                    monto = 0.0
                    for valor in reversed(row):
                        valor = valor.strip().replace('"', '')
                        if valor:
                            try:
                                monto = float(valor)
                                break
                            except ValueError:
                                pass
                    
                    if monto > 0:
                        # 3. Determinar si es Ingreso o Gasto por la descripción
                        desc_lower = descripcion.lower()
                        if "ingr" in desc_lower or "venta" in desc_lower or "cobro" in desc_lower:
                            # Es un INGRESO (Debito Banco, Credito Ventas)
                            cuenta_debito = "110"
                            cuenta_credito = "900"
                        else:
                            # Es un GASTO o PAGO (Debito Gastos, Credito Banco)
                            cuenta_debito = "822" # Gastos generales por defecto
                            cuenta_credito = "110"
                        
                        # IMPRIMIR PREVISUALIZACION (No guardar aun)
                        print(f"[PREVIEW] Fecha: {fecha} | Monto: {monto:,.2f} | Desc: {descripcion[:40]}...")
                        count += 1
                        
                        # DESCOMENTA LA SIGUIENTE LINEA CUANDO ESTEMOS SEGUROS
                        registrar_asiento(fecha, cuenta_debito, cuenta_credito, monto, descripcion)
                        
                except Exception as e:
                    continue
                    
        print(f"\nTotal de filas procesadas exitosamente: {count}")
        
    except FileNotFoundError:
        print("Error: No se encontro el archivo 'datos 2026.csv'")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    cargar_datos_csv()
