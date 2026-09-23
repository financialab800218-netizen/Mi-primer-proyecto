from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.deepseek import deepseek_client

router = APIRouter(
    prefix="/api/ia",
    tags=["Inteligencia Artificial"]
)


class PreguntaRequest(BaseModel):
    prompt: str
    system: str | None = None


@router.get("/estado")
def estado_ia():
    """Verifica si la IA esta configurada."""
    return {
        "configurado": deepseek_client.esta_configurado(),
        "modelo": "deepseek-chat"
    }


@router.post("/preguntar")
async def preguntar(request: PreguntaRequest):
    """Envia una pregunta a DeepSeek y retorna la respuesta."""
    if not deepseek_client.esta_configurado():
        raise HTTPException(
            status_code=503,
            detail="API key de DeepSeek no configurada"
        )

    resultado = await deepseek_client.chat(
        prompt=request.prompt,
        system=request.system
    )

    if "error" in resultado:
        raise HTTPException(status_code=500, detail=resultado)

    return resultado
