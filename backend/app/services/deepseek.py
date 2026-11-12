import httpx
from typing import Optional

from config import settings


class DeepSeekClient:
    """Cliente para la API de DeepSeek."""

    def __init__(self):
        self.api_key = settings.deepseek_api_key
        self.base_url = settings.deepseek_base_url
        self.timeout = 60.0

    def esta_configurado(self) -> bool:
        """Verifica si la API key esta configurada."""
        return bool(self.api_key and self.api_key != "tu_api_key_aqui")

    async def chat(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> dict:
        """Envia un mensaje al modelo DeepSeek y retorna la respuesta."""
        if not self.esta_configurado():
            return {
                "error": "API key no configurada",
                "message": "Configura DEEPSEEK_API_KEY en el archivo .env"
            }

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {
                    "error": "Error HTTP",
                    "status_code": e.response.status_code,
                    "message": e.response.text
                }
            except httpx.RequestError as e:
                return {
                    "error": "Error de conexion",
                    "message": str(e)
                }


deepseek_client = DeepSeekClient()
