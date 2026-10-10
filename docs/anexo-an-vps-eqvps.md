# Anexo AN — VPS EQVPS y Despliegue 24/7

## Fecha: 9-10 octubre 2026

## 1. Infraestructura
- Proveedor: EQVPS (eqvps.com)
- Plan: Nano NAT - $3/mes
- Pagado con: USDT TRON desde QvaPay
- Sistema: Ubuntu 24.04 LTS
- IP: 65.109.60.70 puerto SSH 20705
- Ubicacion: Alemania (UE)

## 2. Componentes instalados
- Python 3.12.3
- Git 2.43.0
- curl 8.5.0
- python-telegram-bot 22.8
- httpx 0.28.1
- python-dotenv 1.2.4

## 3. Servicio systemd
- Nombre: tutoria-bot.service
- Ubicacion: /etc/systemd/system/tutoria-bot.service
- Arranque: automatico al reiniciar VPS
- Reintentos: si falla, se reinicia cada 10 segundos

## 4. Estructura del bot
- Repo clonado en: /root/Mi-primer-proyecto
- Entorno virtual: /root/Mi-primer-proyecto/venv
- .env con claves en: backend/app/.env

## 5. Herramientas del agente
1. leer_archivo - Lee archivos del proyecto
2. listar_archivos - Lista archivos y carpetas
3. buscar_texto - Busca en documentos
4. escribir_archivo - Crea o modifica archivos (con auto-push a GitHub)
5. crear_carpeta - Crea carpetas nuevas
6. git_status - Estado del repo
7. git_commit_push - Commit y push manual

## 6. Auto-push a GitHub
Cada vez que un agente escribe un archivo, el bot automaticamente:
1. Guarda el archivo localmente
2. Hace git add
3. Hace git commit con mensaje Bot: actualizado <ruta>
4. Hace git push a origin main

## 7. API de IA
- Proveedor principal: NVIDIA NIM (integrate.api.nvidia.com)
- Modelo: openai/gpt-oss-20b
- Costo: 0 USD (tier gratuito)
- API alternativa pendiente: Groq (gratis) o DeepSeek (requiere $2)

## 8. Agentes activos
Pablo (Director Adjunto) - Clasifica y deriva
Ernesto (Contador Jefe Digital) - Finanzas
Marta (Asesora Legal) - Legal y ejecucion de archivos
Camilo (Ingeniero Agronomo) - Agricultura
Celia (Coordinadora Academica) - Educacion
Julian (Director Comercial) - Ventas
Ruben (Jefe de Mantenimiento) - Tecnico

## 9. Historial de commits importantes
- 5a22e15 Fase A completada: 7 herramientas operativas
- 28da09d FASE 1B: bot con tool calling + resumen automatico
- 2d5053d Fix: parche auto-push + archivos del bot
- cd65f3f Bot: actualizado docs/prueba-marta.md

## 10. Pendientes proximos
- Documentar integracion Groq
- Reforzar prompts por agente
- Sistema de autenticacion de usuarios
- Integracion WhatsApp (complejo)
- Dashboard web de administracion
- Sistema de pagos (Transfermovil/EnZona)