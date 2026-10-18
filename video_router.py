import os
import asyncio
import httpx
import time

async def generar_agnes(prompt):
    """Genera video usando Agnes."""
    api_key = os.getenv("AGNES_API_KEY")
    base_url = os.getenv("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")
    modelo = "agnes-video-2.5-flash"
    
    payload = {"model": modelo, "prompt": prompt, "seconds": "5", "mode": "text", "size": "720P", "aspect_ratio": "16:9"}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{base_url}/videos", headers=headers, json=payload, timeout=30.0)
        if resp.status_code != 200:
            raise Exception(f"Agnes error {resp.status_code}: {resp.text}")
        
        data = resp.json()
        video_id = data.get("video_id") or data.get("id") or data.get("task_id")
        
        for _ in range(30):
            await asyncio.sleep(2)
            poll_url = f"https://apihub.agnes-ai.com/agnesapi?video_id={video_id}&model_name={modelo}"
            poll_resp = await client.get(poll_url, headers=headers, timeout=15.0)
            if poll_resp.status_code == 200:
                poll_data = poll_resp.json()
                if poll_data.get("status") == "completed":
                    return poll_data.get("url")
                elif poll_data.get("status") == "failed":
                    raise Exception("Agnes reporto fallo en la generacion.")
        raise Exception("Agnes: Tiempo de espera agotado.")

async def generar_huggingface(prompt):
    """Genera video usando Hugging Face (Gratis)."""
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise Exception("HUGGINGFACE_API_KEY no configurada.")
    
    model_url = "https://api-inference.huggingface.co/models/cerspense/zeroscope_v2_576w"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": prompt}
    
    async with httpx.AsyncClient() as client:
        print("[HF] Enviando solicitud a Hugging Face (esto puede tardar)...")
        resp = await client.post(model_url, headers=headers, json=payload, timeout=120.0)
        
        if resp.status_code == 200:
            nombre_archivo = f"hf_{int(time.time())}.mp4"
            carpeta = "/root/Mi-primer-proyecto/backend/app/static/img/videos"
            os.makedirs(carpeta, exist_ok=True)
            ruta = os.path.join(carpeta, nombre_archivo)
            
            with open(ruta, "wb") as f:
                f.write(resp.content)
            
            return f"https://lens-portside-masses.ngrok-free.dev/img/videos/{nombre_archivo}"
        elif resp.status_code == 503:
            raise Exception("Modelo de Hugging Face cargando. Intenta de nuevo en 20 segundos.")
        else:
            raise Exception(f"Hugging Face error {resp.status_code}: {resp.text[:100]}")

async def generar_video_multi(prompt, es_premium):
    """Router principal de video."""
    if es_premium:
        return await generar_agnes(prompt)
    else:
        try:
            print("[VideoRouter] Intentando Hugging Face (Gratis)...")
            return await generar_huggingface(prompt)
        except Exception as e:
            print(f"[VideoRouter] Hugging Face fallo: {e}")
            try:
                print("[VideoRouter] Intentando Agnes Free como respaldo...")
                return await generar_agnes(prompt)
            except Exception as e2:
                print(f"[VideoRouter] Agnes Free fallo: {e2}")
                raise Exception("Todos los proveedores de video estan saturados. Intenta mas tarde.")
