# 📖 LIBRO MAESTRO — TutorIA Cuba

> Punto de entrada al proyecto. Última actualización: 14-oct-2026

---

## 🎯 VISIÓN

Plataforma educativa cubana modular. 3 pilares:
- **TutorIA Cuba** — IA educativa con 7 agentes
- **Ecosistema Mayabeque** — asesoría productiva/legal/agro
- **Financialab** — consultoría financiera

## 👥 LOS 7 AGENTES

| Comando | Cargo |
|---|---|
| /pablo | Director Adjunto |
| /ernesto | Contador Jefe Digital |
| /marta | Asesora Legal |
| /camilo | Ingeniero Agrónomo |
| /celia | Coordinadora Académica |
| /julian | Director Comercial |
| /ruben | Jefe de Mantenimiento |

## 🏗️ ARQUITECTURA — 6 CAPAS

1. PRESENTACIÓN: Telegram · PWA
2. ORQUESTACIÓN: 7 agentes · Router IA · 9 tools
3. PROVEEDORES IA: NVIDIA (chat) · Agnes (imágenes) · PlataformIA (pendiente)
4. HERRAMIENTAS: 9 activas
5. ALMACENAMIENTO: Supabase · static/img · GitHub
6. TRANSPORTE: ngrok

## 📊 ESTADO TÉCNICO (14-oct-2026)

- VPS: 65.109.60.70:20705 ($3/mes)
- URL: lens-portside-masses.ngrok-free.dev
- Servicios: bot + backend + tunnel activos
- IA: NVIDIA chat + Agnes imágenes
- 9 bugs resueltos hoy

## 📁 ESTRUCTURA DEL PROYECTO

- `agents.py` — 7 agentes + reglas
- `llm_router.py` — router IA multi-proveedor
- `tools.py` — 9 herramientas
- `bot_multiagent.py` — bot Telegram
- `backend/app/` — FastAPI + PWA
- `docs/` — 77 documentos
- `scripts/` — automatizaciones

## 📚 DOCUMENTOS CLAVE

- `INVENTARIO.md` — lista completa de los 77 docs
- `maestro-v2.0.md` — documento maestro consolidado
- `anexo-aa-analisis-integral-proyecto.md` — análisis completo
- `anexo-m-mercado-educativo.md` — mercado educativo
- `estrategia/plan-escalado-2026-2027.md` — roadmap
- `anexo-14oct2026-fixes.md` — fixes recientes

## 💰 MODELO DE NEGOCIO

- Suscripciones: 500 CUP/mes por alumno
- Comisiones TCP: 10-20%
- Cursos premium: 500-1500 CUP
- Consultoría: 500-2000 CUP

Escalabilidad:
- 1-10 usuarios: $3/mes (actual)
- 30-100 usuarios: $40-60/mes (upgrade VPS + R2)
- 100-500 usuarios: $150-300/mes (distribuido)

## 🎯 PRÓXIMOS PASOS

1. Fix bug Marta (MAX_ITER + return explícito)
2. Rotar AGNES_API_KEY (seguridad)
3. Onboarding usuario
4. Sistema aprobación TCP
5. Migrar imágenes a Cloudflare R2

## 📜 REGLAS DEL PROYECTO

1. USDT solo TRON (TRC20)
2. API keys en `.env`, nunca en repo
3. Dueño: Yosbel (Telegram ID 5063025481)
4. Documentar en `docs/` con anexos
5. Backup antes de tocar archivos críticos
6. Verificar QUÉ archivo se ejecuta antes de debuggear
7. Revisar si el problema es del túnel antes de tocar código

## 🔗 VISIÓN (Yosbel)

> "Una plataforma educativa cubana donde profesores TCP crean
> contenido asistido por IA. Alumnos acceden desde Telegram y PWA.
> Todos los pagos vía Transfermóvil. Independiente de OFAC.
> **Nosotros somos una herramienta, no la solución.**"

---

**Regenerar inventario:** `python3 scripts/generar-inventario.py`

