import re

ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

# 1. Leer el HTML
with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Conectar el botón "Recargar" con el Bot de Telegram
# Buscamos el botón y le añadimos la acción de abrir Telegram
html = html.replace(
    '<button class="btn btn-primary">Recargar</button>',
    '<button class="btn btn-primary" onclick="window.open(\'https://t.me/TutoriaCubaAssistant\', \'_blank\')">Recargar</button>'
)

# 3. Conectar el botón "Retirar" con el Bot de Telegram también
html = html.replace(
    '<button class="btn btn-secondary">Retirar</button>',
    '<button class="btn btn-secondary" onclick="window.open(\'https://t.me/TutoriaCubaAssistant\', \'_blank\')">Retirar</button>'
)

# 4. Conectar el botón "Crear Nuevo Curso" con el Bot de Telegram
html = html.replace(
    '<button class="btn btn-primary" style="width: 100%;">Crear Nuevo Curso</button>',
    '<button class="btn btn-primary" style="width: 100%;" onclick="window.open(\'https://t.me/TutoriaCubaAssistant\', \'_blank\')">Crear Nuevo Curso</button>'
)

# 5. Guardar el archivo
with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ ¡Botones conectados al Bot de Telegram con éxito!")
print("   -> Al tocar Recargar, Retirar o Crear Curso, se abrirá el chat del bot.")
