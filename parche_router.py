import re

path = 'llm_router.py'
with open(path, 'r') as f:
    code = f.read()

# Buscamos la línea exacta de ejecutar_herramienta capturando sus espacios
pattern = r'^(\s*)resultado = ejecutar_herramienta\(nombre, args\)'
match = re.search(pattern, code, re.MULTILINE)

if match:
    indent = match.group(1)
    # Construimos el bloque de intercepción con la misma indentación
    block = f"\n{indent}if isinstance(resultado, str) and resultado.startswith(\"[MENU_VIDEO]\"):\n{indent}    return resultado\n"
    
    insert_pos = match.end()
    code = code[:insert_pos] + block + code[insert_pos:]
    
    with open(path, 'w') as f:
        f.write(code)
    print("OK: Cortocircuito inyectado en llm_router.py")
else:
    print("ERROR: No se encontro la linea exacta")
