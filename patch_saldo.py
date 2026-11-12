with open('tools.py', 'r') as f:
    c = f.read()

# 1. Inyectar en TOOLS_SCHEMA (el menu)
schema_add = '''
TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "consultar_saldo",
        "description": "Consulta el saldo actual de una cuenta contable (ej: 110 para banco).",
        "parameters": {
            "type": "object",
            "properties": {
                "codigo_cuenta": {"type": "string", "description": "Codigo de la cuenta (ej: 110, 900)"}
            },
            "required": ["codigo_cuenta"]
        }
    }
})
'''
if 'consultar_saldo' not in c:
    c += schema_add

# 2. Inyectar en ejecutar_herramienta (la logica)
logica_add = '''
    elif nombre == "consultar_saldo":
        from contabilidad import obtener_saldo_cuenta
        return obtener_saldo_cuenta(argumentos.get("codigo_cuenta"))
'''

target = 'elif nombre == "ver_estado_resultados":'
if 'consultar_saldo' not in c:
    # Insertamos antes del elif de estado de resultados
    if target in c:
        c = c.replace(target, logica_add + '    ' + target)

with open('tools.py', 'w') as f:
    f.write(c)
print("OK: Herramienta de saldo conectada a la IA.")
