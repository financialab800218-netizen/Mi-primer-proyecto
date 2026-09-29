📘 ANEXO S: BOT TELEGRAM FUNCIONAL

Fecha: 28 septiembre 2026
Estado: OPERATIVO
Commit inicial: 449f1d1

---

PARTE I: DESCRIPCION

El bot @tutoria_cuba_bot es el asistente oficial del proyecto TutorIA Cuba en Telegram.

Funciona 24/7 dentro de tmux, con wakelock activado para sobrevivir bloqueos del telefono.

---

PARTE II: DATOS DEL BOT

- Nombre visible: TutorIA Cuba Assistant
- Username: @tutoria_cuba_bot
- URL: https://t.me/tutoria_cuba_bot
- Token: Guardado en .env como TELEGRAM_BOT_TOKEN
- Creado con: @BotFather en Telegram

---

PARTE III: COMANDOS DISPONIBLES

/start
- Muestra el menu principal
- Lista los comandos disponibles

/status
- Muestra el estado del sistema
- Indica si DeepSeek esta activo
- Indica si Supabase esta conectado
- Indica si GitHub esta activo

/maestro
- Muestra informacion del proyecto
- Lista las 5 direcciones y sus areas
- Muestra contacto

/ayuda
- Explica como usar el bot
- Indica que falta para IA real

Cualquier otro texto
- Responde con mensaje de placeholder
- Cuando DeepSeek este fondeado, respondera con IA real

---

PARTE IV: ARQUITECTURA

El bot esta construido en Python con python-telegram-bot.

Componentes:
1. bot.py (script principal en ~/tutoria-cuba/)
2. .env con credenciales (TELEGRAM_BOT_TOKEN)
3. tmux session llamada "bot" para persistencia
4. termux-wake-lock para evitar que MIUI cierre Termux

Flujo:
Telegram -> Bot API -> bot.py -> respuesta

Proximamente:
Telegram -> bot.py -> DeepSeek API -> respuesta con IA

---

PARTE V: PROCESO DE CREACION

PASO 1: BotFather
- Abrir Telegram
- Buscar @BotFather
- Enviar /newbot
- Nombre: TutorIA Cuba Assistant
- Username: tutoria_cuba_bot
- BotFather entrega token

PASO 2: Guardar token
- Editar backend/app/.env
- Anadir TELEGRAM_BOT_TOKEN=...
- Anadir TELEGRAM_BOT_USERNAME=tutoria_cuba_bot
- Anadir TELEGRAM_BOT_URL=https://t.me/tutoria_cuba_bot

PASO 3: Script bot.py
- Instalar python-telegram-bot
- Instalar python-dotenv
- Crear script con comandos

PASO 4: Ejecutar
- python bot.py
- Escuchando mensajes

PASO 5: Persistencia
- tmux new -s bot
- python bot.py
- CTRL+B, D (detach)
- Bot sigue corriendo

PASO 6: Wakelock
- termux-wake-lock
- Evita que MIUI cierre Termux

---

PARTE VI: ESTADO ACTUAL

| Componente | Estado |
|------------|--------|
| Bot creado en BotFather | OK |
| Token en .env | OK |
| bot.py funcional | OK |
| Comandos /start /status /maestro /ayuda | OK |
| Ejecutando en tmux | OK |
| Wakelock activado | OK |
| Integracion DeepSeek | PENDIENTE |
| Respuestas con IA real | PENDIENTE |

---

PARTE VII: PENDIENTES

CORTO PLAZO:
1. Fondear DeepSeek (5 USD)
2. Integrar DeepSeek API en bot.py
3. Actualizar comando /status para reflejar IA activa

MEDIANO PLAZO:
4. Anadir comandos mas avanzados
5. Integrar guardado en Supabase (tabla conversaciones)
6. Anadir soporte para imagenes y audios

LARGO PLAZO:
7. Multiples agentes (comercial, financiero, educativo)
8. Integracion con otras direcciones

---

PARTE VIII: COMANDOS DE MANTENIMIENTO

Ver si el bot esta corriendo:
tmux ls

Entrar a la sesion del bot:
tmux attach -t bot

Salir de la sesion sin cerrar el bot:
CTRL+B, luego D

Detener el bot:
tmux attach -t bot
CTRL+C

Reiniciar el bot:
tmux attach -t bot
cd ~/tutoria-cuba
python bot.py
CTRL+B, D

---

PARTE IX: LECCIONES APRENDIDAS

1. BotFather puede tener usernames ya tomados
   - Probar variantes si el primero falla

2. tmux es esencial para persistencia
   - Sin tmux, el bot muere al cerrar Termux

3. Wakelock es esencial en MIUI
   - Sin wakelock, MIUI cierra Termux en segundo plano

4. Los tokens se exponen facil
   - El token del bot quedo visible en una captura
   - Accion pendiente: rotar en BotFather con /revoke

---

PARTE X: PROXIMO HITO

Integrar DeepSeek al bot.

Cuando DeepSeek este fondeado:
1. Actualizar bot.py con llamada a API
2. Reemplazar el "echo" por respuesta real
3. Probar con mensajes reales
4. Documentar en Anexo T

---

FIN DEL ANEXO S
