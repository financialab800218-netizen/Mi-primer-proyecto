📘 ANEXO T: PLAN DE EJECUCION DE LAS 3 ETAPAS DEL AGENTE

Fecha: 28 septiembre 2026
Proposito: Hoja de ruta de 6 meses para construir el agente autonomo completo.

---

VISION GENERAL

El agente se construye en 3 etapas incrementales:

ETAPA 1 - Bebe (Mes 1)
- Memoria + documentos
- Existe cuando escribes
- Costo: 5 USD/mes

ETAPA 2 - Nino (Mes 2-3)
- Ojos + oidos (imagenes, audios, PDFs, webs)
- Costo: 13-20 USD/mes

ETAPA 3 - Joven (Mes 4-6)
- Manos + ejecucion (envia correos, actualiza Sheets, sube a Drive)
- Costo: 20-40 USD/mes

---

ETAPA 1 - EL BEBE

OBJETIVO
Asistente basico con memoria persistente y respaldo automatico.

DURACION
4 semanas

COMPONENTES
1. Cerebro: DeepSeek API
2. Memoria: Supabase
3. Interfaz: Bot Telegram
4. Respaldo: GitHub
5. Ejecucion: Termux

REQUISITOS
- Cuenta DeepSeek (crear)
- Saldo DeepSeek 5 USD (fondear)
- API Key DeepSeek (generar)
- Cuenta Telegram (ya tienes)
- Supabase conectado (ya funciona)
- Termux + Python (ya funciona)
- GitHub (ya funciona)

CRONOGRAMA SEMANAL

SEMANA 1: Desbloqueo
- Dia 1: Fondear DeepSeek 5 USD
- Dia 2: Generar API Key
- Dia 3: Configurar .env
- Dia 4: Crear Bot Telegram
- Dia 5: Instalar dependencias

SEMANA 2: Script del Bot
- Dia 1-2: Escribir bot.py
- Dia 3: Integrar Supabase
- Dia 4: Ejecutar con tmux
- Dia 5: Pruebas basicas

SEMANA 3: Respaldo Automatico
- Dia 1-2: Script backup.py
- Dia 3: Programar con cron
- Dia 4: Pruebas de respaldo
- Dia 5: Documentar

SEMANA 4: Ajustes y cierre
- Dia 1-3: Uso real
- Dia 4: Optimizacion
- Dia 5: Cerrar Etapa 1

COSTO
5 USD una vez (dura 6-12 meses)

RESULTADO
- Bot Telegram respondiendo 24/7
- Memoria persistente en Supabase
- Respaldo automatico diario
- Generacion de documentos

ESTADO ACTUAL
- Bot creado: OK
- bot.py funcional: OK
- tmux: OK
- wakelock: OK
- Fondear DeepSeek: PENDIENTE
- Integracion DeepSeek: PENDIENTE

Progreso: 85 por ciento

---

ETAPA 2 - EL NINO

OBJETIVO
Asistente multimodal con ojos y oidos. Procesa imagenes, audios, PDFs y webs.

DURACION
8 semanas

COMPONENTES NUEVOS
1. Vision: Gemini Pro Vision
2. Audicion: Whisper API (Groq gratis)
3. Video: Gemini 1.5 Pro
4. Lectura web: BeautifulSoup
5. Lectura PDFs: PyPDF2
6. Memoria vectorial: Supabase pgvector
7. Orquestador: n8n autoalojado

REQUISITOS
- Etapa 1 completada
- Cuenta Google (ya tienes)
- API Key Gemini (gratis)
- API Key Groq (gratis)
- VPS Hetzner 5.60 USD/mes
- pgvector activado

CRONOGRAMA SEMANAL

SEMANA 5-6: Vision (Gemini)
- API Key Gemini
- Script analisis de imagenes
- Integracion con Telegram

SEMANA 7-8: Audicion (Whisper)
- API Key Groq
- Script transcripcion
- Integracion con Telegram

SEMANA 9-10: PDFs y Webs
- Lectura PDFs
- Scraping webs
- Integracion

