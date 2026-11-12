import re

# 1. Crear la función que lee el manual en reporte_contable.py
ruta_rep = '/root/Mi-primer-proyecto/reporte_contable.py'
with open(ruta_rep, 'r', encoding='utf-8') as f:
    codigo_rep = f.read()

if "def consultar_manual_contable" not in codigo_rep:
    codigo_rep += '''

def consultar_manual_contable():
    """Devuelve las reglas contables básicas para el agente."""
    with open('/root/Mi-primer-proyecto/manual_contable.txt', 'r', encoding='utf-8') as f:
        return f.read()
'''
    with open(ruta_rep, 'w', encoding='utf-8') as f:
        f.write(codigo_rep)
    print("✅ Función consultar_manual_contable creada.")

# 2. Inyectar la herramienta en tools.py
ruta_tools = '/root/Mi-primer-proyecto/tools.py'
with open(ruta_tools, 'r', encoding='utf-8') as f:
    codigo_tools = f.read()

# Añadir al esquema
nuevo_schema = '''
TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "consultar_manual_contable",
        "description": "Consulta el manual de contabilidad para saber cómo registrar salarios, gastos, ingresos o cierres.",
        "parameters": {"type": "object", "properties": {}}
    }
})
'''

if '"name": "consultar_manual_contable"' not in codigo_tools:
    codigo_tools = codigo_tools.replace('TOOLS_SCHEMA = []', 'TOOLS_SCHEMA = []\n' + nuevo_schema)
    
    # Añadir la ejecución
    nueva_ejecucion = '''
    elif nombre == "consultar_manual_contable":
        from reporte_contable import consultar_manual_contable
        return consultar_manual_contable()
'''
    codigo_tools = codigo_tools.replace('    else:\n        return f"[Error] Herramienta desconocida: {nombre}"', nueva_ejecucion + '    else:\n        return f"[Error] Herramienta desconocida: {nombre}"')
    
    with open(ruta_tools, 'w', encoding='utf-8') as f:
        f.write(codigo_tools)
    print("✅ Herramienta 'consultar_manual_contable' inyectada en tools.py.")
