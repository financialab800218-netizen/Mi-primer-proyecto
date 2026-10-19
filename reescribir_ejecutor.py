import re

with open('tools.py', 'r') as f:
    code = f.read()

# Bloque de la nueva funcion ejecutar_herramienta
nueva_funcion = '''def ejecutar_herramienta(nombre, argumentos):
    if nombre == "leer_archivo":
        return leer_archivo(argumentos.get("ruta", ""))
    elif nombre == "listar_archivos":
        return listar_archivos(argumentos.get("carpeta", "."))
    elif nombre == "buscar_texto":
        return buscar_texto(argumentos.get("patron", ""), argumentos.get("carpeta", "docs"))
    elif nombre == "escribir_archivo":
        return escribir_archivo(argumentos.get("ruta", ""), argumentos.get("contenido", ""))
    elif nombre == "crear_carpeta":
        return crear_carpeta(argumentos.get("ruta", ""))
    elif nombre == "registrar_movimiento_contable":
        from contabilidad import registrar_asiento
        return registrar_asiento(
            fecha=argumentos.get("fecha"),
            cuenta_debito=argumentos.get("cuenta_debito"),
            cuenta_credito=argumentos.get("cuenta_credito"),
            monto=argumentos.get("monto"),
            descripcion=argumentos.get("descripcion")
        )
    elif nombre == "ver_estado_resultados":
        from contabilidad import obtener_estado_resultados
        return obtener_estado_resultados(
            fecha_inicio=argumentos.get("fecha_inicio"),
            fecha_fin=argumentos.get("fecha_fin")
        )
    elif nombre == "consultar_saldo":
        from contabilidad import obtener_saldo_cuenta
        return obtener_saldo_cuenta(argumentos.get("codigo_cuenta"))
    else:
        return f"[Error] Herramienta desconocida: {nombre}"
'''

# Buscamos la funcion actual y la reemplazamos
pattern = re.compile(r'def ejecutar_herramienta\(nombre, argumentos\):.*?(?=\ndef |\nTOOLS_SCHEMA|\Z)', re.DOTALL)
match = pattern.search(code)

if match:
    code = code[:match.start()] + nueva_funcion + code[match.end():]
    with open('tools.py', 'w') as f:
        f.write(code)
    print("OK: Funcion ejecutar_herramienta reescrita con exito. Todas las herramientas conectadas.")
else:
    print("ERROR: No se encontro la definicion de ejecutar_herramienta.")
