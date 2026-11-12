import os
import sys

print("🧪 INICIANDO TEST DE TODAS LAS HERRAMIENTAS...\n")

# 1. PROBAR GENERACIÓN DE EXCEL
print("--- 1. PRUEBA DE EXCEL ---")
try:
    from documentos import generar_excel_asientos
    # Creamos un archivo de prueba
    resultado = generar_excel_asientos()
    if "OK" in resultado or "http" in resultado:
        print(f"✅ Excel funciona: {resultado[:60]}...")
    else:
        print(f"❌ Excel falló: {resultado}")
except Exception as e:
    print(f"❌ Error importando Excel: {e}")

# 2. PROBAR GENERACIÓN DE WORD (CONTRATOS)
print("\n--- 2. PRUEBA DE CONTRATOS WORD ---")
try:
    from documentos_legales import generar_contrato_tcp
    resultado = generar_contrato_tcp("Profesor Prueba", "Secundaria", "Matemáticas", 10, 2000)
    if "OK" in resultado or "http" in resultado:
        print(f"✅ Contrato TCP funciona: {resultado[:60]}...")
    else:
        print(f"❌ Contrato falló: {resultado}")
except Exception as e:
    print(f"❌ Error importando Contrato: {e}")

# 3. PROBAR LECTURA DE ARCHIVOS (EXCEL/WORD)
print("\n--- 3. PRUEBA DE LECTURA DE DOCUMENTOS ---")
try:
    from documentos_legales import leer_documento
    # Intentamos leer un archivo que debería existir
    resultado = leer_documento("CONVENIO PRODUCCION COOPERADA CPA 17 M y PDL Aquaponica .docx")
    if "Error" not in resultado:
        print(f"✅ Lectura de Word funciona. (Extracto: {resultado[:50]}...)")
    else:
        print(f"⚠️ No encontró el archivo exacto, pero la función responde: {resultado[:60]}")
except Exception as e:
    print(f"❌ Error leyendo documento: {e}")

# 4. PROBAR GENERACIÓN DE IMÁGENES (AGNES)
print("\n--- 4. PRUEBA DE IMAGEN CON AGNES ---")
try:
    from herramientas_media import generar_imagen
    # Llamamos a la función de imagen (esto puede tardar unos segundos)
    resultado = generar_imagen("Un pelícano montado en un bote de madera, estilo acuarela")
    if "OK" in resultado or "http" in resultado:
        print(f"✅ Generación de Imagen funciona: {resultado[:80]}...")
    else:
        print(f"⚠️ Respuesta de imagen: {resultado[:100]}")
except Exception as e:
    print(f"❌ Error generando imagen: {e}")

# 5. PROBAR HERRAMIENTAS CONTABLES
print("\n--- 5. PRUEBA DE CONTABILIDAD ---")
try:
    from reporte_contable import obtener_balance_general
    balance = obtener_balance_general()
    if "BALANCE" in balance:
        print("✅ Generación de Balance funciona.")
    else:
        print(f"❌ Falló el balance: {balance[:100]}")
except Exception as e:
    print(f"❌ Error en balance: {e}")

print("\n✅ TEST FINALIZADO.")
