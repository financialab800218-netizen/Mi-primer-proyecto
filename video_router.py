import os
import asyncio
import httpx
import time

async def generar_agnes(prompt):
    """Genera video usando Agnes con sistema de reintentos para cola llena."""
    api_key = os.getenv("AGNES_API_KEY")
    base_url = os.getenv("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")
    modelo = "agnes-video-2.5-flash"
    
    payload = {"model": modelo, "prompt": prompt, "seconds": "5", "mode": "text", "size": "720P", "aspect_ratio": "16:9"}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    async with httpx.AsyncClient() as client:
        video_id = None
        
        # Bucle de reintentos si la cola esta llena (Error 503)
        for intento in range(3):
            resp = await client.post(f"{base_url}/videos", headers=headers, json=payload, timeout=30.0)
            
            if resp.status_code == 200:
                data = resp.json()
                video_id = data.get("video_id") or data.get("id") or data.get("task_id")
                break # Exito, salimos del bucle
            elif resp.status_code == 503 or "queue_full" in resp.text:
                if intento < 2:
                    print(f"[Agnes] Cola llena. Reintentando en 15 segundos... (Intento {intento+1}/3)")
                    await asyncio.sleep(15)
                else:
                    raise Exception("La cola de Agnes esta llena. Intenta de nuevo en unos minutos.")
            else:
                raise Exception(f"Agnes error {resp.status_code}: {resp.text[:100]}")

        if not video_id:
            raise Exception("No se pudo crear el video en Agnes.")

        # Polling para ver si el video esta listo
        url_video = None
        for _ in range(30):
            await asyncio.sleep(2)
            poll_url = f"https://apihub.agnes-ai.com/agnesapi?video_id={video_id}&model_name={modelo}"
            poll_resp = await client.get(poll_url, headers=headers, timeout=15.0)
            if poll_resp.status_code == 200:
                poll_data = poll_resp.json()
                if poll_data.get("status") == "completed":
                    url_video = poll_data.get("url")
                    break
                elif poll_data.get("status") == "failed":
                    raise Exception("Agnes reporto fallo en la generacion.")
        
        if not url_video:
            raise Exception("Tiempo de espera agotado en Agnes.")

        # Descargar el video
        nombre_archivo = f"vid_{int(time.time())}.mp4"
        carpeta = "/root/Mi-primer-proyecto/backend/app/static/img/videos"
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, nombre_archivo)

        vid_resp = await client.get(url_video, headers=headers, timeout=120.0)
        
        if len(vid_resp.content) < 50000:
            raise Exception("El archivo descargado es demasiado pequeno (posible error de red).")

        with open(ruta, "wb") as f:
            f.write(vid_resp.content)

        return f"https://lens-portside-masses.ngrok-free.dev/img/videos/{nombre_archivo}"

async def generar_huggingface(prompt):
    raise Exception("Hugging Face no disponible (bloqueo DNS).")

async def generar_video_multi(prompt, es_premium):
    if es_premium:
        return await generar_agnes(prompt)
    else:
        try:
            return await generar_huggingface(prompt)
        except Exception:
            return await generar_agnes(prompt)
