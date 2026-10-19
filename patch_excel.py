import re

with open('tools.py', 'r') as f:
    code = f.read()

# 1. Agregar al TOOLS_SCHEMA
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
if 'generar_excel_contabilidad' not in code:
    code += schema_add

# 2. Agregar la logica a ejecutar_herramienta
logica_add = '''
    elif nombre == "generar_excel_contabilidad":
        from documentos import generar_excel_asientos
        return generar_excel_asientos()
'''

# Inyectar antes del else final
target = 'return f"[Error] Herramienta desconocida: {nombre}"'
if target in code and 'generar_excel_contabilidad' not in code:
    code = code.replace(target, logica_add + '    ' + target)

with open('tools.py', 'w') as f:
    f.write(code)
print("OK: Herramienta Excel conectada.")
