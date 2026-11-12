import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv('/root/Mi-primer-proyecto/backend/app/.env')
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def subir_archivo_a_nube(nombre_archivo_local: str, nombre_en_nube: str):
    try:
        ruta_local = f"/root/Mi-primer-proyecto/backend/app/static/docs/{nombre_archivo_local}"
        
        # 1. Subir el archivo a Supabase
        with open(ruta_local, 'rb') as f:
            supabase.storage.from_("Documentos").upload(
                path=nombre_en_nube,
                file=f,
                file_options={"content-type": "application/octet-stream", "upsert": "true"}
            )
            
        # 2. Obtener la URL publica
        url_publica = supabase.storage.from_("Documentos").get_public_url(nombre_en_nube)
        
        # 3. Borrar el archivo local para no llenar el VPS
        os.remove(ruta_local)
        
        return url_publica
    except Exception as e:
        return f"Error al subir a la nube: {str(e)}"
