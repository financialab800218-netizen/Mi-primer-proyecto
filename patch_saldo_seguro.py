with open('tools.py', 'r') as f:
    code = f.read()

# 1. Aseguramos que el schema esté (ya lo vimos en captura, pero por si acaso)
if 'consultar_saldo' not in code:
    schema = '''
TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "consultar_saldo",
        "description": "Consulta el saldo actual de una cuenta contable.",
        "parameters": {
            "type": "object",
            "properties": {
                "codigo_cuenta": {"type": "string", "description": "Codigo de la cuenta (ej: 110)"}
            },
            "required": ["codigo_cuenta"]
        }
    }
})
'''
    code += schema

# 2. Aseguramos la logica de ejecucion
# Buscamos el final de la funcion ejecutar_herramienta (el ultimo return)
target = 'return f"[Error] Herramienta desconocida: {nombre}"'
inject = '''
    elif nombre == "consultar_saldo":
        from contabilidad import obtener_saldo_cuenta
        return obtener_saldo_cuenta(argumentos.get("codigo_cuenta"))
'''

if 'elif nombre == "consultar_saldo":' not in code:
    if target in code:
        code = code.replace(target, inject + '\n    ' + target)
        print("OK: Logica de consultar_saldo inyectada correctamente.")
    else:
        print("ERROR: No se encontro el final de la funcion. Revisar manualmente.")
else:
    print("INFO: La logica ya estaba inyectada.")

with open('tools.py', 'w') as f:
    f.write(code)
