# Anexo AO - Groq como Respaldo de NVIDIA

Fecha: 10 octubre 2026

## Objetivo

Implementar un sistema de IA con alta disponibilidad usando dos proveedores en cascada: NVIDIA como principal y Groq como respaldo automatico.

## Problema resuelto

Si NVIDIA falla (saturacion, rate limit, timeout, error 500), el bot queda sin respuesta. El router multi-proveedor resuelve esto automaticamente.

## Arquitectura

Usuario Telegram
      |
Bot Telegram
      |
llm_router.py (enrutador)
      |
      |--- NVIDIA (principal) -----> openai/gpt-oss-20b
      |
      |--- Groq (respaldo) --------> openai/gpt-oss-120b

## Componentes

### 1. Cuenta Groq
- URL: console.groq.com
- Costo: 0 USD (tier gratuito)
- API Key guardada en: backend/app/.env como GROQ_API_KEY

### 2. Modelo Groq actual
- Modelo: openai/gpt-oss-120b
- Compatible con tool calling
- API identica a OpenAI

### 3. Archivo llm_router.py
- Contiene funcion consultar_llm_router
- Intenta NVIDIA primero
- Si falla, intenta Groq
- Devuelve respuesta del primer proveedor que responda

### 4. Modificacion del bot
- bot_multiagent.py importa desde llm_router
- En lugar de from llm_tools import consultar_llm_con_tools
- Ahora es from llm_router import consultar_llm_router as consultar_llm_con_tools

## Como funciona

1. Usuario envia mensaje en Telegram
2. Bot llama a consultar_llm_router
3. Router intenta NVIDIA con openai/gpt-oss-20b
4. Si NVIDIA responde OK, retorna respuesta
5. Si NVIDIA falla, imprime error en log y prueba Groq
6. Groq usa openai/gpt-oss-120b
7. Retorna la respuesta final

## Costos

- NVIDIA NIM: 0 USD (tier gratuito)
- Groq: 0 USD (tier gratuito)
- Total IA: 0 USD/mes
- VPS EQVPS: 3 USD/mes
- Costo total operativo: 3 USD/mes

## Limitaciones

- Ambos proveedores tienen rate limit (40 req/min aprox)
- Groq cambia modelos periodicamente (verificar lista actual)
- No hay tercer proveedor todavia (DeepSeek en pausa)

## Verificacion

Prueba manual ejecutada:
curl a api.groq.com con modelo openai/gpt-oss-120b
Resultado: respuesta exitosa con total_tokens 127

## Proximos pasos

- Monitorear logs para ver cuando se usa Groq
- Evaluar si vale la pena un tercer proveedor
- Considerar cache de respuestas frecuentes