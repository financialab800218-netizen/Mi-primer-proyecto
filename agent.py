"""Agente TutorIA Cuba - CLI con acceso a documentos.
Uso: python3 agent.py "tu pregunta en lenguaje natural"
"""
import sys
import os
import json
import httpx
from dotenv import load_dotenv
from tools import leer_archivo, listar_archivos, buscar_texto, TOOLS_SCHEMA

ENV_PATH = "/data/data/com.termux/files/home/tutoria-cuba/backend/app/.env"
load_dotenv(ENV_PATH)

NVIDIA_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "openai/gpt-oss-20b"
MAX_TOKENS = 2000
MAX_ITERACIONES = 5

SYSTEM_PROMPT = """Eres un asistente del proyecto TutorIA Cuba.
Tienes acceso a herramientas para leer archivos del proyecto.
Usa las herramientas cuando necesites informacion que no sabes.
Cuando tengas la respuesta, responde de forma clara y concisa.
Siempre cita el archivo de donde sacaste la informacion."""

def ejecutar_tool(nombre, args):
    if nombre == "leer_archivo":
        return leer_archivo(args.get("ruta", ""))
    elif nombre == "listar_archivos":
        return listar_archivos(args.get("carpeta", "."))
    elif nombre == "buscar_texto":
        return buscar_texto(args.get("patron", ""), args.get("carpeta", "docs"))
    else:
        return "[Error] Tool desconocida: " + nombre

SYSTEM_PROMPT = """Eres un asistente del proyecto TutorIA Cuba.
Tienes acceso a herramientas para leer archivos del proyecto.
Usa las herramientas cuando necesites informacion que no sabes.
Cuando tengas la respuesta, responde de forma clara y concisa.
Siempre cita el archivo de donde sacaste la informacion."""

def ejecutar_tool(nombre, args):
    if nombre == "leer_archivo":
        return leer_archivo(args.get("ruta", ""))
    elif nombre == "listar_archivos":
        return listar_archivos(args.get("carpeta", "."))
    elif nombre == "buscar_texto":
        return buscar_texto(args.get("patron", ""), args.get("carpeta", "docs"))
    else:
        return "[Error] Tool desconocida: " + nombre

def consultar_agente(pregunta):
    if not NVIDIA_KEY:
        return "[Error] Falta NVIDIA_API_KEY en el .env"
    
    headers = {
        "Authorization": "Bearer " + NVIDIA_KEY,
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": pregunta}
    ]
    
    for i in range(MAX_ITERACIONES):
        try:
            r = httpx.post(
                NVIDIA_URL,
                headers=headers,
                json={
                    "model": MODEL,
                    "messages": messages,
                    "tools": TOOLS_SCHEMA,
                    "max_tokens": MAX_TOKENS
                },
                timeout=90
            )
        except Exception as e:
            return "[Error de conexion] " + str(e)
        
        if r.status_code != 200:
            return "[Error " + str(r.status_code) + "] " + r.text[:300]
        
        data = r.json()
        msg = data["choices"][0]["message"]
        tool_calls = msg.get("tool_calls") or []
        
        if not tool_calls:
            return msg.get("content") or "(sin respuesta)"
        
        messages.append(msg)
        
        for tc in tool_calls:
            nombre = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"])
            except Exception:
                args = {}
            print("[tool] " + nombre + " " + json.dumps(args, ensure_ascii=False), file=sys.stderr)
            resultado = ejecutar_tool(nombre, args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc["id"],
                "content": resultado[:8000]
            })
    
    return "[Error] Maximo de iteraciones alcanzado"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 agent.py \"tu pregunta\"")
        sys.exit(1)
    pregunta = " ".join(sys.argv[1:])
    respuesta = consultar_agente(pregunta)
    print(respuesta)
