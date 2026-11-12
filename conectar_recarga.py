ruta = '/root/Mi-primer-proyecto/backend/app/static/index.html'

with open(ruta, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Cambiamos el botón de Recargar para que abra recarga.html
html = html.replace(
    '<button class="btn btn-primary" onclick="window.open(\'https://t.me/TutorIACubaAssistant_bot\', \'_blank\')">Recargar</button>',
    '<a href="recarga.html" class="btn btn-primary" style="text-decoration: none; display: inline-block; text-align: center;">Recargar</a>'
)

# 2. Aseguramos que el botón de Retirar siga yendo a Telegram
html = html.replace(
    '<button class="btn btn-secondary" onclick="window.open(\'https://t.me/TutorIACubaAssistant_bot\', \'_blank\')">Retirar</button>',
    '<a href="https://t.me/TutorIACubaAssistant_bot" target="_blank" class="btn btn-secondary" style="text-decoration: none; display: inline-block; text-align: center;">Retirar</a>'
)

with open(ruta, 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Botón de Recargar conectado a la página de pago.")
