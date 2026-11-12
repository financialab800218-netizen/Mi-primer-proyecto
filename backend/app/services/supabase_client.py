import httpx
from typing import Optional, List, Dict, Any
from config import settings


class SupabaseClient:
    """Cliente de Supabase usando httpx directamente."""

    def __init__(self):
        self.url = settings.supabase_url.rstrip("/")
        self.key = settings.supabase_key
        self.timeout = 30.0

    def esta_configurado(self) -> bool:
        return bool(self.url and self.key)

    def _headers(self) -> dict:
        return {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }

    def _url(self, tabla: str, query: Optional[str] = None) -> str:
        url = f"{self.url}/rest/v1/{tabla}"
        if query:
            url += f"?{query}"
        return url

    def select(self, tabla: str, query: Optional[str] = None) -> List[Dict[str, Any]]:
        try:
            response = httpx.get(
                self._url(tabla, query),
                headers=self._headers(),
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return [{"error": str(e)}]

    def insert(self, tabla: str, datos: dict) -> dict:
        try:
            response = httpx.post(
                self._url(tabla),
                headers=self._headers(),
                json=datos,
                timeout=self.timeout
            )
            response.raise_for_status()
            return {"status": "ok", "data": response.json()}
        except Exception as e:
            return {"status": "error", "detail": str(e)}

    def health_check(self) -> dict:
        if not self.esta_configurado():
            return {"status": "no_configurado"}
        try:
            response = httpx.get(
                self._url("profiles", "limit=1"),
                headers=self._headers(),
                timeout=self.timeout
            )
            if response.status_code == 200:
                return {"status": "conectado", "url": self.url}
            return {"status": "error", "code": response.status_code, "detail": response.text}
        except Exception as e:
            return {"status": "error", "detail": str(e)}


supabase_client = SupabaseClient()
