# Anexo 14 de octubre de 2026 — Bugs resueltos en sesión

## Resumen
Se resolvieron 7 bugs históricos del proyecto TutorIA Cuba. El pipeline
completo de chat + generación de imágenes funciona de punta a punta.

## Estado final
- Túnel: ngrok (`lens-portside-masses.ngrok-free.dev`)
- Backend: FastAPI en :8000, systemd activo
- LLM chat: NVIDIA (prioritario), Groq (fallback, con bug conocido)
- Imágenes: Agnes API con `response_format: b64_json`
- PWA: servida por FastAPI con URLs relativas

## Bugs resueltos

### 1. Túnel Cloudflare timeout (30s)
- Causa: plan gratuito Cloudflare corta requests >30s
- Fix: migrar a ngrok (plan free, sin timeout)
- Servicio: `/etc/systemd/system/tutoria-tunnel.service`

### 2. Modelo no ejecutaba tools
- Causa: system_prompt de Pablo decía "Escribe /[comando]"
- Fix: suavizar instrucción + añadir REGLA_HERRAMIENTAS a los 7 agentes

### 3. Dispatcher sin registrar generar_imagen/generar_video
- Causa: `ejecutar_herramienta` en tools.py tenía 7 elif, faltaban 2
- Fix: añadir los 2 elif faltantes

### 4. `return [OK]` mal indentado
- Causa: el `return f"[OK] Imagen creada..."` estaba a 12 espacios
  (dentro del `else:`) en vez de a 8 (nivel del if/elif/else)
- Fix: quitar 4 espacios de indentación
- Síntoma: la función siempre devolvía `None` en el camino exitoso

### 5. Agnes devolvía URL rota
- Causa: Agnes devolvía `b64_json: ""` + URL en S3 que daba `NoSuchKey`
- Fix: enviar `"response_format": "b64_json"` explícito en el payload
- Resultado: devuelve ~1.5 MB de base64 directo

### 6. AGNES_API_KEY con caracteres invisibles
- Causa: el `read -s` desde terminal móvil metió secuencias `^[[A` (flecha arriba)
  y `\r` (carriage return) en el `.env`
- Fix: `re.sub(r'\x1b\[[A-Za-z]', '', c)` + eliminar `\r`
- Síntoma: HTTP 400 con body vacío de Agnes

### 7. Modelo alucinaba URLs falsas
- Causa: cuando la tool fallaba, el modelo inventaba una URL plausible
- Fix: añadir REGLAS CRÍTICO + URL_EXACTA a los 7 agentes
- Síntoma: el modelo decía "aquí tienes: /img/imagenes/dragón_verde.png"
  cuando la tool en realidad había fallado

## Bugs pendientes

### A. Groq rechaza `role:tool` sin `content`
- Síntoma: HTTP 400 `'messages.3.content': property 'content' is missing`
- Causa: el bloque `messages.append({"role":"tool",...})` en `llm_router.py`
  quedó sin la línea `"content": str(resultado)[:8000]` tras un `sed` mal usado
- Estado: Groq no prioritario, funciona con NVIDIA como principal
- Fix sugerido: añadir la línea `content` en el bloque

### B. Modelo no pasa `nombre_archivo` a generar_imagen
- Síntoma: siempre genera `imagen_generada.png` (sobrescribe)
- Mitigación: default ahora es `img_TIMESTAMP.png` si no viene
- Fix sugerido: prompt más explícito o `tool_choice` con argumentos obligatorios

## Archivos modificados
- `agents.py` — reglas CRÍTICO + URL_EXACTA + reglas de herramientas
- `llm_router.py` — revertido a NVIDIA prioritario, fix `content` en role:tool
- `tools.py` — sanitización de nombres + default timestamp + fix indentación
- `/etc/systemd/system/tutoria-tunnel.service` — Cloudflare → ngrok
- `backend/app/.env` — AGNES_API_KEY limpia

## Comandos útiles
- Ver URL del túnel: `journalctl -u tutoria-tunnel.service | grep "started tunnel" | tail -1`
- Reiniciar todo: `systemctl restart tutoria-backend.service`
- Ver logs: `journalctl -u tutoria-backend.service -f`
- Probar chat: `curl -X POST https://lens-portside-masses.ngrok-free.dev/agentes/chat -H "Content-Type: application/json" -d '{"agente":"pablo","mensaje":"Hola"}'`

## Pendientes para próxima sesión
1. Entrega multimedia (bot Telegram envía foto + PWA muestra imagen)
2. Unificar IA (bot_multiagent.py usa llm_router.py)
3. Integrar PlataformIA (IA cubana con Transfermóvil)
4. Rotar API key Agnes (seguridad)
5. Arreglar Groq `content` en `role:tool`

---
Documento creado: 14 de octubre de 2026, 11:16 AM
