with open('tools.py', 'r') as f:
    lines = f.readlines()

# 1. Eliminamos cualquier linea que contenga 'TOOLS_SCHEMA = []' que haya quedado mal puesta
lines = [l for l in lines if not l.strip() == 'TOOLS_SCHEMA = []']

# 2. La insertamos al principio (despues de los imports)
inserted = False
for i, line in enumerate(lines):
    if line.startswith('def ') or line.startswith('class '):
        lines.insert(i, 'TOOLS_SCHEMA = []\n\n')
        inserted = True
        break

if not inserted:
    lines.insert(0, 'TOOLS_SCHEMA = []\n\n')

with open('tools.py', 'w') as f:
    f.writelines(lines)
print("OK: TOOLS_SCHEMA reparado en la cabecera del archivo.")
