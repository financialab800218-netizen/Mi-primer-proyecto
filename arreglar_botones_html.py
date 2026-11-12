import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# Reemplazamos los botones por enlaces HTML directos (más estables en móviles)
html = html.replace(
    '<button class="btn btn-primary" onclick="window.open(\'https://t.me/TutorIACubaAssistant_bot\', \'_blank\')">Recargar</button>',
    '<a href="https://t.me/TutorIACubaAssistant_bot" target="_blank" class="btn btn-primary" style="text-decoration: none; display: inline-block; text-align: center;">Recargar</a>'
)

html = html.replace(
    '<button class="btn btn-secondary" onclick="window.open(\'https://t.me/TutorIACubaAssistant_bot\', \'_blank\')">Retirar</button>',
    '<a href="https://t.me/TutorIACubaAssistant_bot" target="_blank" class="btn btn-secondary" style="text-decoration: none; display: inline-block; text-align: center;">Retirar</a>'
)

html = html.replace(
    '<button class="btn btn-primary" style="width: 100%;" onclick="window.open(\'https://t.me/TutorIACubaAssistant_bot\', \'_blank\')">Crear Nuevo Curso</button>',
    '<a href="https://t.me/TutorIACubaAssistant_bot" target="_blank" class="btn btn-primary" style="text-decoration: none; display: block; width: 100%; text-align: center; box-sizing: border-box;">Crear Nuevo Curso</a>'
)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Botones convertidos a enlaces HTML directos.")
