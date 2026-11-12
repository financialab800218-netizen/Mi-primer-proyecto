docs/automatizacion/analisis-pendientes-automatizacion.md

# Analisis de Pendientes para Automatizacion - Ecosistema Mayabeque

Version: 1.0
Fecha: 3/octubre/2026
Autor: Yosbel Collazo Avila + Socio IA
Uso: Mapa completo de lo que falta para automatizar el ecosistema
Estado: ANALISIS COMPLETO
Documentos complementarios:
- anexo-s-bot-telegram.md
- anexo-t-plan-etapas.md
- anexo-q-cuerpo-agente-ia.md
- plan-escalado-2026-2027.md

---

## 1. Proposito

Definir el mapa completo de automatizacion del Ecosistema
Mayabeque. Distinguir entre lo que YA funciona, lo que esta
listo pero parado, y lo que hay que crear.

Objetivo: priorizar inversiones minimas para maximizar
automatizacion con recursos limitados.

---

## 2. Lo que YA Esta Automatizado

### 2.1 Documental - Git y GitHub
- Termux + Git 2.55 operativo.
- Token de GitHub configurado (credential.helper store).
- Comandos de creacion directa de documentos.
- Push automatico a main.
- Estructura limpia en docs/.
- Sin carpetas anidadas (arreglado hoy).

Capacidad: crear y subir un documento en 30 segundos.

### 2.2 Codigo fuente en GitHub
- Backend FastAPI: 5 routers, 26 endpoints, 9 modelos.
- Bot Telegram multi-agente: 7 agentes definidos.
- llm_client.py (capa de abstraccion IA).
- bot_multiagent.py (bot principal).
- .env.example con variables NVIDIA.
- Supabase conectado: tabla profiles + trigger.

Capacidad: codigo listo para deploy.

### 2.3 Documentacion en GitHub
- 65 documentos .md organizados.
- Estructura: docs/, docs/legales/, docs/estrategia/, docs/automatizacion/.
- Todos los pendientes alta prioridad creados.
- 7 perfiles de agentes IA.
- Formacion de Ernesto (3 archivos).

Capacidad: fuente de verdad centralizada.

---

## 3. Lo Que Esta Listo Pero Parado

### 3.1 Bot Telegram tutoria_cuba_bot
- Codigo completo.
- 7 agentes configurados.
- Formato de respuestas definido.
- Deteccion automatica de IA activa.
- Comandos y aliases implementados.

Bloqueante: SIN IA fondada.
Razon de parada voluntaria: no tiene sentido correr sin IA.

### 3.2 Backend FastAPI
- Codigo completo en backend/app/.
- 5 routers funcionales.
- Modelos SQLAlchemy para Supabase.
- Servicios deepseek.py y supabase_client.py.
- requirements.txt actualizado.

Bloqueante: SIN VPS internacional.
Razon: no se puede exponer sin infraestructura.

### 3.3 Agentes IA
- 7 perfiles completos.
- Programa de formacion N1 a N5 disenado.
- Limites definidos.
- Estado actual: todos en N0 Pre-aprendiz.

Bloqueante: SIN IA fondada para que operen.
Razon: los agentes necesitan LLM activo.

### 3.4 Sistema de inteligencia de mercado
- Fuentes identificadas (Facebook, WhatsApp, Telegram).
- Rutina diaria definida.
- Productos a monitorear listados.

Bloqueante: sin automatizacion, todo es manual.

---

## 4. Lo Que Falta Crear

### 4.1 Automatizacion Documental

- [ ] Script batch para crear varios documentos de una vez.
- [ ] Script de backup automatico diario del repo.
- [ ] Script de verificacion de estructura (sin anidaciones).
- [ ] Script de sincronizacion programada (cron en Termux).
- [ ] Script de verificacion de duplicados por nombre.

Esfuerzo: 1 dia de desarrollo.
Impacto: alto (ahorra tiempo y evita errores).

### 4.2 Automatizacion IA

- [ ] Fondeo de DeepSeek (5 USD) o registro NVIDIA (gratis).
- [ ] Bot operando 24h con IA real.
- [ ] Pipeline de formacion automatizada de agentes.
- [ ] Sistema de logs de conversaciones.
- [ ] Dashboard de estado de agentes.

Esfuerzo: 2-3 dias + inversion 5 a 20 USD.
Impacto: critico (habilita el bot).

### 4.3 Automatizacion de Infraestructura

- [ ] VPS internacional (Hetzner, Contabo, DigitalOcean).
- [ ] Deploy de FastAPI con systemd.
- [ ] Configuracion de Nginx reverse proxy.
- [ ] Certificado SSL con Let's Encrypt.
- [ ] Monitoreo basico (uptime + logs).

Esfuerzo: 2-3 dias + inversion 5 USD/mes.
Impacto: alto (habilita backend publico).

### 4.4 Automatizacion de Comunicaciones

- [ ] Bot de WhatsApp Business (Twilio o similar).
- [ ] Canal automatizado de alertas.
- [ ] Respuestas automaticas a clientes.
- [ ] Integracion con Transfermovil (futuro).

Esfuerzo: variable, depende de API.
Impacto: medio (mejora atencion).

### 4.5 Automatizacion Financiera

- [ ] Registro automatico de ventas.
- [ ] Calculo automatico de impuestos.
- [ ] Reportes financieros mensuales.
- [ ] Alertas de vencimientos fiscales.

Esfuerzo: 3-5 dias con Excel o Python.
Impacto: medio (evita sanciones).

### 4.6 Automatizacion Operativa (fisica)

