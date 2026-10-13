# Fix del bot Telegram - 13 octubre 2026

## Problema
El bot decia "IA pendiente: fondear DeepSeek $5" al recibir mensajes.

## Causa raiz
El bot_multiagent.py NO usa llm_router.py. Tiene su PROPIA logica:
- Lee DEEPSEEK_API_KEY del .env
- Si la key tiene mas de 20 caracteres, marca IA como activa
- Si no, devuelve el mensaje "IA pendiente"

El .env tenia DEEPSEEK_API_KEY comentado, por eso el bot siempre decia "IA pendiente".

## Solucion
Poner la key de NVIDIA en DEEPSEEK_API_KEY y apuntar DEEPSEEK_BASE_URL a NVIDIA.

Variables cambiadas en .env:
- DEEPSEEK_API_KEY=nvapi-*** (key de NVIDIA)
- DEEPSEEK_BASE_URL=https://integrate.api.nvidia.com/v1

## Resultado
Bot de Telegram funciona con IA real.

## Pendiente
- generar_imagen y generar_video fallan con "[Error conexion:]"
- Hay un except silencioso que no loguea el error
- Investigar con mas calma

## Comandos utiles
- Ver logs bot: journalctl -u tutoria-bot.service --no-pager -n 50
- Ver logs backend: journalctl -u tutoria-backend.service --no-pager -n 50
- Reiniciar bot: systemctl restart tutoria-bot.service

## Leccion aprendida
Cuando un bot dice "no tengo X", revisar QUE ARCHIVO usa realmente.
No siempre es el que editamos.
bot_multiagent.py y llm_router.py son DOS sistemas diferentes.