SEMANA 11-12: n8n y Vectorial
- Contratar VPS Hetzner
- Instalar n8n
- Activar pgvector en Supabase

COSTO MENSUAL
13-20 USD

RESULTADO
- Bot que ve imagenes
- Bot que transcribe audios
- Bot que lee PDFs y webs
- n8n autoalojado 24/7
- Busqueda semantica

---

ETAPA 3 - EL JOVEN

OBJETIVO
Asistente con manos. Ejecuta tareas por ti.

DURACION
12 semanas

COMPONENTES NUEVOS
1. Gmail API (enviar correos)
2. Google Sheets API (registrar datos)
3. Google Drive API (subir archivos)
4. GitHub Actions (automatizacion)
5. WhatsApp Business (alternativa)
6. Multiples agentes especializados

REQUISITOS
- Etapa 2 completada
- Service Account de Google
- APIs habilitadas
- GitHub Actions configurado

CRONOGRAMA SEMANAL

SEMANA 13-14: Gmail API
- Service Account
- Script envio de correos
- Integracion

SEMANA 15-16: Sheets + Drive
- APIs habilitadas
- Funciones de lectura/escritura
- Backup automatico

SEMANA 17-18: GitHub Actions
- Workflows
- Backup diario
- Deploy automatico

SEMANA 19-20: WhatsApp alternativa
- Investigar Evolution API
- Probar o descartar
- Mantener Telegram optimizado

SEMANA 21-24: Multi-agentes
- Agente Comercial
- Agente Financiero
- Agente Educativo
- Integracion

COSTO MENSUAL
20-40 USD

RESULTADO
- Bot que envia correos
- Bot que actualiza Sheets/Drive
- GitHub Actions funcionando
- WhatsApp integrado (o alternativa)
- Multi-agentes operando

---

RESUMEN GENERAL

| Etapa | Duracion | Costo/mes | Resultado |
|-------|----------|-----------|-----------|
| 1 - Bebe | 4 semanas | 5 USD | Asistente basico |
| 2 - Nino | 8 semanas | 13-20 USD | Asistente multimodal |
| 3 - Joven | 12 semanas | 20-40 USD | Asistente ejecutor |
| TOTAL | 6 meses | 20-40 USD | Equipo completo |

---

BLOQUEANTES ACTUALES

1. Fondear DeepSeek 5 USD
   - Opcion A: ggsel.net (24h, fee 40 por ciento)
   - Opcion B: Lobato (proximo fin de semana)
   - Opcion C: VISA recuperada (bloqueada por CardCentral)

2. VPS Hetzner 5.60 USD/mes
   - Requiere tarjeta internacional
   - Alternativa: Oracle Cloud Free (gratis, inestable)

3. API Key OpenAI Whisper
   - Alternativa: Groq (gratis)

4. WhatsApp Business API
   - Meta bloquea Cuba
   - Alternativa: Evolution API autoalojada

---

COMO BUSCAR LO QUE FALTA

DEEPSEEK 5 USD:
- ggsel.net
- Esperar a Lobato
- Binance P2P

VPS HETZNER:
- QvaPay a VISA
- Binance a USDT
- Oracle Cloud Free

API KEY WHISPER:
- Groq (console.groq.com)

WHATSAPP:
- Evolution API (autoalojada)
- Baileys (no oficial, riesgo)
- Mantener Telegram

---

PROXIMOS PASOS INMEDIATOS

CORTO PLAZO (esta semana):
1. Fondear DeepSeek
2. Integrar DeepSeek en bot.py
3. Rotar credenciales expuestas

MEDIANO PLAZO (este mes):
4. Completar Etapa 1 al 100 por ciento
5. Iniciar Etapa 2 (Vision Gemini)
6. Contratar VPS Hetzner

LARGO PLAZO (3-6 meses):
7. Completar Etapa 2
8. Iniciar Etapa 3
9. Multi-agentes operando

---

FIN DEL ANEXO T