- [ ] Sensores IoT en microembalses (temperatura, oxigeno).
- [ ] Camaras de seguridad en instalaciones.
- [ ] Alarmas de temperatura en camara de frio.
- [ ] Monitoreo remoto de produccion.

Esfuerzo: variable, requiere hardware.
Impacto: bajo a corto plazo (no prioritario).

---

## 5. Prioridades de Inversion

### Prioridad 1 - Criticos (proximos 30 dias)

- IA fondada: 5 a 20 USD.
- VPS internacional: 5 USD/mes.
- Bot 24h activo.

Inversion total: 10 a 30 USD + 5 USD/mes.
Impacto: habilita el 80 por ciento de la automatizacion.

### Prioridad 2 - Altos (proximos 60-90 dias)

- Deploy de FastAPI.
- Backups automaticos.
- Script batch de documentos.

Inversion: 0 USD (solo tiempo).
Impacto: robustez del sistema.

### Prioridad 3 - Medios (proximos 6 meses)

- Automatizacion financiera.
- Automatizacion de comunicaciones.
- Dashboard de agentes.

Inversion: variable.
Impacto: eficiencia operativa.

### Prioridad 4 - Bajos (largo plazo)

- IoT en microembalses.
- Camaras de seguridad.
- Monitoreo remoto.

Inversion: alta.
Impacto: reservado para escalado.

---

## 6. Presupuesto de Automatizacion

### Inversion minima para arrancar
- Fondeo DeepSeek: 5 USD.
- VPS internacional: 5 USD (mes 1).
- Total arranque: 10 USD.

### Inversion anual completa
- VPS: 60 USD/ano.
- IA variable: 20 a 100 USD/ano.
- Dominio (opcional): 10 USD/ano.
- Total anual: 90 a 170 USD.

### Recuperacion de la inversion
- Con 240 kg de filete y 1 ton de pienso actuales.
- Margen actual: 187 USD/mes.
- Automatizacion completa: no requiere mas produccion.
- Recuperacion: 1 mes de operacion.

---

## 7. Cronograma de Automatizacion

### Mes 1 - Criticos
Semana 1: Fondeo DeepSeek o registro NVIDIA.
Semana 2: Contratacion VPS internacional.
Semana 3: Deploy de bot 24h.
Semana 4: Verificacion de operacion continua.

### Mes 2 - Altos
Semana 1: Deploy de FastAPI en VPS.
Semana 2: Configuracion SSL y dominio.
Semana 3: Script de backups automaticos.
Semana 4: Verificacion de backups.

### Mes 3 - Medios
Semana 1: Script batch de documentos.
Semana 2: Automatizacion financiera basica.
Semana 3: Dashboard de estado.
Semana 4: Documentacion del sistema completo.

### Mes 4-6 - Consolidacion
- Mejoras incrementales.
- Automatizacion de comunicaciones si hay recursos.
- Preparacion para IoT si hay financiamiento.

---

## 8. Bloqueantes Actuales

### 8.1 Conexion a internet
- Actual: 250 kbps variable.
- Solucion: VPS internacional + operaciones en madrugada.
- Impacto: medio, manejable.

### 8.2 Capital
- Actual: 39.92 USD (QvaPay + VISA bloqueada).
- Necesario: 10 a 30 USD para arranque.
- Solucion: fondear QvaPay con ventas del mes.

### 8.3 Carga de trabajo de Yosbel
- Actual: unico operador.
- Solucion: agentes IA automatizados.
- Impacto: alto, la automatizacion libera tiempo.

### 8.4 Falta de VPS
- Actual: nada.
- Solucion: contratar uno basico.
- Impacto: critico para bot y backend.

### 8.5 Falta de IA fondada
- Actual: sin acceso a DeepSeek ni NVIDIA.
- Solucion: fondear o registrarse.
- Impacto: critico para agentes.

---

## 9. Documentos que Faltan Guardar (contexto)

De los 9 pendientes de medio plazo del traspaso:

- anexo-ah-modelo-financialab-tutoria.md
- anexo-ab-malla-curricular.md
- anexo-ac-onboarding-profesores.md
- anexo-x-sistema-autonomo.md
- anexo-y-formacion-agentes.md
- anexo-z-herramientas-agentes.md
- analisis-ley-176-transformaciones.md
- Modulos 02 a 05 de formacion Ernesto
- 5 cursos TutorIA sobre Ley 185

Relacion con automatizacion:
- anexo-x (sistema autonomo): 100 por ciento automatizacion.
- anexo-y (formacion agentes): automatizacion educativa.
- anexo-z (herramientas agentes): base de automatizacion.
- anexo-ah (modelo FinanciaLab): automatizacion financiera.

Estos 4 documentos son prioritarios para el plan de
automatizacion y deben crearse primero.

---

## 10. Proximos Pasos Inmediatos

1. [ ] Crear anexo-x-sistema-autonomo.md.
2. [ ] Crear anexo-y-formacion-agentes.md.
3. [ ] Crear anexo-z-herramientas-agentes.md.
4. [ ] Crear anexo-ah-modelo-financialab-tutoria.md.
5. [ ] Fondear QvaPay con 5 USD de la proxima venta.
6. [ ] Registrar cuenta NVIDIA (gratis) como respaldo.
7. [ ] Investigar VPS economicos disponibles en Cuba.
8. [ ] Configurar cron en Termux para backups diarios.

---

## 11. Cumplimiento Anexo V

Este documento NO contiene credenciales, API Keys, tokens ni
datos sensibles. Todo dato protegido va en .env bajo .gitignore.

---

## 12. Registro de Cambios

Version 1.0 - 3/oct/2026 - Creacion inicial.

---

Documento oficial del Ecosistema Mayabeque - 3/octubre/2026
