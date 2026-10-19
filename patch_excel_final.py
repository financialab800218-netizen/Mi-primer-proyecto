with open('tools.py', 'r') as f:
    code = f.read()

# 1. Inyectar en el Schema (El menu de la IA) si no esta
if 'generar_excel_contabilidad' not in code[:code.find('def ejecutar_herramienta')]:
    schema_add = '''
TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "generar_excel_contabilidad",
        "description": "Genera un archivo Excel con todos los asientos contables y devuelve el enlace de descarga.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
})
'''
    # Lo insertamos justo antes de la funcion ejecutar_herramienta
    match = code.find('def ejecutar_herramienta')
    if match != -1:
        code = code[:match] + schema_add + '\n' + code[match:]
        print("OK: Schema de Excel inyectado.")

# 2. Inyectar en la Logica si no esta
if 'elif nombre == "generar_excel_contabilidad":' not in code:
    logica_add = '''
    elif nombre == "generar_excel_contabilidad":
        from documentos import generar_excel_asientos
        return generar_excel_asientos()
'''
    target = 'return f"[Error] Herramienta desconocida: {nombre}"'
    if target in code:
        code = code.replace(target, logica_add + '\n    ' + target)
        print("OK: Logica de Excel inyectada.")

with open('tools.py', 'w') as f:
    f.write(code)
