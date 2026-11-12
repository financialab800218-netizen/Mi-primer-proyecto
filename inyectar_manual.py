import re

# 1. Leer el manual
with open('/root/Mi-primer-proyecto/manual_contable.txt', 'r', encoding='utf-8') as f:
    manual = f.read()

# 2. Leer el bot.py
with open('/root/Mi-primer-proyecto/bot.py', 'r', encoding='utf-8') as f:
    codigo = f.read()

# 3. Buscar donde se define el "system prompt" o el contexto de la IA
# Asumimos que hay una variable que define el comportamiento o un "system_prompt"
if "system_prompt" in codigo:
    # Si existe, lo actualizamos
    patron = r'system_prompt\s*=\s*".*?"'
    nuevo_prompt = f'system_prompt = """{manual}"""'
    codigo = re.sub(patron, nuevo_prompt, codigo, flags=re.DOTALL)
    print("✅ System prompt actualizado con el manual contable.")
else:
    # Si no existe, inyectamos el manual en la función principal
    print("⚠️ No se encontró 'system_prompt'. Inyectando manual en la memoria del bot.")
    # Buscamos la función de inicio y le inyectamos una variable global
    if "MANUAL_CONTABLE" not in codigo:
        codigo = codigo.replace('load_dotenv', 'MANUAL_CONTABLE = """' + manual + '"""\n\nload_dotenv')

# 4. Guardar cambios
with open('/root/Mi-primer-proyecto/bot.py', 'w', encoding='utf-8') as f:
    f.write(codigo)

print("✅ Archivo bot.py actualizado con la lógica contable.")
