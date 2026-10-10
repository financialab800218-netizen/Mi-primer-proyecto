"""Extiende llm_client con soporte de tool calling."""
import os
import json
import httpx
from llm_client import obtener_config
from tools import TOOLS_SCHEMA, ejecutar_herramienta

MAX_ITERACIONES = 5
MAX_TOKENS = 1500

async def consultar_llm_con_tools(system_prompt, mensaje, max_iter=MAX_ITERACIONES):
    config = obtener_config()
    if not config:
        return None

    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json",
    }
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": mensaje},
    ]

    try:
        async with httpx.AsyncClient(timeout=90.0) as client:
            for i in range(max_iter):
                payload = {
                    "model": config["modelo"],
                    "messages": messages,
                    "tools": TOOLS_SCHEMA,
                    "max_tokens": MAX_TOKENS,
                }
                r = await client.post(
                    f"{config['url']}/chat/completions",
                    headers=headers,
                    json=payload,
                )
                if r.status_code != 200:
                    return f"[Error {config['nombre']} {r.status_code}]"

                data = r.json()
                msg = data["choices"][0]["message"]
                tool_calls = msg.get("tool_calls") or []

                if not tool_calls:
                    return msg.get("content") or "[Sin respuesta]"

                messages.append(msg)
                for tc in tool_calls:
                    nombre = tc["function"]["name"]
                    try:
                        args = json.loads(tc["function"]["arguments"])
                    except Exception:
                        args = {}
                    print(f"[tool] {nombre} {args}")
                    resultado = ejecutar_herramienta(nombre, args)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc["id"],
                        "content": str(resultado)[:8000],
                    })

        return "[Error] Maximo de iteraciones alcanzado"
    except Exception as e:
        return f"[Error conexion: {str(e)[:80]}]"
