import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# El nombre correcto del bot
nombre_real = 'TutorIACubaAssistant_bot'

# Reemplazamos cualquier enlace viejo de t.me por el correcto
html = re.sub(r'https://t\.me/[^\'\"]*', f'https://t.me/{nombre_real}', html)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Enlaces de la página web actualizados al bot real: @{nombre_real}")
