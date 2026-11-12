with open('tools.py', 'r') as f:
    lines = f.readlines()

insert_idx = -1
for i, line in enumerate(lines):
    if 'return crear_carpeta(argumentos.get("ruta", ""))' in line:
        insert_idx = i
        break

if insert_idx != -1:
    # Verificamos si ya inyectamos en la funcion (no en el schema)
    if any('elif nombre == "registrar_movimiento_contable":' in l for l in lines):
        print("INFO: La logica ya estaba inyectada en la funcion.")
    else:
        new_lines = [
            '    elif nombre == "registrar_movimiento_contable":\n',
            '        from contabilidad import registrar_asiento\n',
            '        return registrar_asiento(\n',
            '            fecha=argumentos.get("fecha"),\n',
            '            cuenta_debito=argumentos.get("cuenta_debito"),\n',
            '            cuenta_credito=argumentos.get("cuenta_credito"),\n',
            '            monto=argumentos.get("monto"),\n',
            '            descripcion=argumentos.get("descripcion")\n',
            '        )\n',
            '    elif nombre == "ver_estado_resultados":\n',
            '        from contabilidad import obtener_estado_resultados\n',
            '        return obtener_estado_resultados(\n',
            '            fecha_inicio=argumentos.get("fecha_inicio"),\n',
            '            fecha_fin=argumentos.get("fecha_fin")\n',
            '        )\n'
        ]
        # Insertamos justo despues de la linea de crear_carpeta
        lines = lines[:insert_idx+1] + new_lines + lines[insert_idx+1:]
        with open('tools.py', 'w') as f:
            f.writelines(lines)
        print("OK: Logica inyectada quirurgicamente en ejecutar_herramienta.")
else:
    print("ERROR: No se encontro la linea exacta.")
