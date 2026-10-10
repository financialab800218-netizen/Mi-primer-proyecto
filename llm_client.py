"""
llm_client.py - Cliente unificado para LLMs
Ecosistema Mayabeque + TutorIA Cuba
"""

import os
import httpx
from dotenv import load_dotenv

ENV_PATH = "/root/Mi-primer-proyecto/backend/app/.env"
load_dotenv(ENV_PATH)


PROVEEDORES = {
    "deepseek": {
        "url": "https://api.deepseek.com",
        "modelo": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
    },
    "nvidia": {
        "url": "https://integrate.api.nvidia.com/v1",
        "modelo": "openai/gpt-oss-20b",
        "env_key": "NVIDIA_API_KEY",
    },
}


def obtener_config():
    proveedor_activo = os.getenv("LLM_PROVIDER", "deepseek").lower()

    if proveedor_activo in PROVEEDORES:
        config = PROVEEDORES[proveedor_activo]
        api_key = os.getenv(config["env_key"], "")
        if api_key and len(api_key) > 20:
            return {
                "nombre": proveedor_activo,
                "url": config["url"],
                "modelo": config["modelo"],
                "api_key": api_key,
            }

    for nombre, config in PROVEEDORES.items():
        api_key = os.getenv(config["env_key"], "")
        if api_key and len(api_key) > 20:
            return {
                "nombre": nombre,
                "url": config["url"],
                "modelo": config["modelo"],
                "api_key": api_key,
            }

    return None


def tiene_llm():
    return obtener_config() is not None


async def consultar_llm(system_prompt, mensaje, max_tokens=800, temperature=0.7):
    config = obtener_config()
    if not config:
        return None

    try:
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": config["modelo"],
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": mensaje},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            r = await client.post(
                f"{config['url']}/chat/completions",
                headers=headers,
                json=payload,
            )
            if r.status_code == 200:
                data = r.json()
                return data["choices"][0]["message"]["content"]
            else:
                return f"[Error {config['nombre']} {r.status_code}]"

    except Exception as e:
        return f"[Error conexion: {str(e)[:80]}]"


def info_proveedor():
    config = obtener_config()
    if not config:
        return "Sin proveedor de IA activo"
    return f"{config['nombre']} ({config['modelo']})"
