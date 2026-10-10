# Comandos del VPS TutorIA Cuba

Ultima actualizacion: 9 octubre 2026

## Datos del VPS
- IP: 65.109.60.70
- Puerto SSH: 20705
- Usuario: root
- Sistema: Ubuntu 24.04 LTS

## Conexion SSH
ssh root@65.109.60.70 -p 20705

## Servicio del bot (systemd)
- Ver estado detallado: systemctl status tutoria-bot.service
- Reiniciar: systemctl restart tutoria-bot.service
- Detener: systemctl stop tutoria-bot.service
- Arrancar: systemctl start tutoria-bot.service
- Estado simple: systemctl is-active tutoria-bot.service

## Logs del bot
- Ver en vivo: journalctl -u tutoria-bot.service -f
- Ultimas 50 lineas: journalctl -u tutoria-bot.service -n 50

## Repositorio GitHub
- Ver commits recientes: cd ~/Mi-primer-proyecto && git log --oneline -5
- Ver archivos modificados: cd ~/Mi-primer-proyecto && git status --short
- Actualizar desde GitHub: cd ~/Mi-primer-proyecto && git pull origin main
- Ver docs: ls ~/Mi-primer-proyecto/docs/

## Verificar herramientas del agente
cd ~/Mi-primer-proyecto && source venv/bin/activate && python3 -c "from tools import TOOLS_SCHEMA; [print(t['function']['name']) for t in TOOLS_SCHEMA]"

## Probar agente manualmente
cd ~/Mi-primer-proyecto && source venv/bin/activate && python3 agent.py "Hola"

## Agentes disponibles en Telegram
- /marta - Archivos, legal, documentos
- /ernesto - Contabilidad, finanzas
- /camilo - Agricultura, acuicultura
- /celia - Educacion
- /julian - Comercial, ventas
- /ruben - Mantenimiento, tecnico
- /pablo - Clasificacion general

## URLs utiles
- GitHub: github.com/financialab800218-netizen/Mi-primer-proyecto
- EQVPS: eqvps.com
- Telegram bot: t.me/tutoria_cuba_bot

## Costo mensual
- VPS EQVPS: 3 USD/mes
- IA NVIDIA: 0 USD (gratis)
- Total: 3 USD/mes

## Pendientes proximos
- Integrar Groq como respaldo
- Reforzar prompts por agente
- Explorar WhatsApp
- Sistema de pagos (Transfermovil/EnZona)
- Autenticacion de usuarios