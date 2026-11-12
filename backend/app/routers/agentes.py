from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys
from dotenv import load_dotenv

load_dotenv("/root/Mi-primer-proyecto/backend/app/.env")
sys.path.insert(0, "/root/Mi-primer-proyecto")

from agents import AGENTS
from llm_router import consultar_llm_router

router = APIRouter(prefix="/agentes", tags=["agentes"])

class ChatIn(BaseModel):
    agente: str = "pablo"
    mensaje: str

@router.get("/lista")
def lista_agentes():
    return [
        {
            "id": k,
            "nombre": v["nombre"],
            "cargo": v["cargo"],
            "emoji": v.get("emoji", ""),
            "descripcion": v.get("descripcion", ""),
        }
        for k, v in AGENTS.items()
    ]

@router.post("/chat")
async def chat(data: ChatIn):
    agente_id = data.agente.lower().strip()
    if agente_id not in AGENTS:
        raise HTTPException(400, f"Agente '{agente_id}' no existe")
    if not data.mensaje.strip():
        raise HTTPException(400, "Mensaje vacio")
    config = AGENTS[agente_id]
    try:
        respuesta = await consultar_llm_router(
            config["system_prompt"],
            data.mensaje
        )
    except Exception as e:
        raise HTTPException(500, f"Error de IA: {str(e)[:200]}")
    return {
        "agente": agente_id,
        "nombre": config["nombre"],
        "respuesta": respuesta,
    }
