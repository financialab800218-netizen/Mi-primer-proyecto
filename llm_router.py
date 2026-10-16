"""Router multi-proveedor: NVIDIA principal, Groq respaldo."""
import os
import json
import httpx
from llm_client import obtener_config
from tools import TOOLS_SCHEMA, ejecutar_herramienta

GROQ_URL = "https://api.groq.com/openai/v1"
GROQ_MODEL = "openai/gpt-oss-120b"
MAX_ITER = 6

async def _consultar(proveedor, url, model, api_key, system_prompt, mensaje):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": mensaje}
    ]
    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            for i in range(MAX_ITER):
                payload = {
                    "model": model,
                    "messages": messages,
                    "tools": TOOLS_SCHEMA,
                    "max_tokens": 1500
                }
                r = await client.post(f"{url}/chat/completions", headers=headers, json=payload)
                if r.status_code != 200:
                    print(f"[error-status/{proveedor}] HTTP {r.status_code}: {r.text[:200]}")
                    return "[No pude procesar tu solicitud. Intenta con una pregunta mas especifica.]"
                data = r.json()
                if "choices" not in data or not data.get("choices"):
                    print(f"[error-choices/{proveedor}] Sin choices: {str(data)[:200]}")
                    return "[No pude procesar tu solicitud. Intenta con una pregunta mas especifica.]"
                msg = data["choices"][0]["message"]
                tool_calls = msg.get("tool_calls") or []
                if not tool_calls:
                    return msg.get("content") or "[Sin respuesta]"
                messages.append(msg)
                for tc in tool_calls:
                    nombre = tc["function"]["name"].split("<")[0].strip()
                    try:
                        args = json.loads(tc["function"]["arguments"])
                    except Exception:
                        args = {}
                    print(f"[tool/{proveedor}] {nombre} {args}")
                    resultado = ejecutar_herramienta(nombre, args)

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc["id"],
                        "content": str(resultado)[:8000],
                    })
    except Exception as e:
        print(f"[error/{proveedor}] {str(e)[:80]}")
        return "[No pude procesar tu solicitud. Intenta con una pregunta mas especifica.]"

async def consultar_llm_router(system_prompt, mensaje):
    # Intento 1: NVIDIA (principal)
    config = obtener_config()
    if config:
        print("[router] Intentando NVIDIA...")
        r = await _consultar("nvidia", config["url"], config["modelo"], config["api_key"], system_prompt, mensaje)
        if r:
            return r
        print("[router] NVIDIA fallo, usando Groq...")
    
    # Intento 2: Groq DESHABILITADO (bug + rate limit)
    # groq_key = os.getenv("GROQ_API_KEY")
    # if groq_key:
    #     print("[router] Intentando Groq...")
    #     r = await _consultar("groq", GROQ_URL, GROQ_MODEL, groq_key, system_prompt, mensaje)
    #     if r:
    #         return r
    #     print("[router] Groq tambien fallo")
    
    return "[Error] Ningun proveedor de IA respondio"
