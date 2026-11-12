import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# IMPORTANTE: Reemplaza 'TutoriaCubaAssistant' por el nombre real de tu bot (sin la @)
nombre_real = 'TutoriaCubaAssistant' 

# Buscamos cualquier enlace de Telegram viejo y lo reemplazamos por el nuevo
html = re.sub(r'https://t\.me/[^\'\"]*', f'https://t.me/{nombre_real}', html)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Enlaces actualizados al bot: @{nombre_real}")
