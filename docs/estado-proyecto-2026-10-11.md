# Estado del Proyecto — 11 Octubre 2026

## Contexto
- Usuario: Yosbel Collazo Ávila (Bejucal, Mayabeque, Cuba)
- Proyecto: Ecosistema Mayabeque + TutorIA Cuba
- Sesión: 8 horas de trabajo intensivo
- Estado: Sistema en producción

## Infraestructura

### VPS EQVPS
- IP: 65.109.60.70
- Puerto SSH: 20705
- Usuario: root
- Plan: Nano NAT — 3 USD/mes
- Ubuntu 24.04 LTS
- Ubicación: Alemania (UE)
- Pagado hasta: 8 noviembre 2026
- Disco: 13.49 GB (20 por ciento usado)
- Pendiente: reinicio del sistema

### Servicios systemd activos
- tutoria-bot.service (bot Telegram)
- tutoria-backend.service (FastAPI puerto 8000)
- tutoria-tunnel.service (Cloudflare Tunnel)
- tunel-update.timer (auto-actualizacion cada 5 min)

## Bot Telegram
- Usuario: @tutoria_cuba_bot
- 7 agentes: /pablo /ernesto /marta /camilo /celia /julian /ruben
- Comandos: /start /ayuda /quien /salir

## IA Multi-proveedor

### NVIDIA NIM (principal)
- URL: https://integrate.api.nvidia.com/v1
- Modelo: openai/gpt-oss-20b
- Costo: gratis

### Groq (respaldo)
- URL: https://api.groq.com/openai/v1
- Modelo: openai/gpt-oss-120b
- Costo: gratis

### Agnes AI (NUEVO 11 oct)
- URL: https://apihub.agnes-ai.com/v1
- AGNES_MODEL=agnes-2.5-flash
- AGNES_IMAGE_MODEL=agnes-image-2.5-flash
- AGNES_VIDEO_MODEL=agnes-video-2.5-flash
- Modelos: agnes-3.0-flash, agnes-3.0-flash-max, agnes-2.5-flash, agnes-2.5-pro, agnes-2.5-pro-beta, agnes-image-2.1-flash, agnes-image-2.0-flash, agnes-image-2.5-flash, agnes-video-2.5-flash, agnes-video-2.5

## Base de Datos Supabase
- Proyecto: tutoria ia cuba
- URL: https://ktdpxyqpghipmsftepgl.supabase.co
- 7 tablas: usuarios, tcp_perfiles, contenido, conversaciones, pagos, suscripciones, certificados
- RLS: DESACTIVADO
- Usuarios: 3 registrados

## GitHub + PWA
- Repo: github.com/financialab800218-netizen/Mi-primer-proyecto
- URL publica: https://financialab800218-netizen.github.io/Mi-primer-proyecto/
- PWA en /docs/ (GitHub Pages)
- Codigo fuente PWA en /pwa/

## Estructura PWA
- index.html (login/registro)
- app.html (dashboard con menu)
- chat.html (chat con 7 agentes)
- manifest.json
- css/styles.css, css/chat.css
- js/app.js, js/chat.js

## Cloudflare Tunnel
- URL temporal (cambia al reiniciar)
- Script: /root/scripts/actualizar-tunel.sh
- Log: /var/log/tunel-update.log
- Timer actualiza cada 5 min

## Herramientas tools.py (9 activas)
1. leer_archivo
2. listar_archivos
3. buscar_texto
4. escribir_archivo
5. crear_carpeta
6. git_status
7. git_commit_push
8. generar_imagen (NUEVO - Agnes AI)
9. generar_video (NUEVO - Agnes AI)

## Backups
- /root/Mi-primer-proyecto/tools.py.bak-20261011-2024
- /root/Mi-primer-proyecto/llm_router.py.bak-20261011-2045

## Bug pendiente
- Sintoma: Error conexion choices al usar generar_imagen
- Causa: llm_router.py linea 31: msg = data["choices"][0]["message"] crashea si no hay choices
- Fix: comprobar con if choices not in data return None
- Metodo: usar VSCode Remote SSH (no nano desde movil)

## Vision sistema de contenido
- Profesor TCP es dueno de su contenido
- Sube Word/foto/video/texto
- Pide en lenguaje natural
- IA decide herramienta y genera
- Profesor revisa y publica
- IA valida y bloquea contenido prohibido

## Proximos pasos
Alta:
1. Arreglar bug choices del router
2. Probar generar_imagen con Agnes AI

Media:
3. Sistema de contenido para profesores
4. Menus internos de la PWA
5. Historial de conversaciones en Supabase
6. Panel admin

Baja:
7. Pagos EnZona/Transfermovil
8. Certificados PDF
9. Tunel permanente (requiere dominio)
10. WhatsApp

## Reglas
1. USDT solo TRON TRC20
2. API keys en .env jamas en repo
3. Dueno: Yosbel Telegram ID 5063025481
4. Documentar en docs/
5. Backup antes de tocar archivos criticos