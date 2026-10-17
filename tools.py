import json
from pathlib import Path

SANDBOX_ROOT = Path("/root/Mi-primer-proyecto").resolve()
MAX_FILE_SIZE = 50000
MAX_RESULTS = 50
EXTENSIONES_TEXTO = ['.md', '.py', '.txt', '.json', '.env', '.yaml', '.yml']

def _validar_ruta(ruta_relativa):
    ruta_abs = (SANDBOX_ROOT / ruta_relativa).resolve()
    if not str(ruta_abs).startswith(str(SANDBOX_ROOT)):
        raise ValueError("Ruta fuera del sandbox")
    return ruta_abs

def leer_archivo(ruta):
    try:
        ruta_abs = _validar_ruta(ruta)
        if not ruta_abs.exists():
            return "[Error] No existe: " + ruta
        if not ruta_abs.is_file():
            return "[Error] No es archivo: " + ruta
        if ruta_abs.stat().st_size > MAX_FILE_SIZE:
            return "[Error] Muy grande"
        with open(ruta_abs, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception as e:
        return "[Error] " + str(e)

def listar_archivos(carpeta="."):
    try:
        ruta_abs = _validar_ruta(carpeta)
        if not ruta_abs.exists():
            return "[Error] No existe: " + carpeta
        if not ruta_abs.is_dir():
            return "[Error] No es carpeta: " + carpeta
        items = []
        for item in sorted(ruta_abs.iterdir())[:MAX_RESULTS]:
            if item.name.startswith('.'):
                continue
            tipo = "DIR " if item.is_dir() else "FILE"
            size = item.stat().st_size if item.is_file() else 0
            items.append(tipo + "  " + item.name + "  (" + str(size) + " bytes)")
        return "\n".join(items) if items else "(vacio)"
    except Exception as e:
        return "[Error] " + str(e)

def buscar_texto(patron, carpeta="docs"):
    try:
        ruta_abs = _validar_ruta(carpeta)
        if not ruta_abs.exists():
            return "[Error] No existe: " + carpeta
        resultados = []
        for archivo in ruta_abs.rglob("*"):
            if not archivo.is_file():
                continue
            if archivo.suffix not in EXTENSIONES_TEXTO:
                continue
            try:
                with open(archivo, 'r', encoding='utf-8', errors='replace') as f:
                    for num, linea in enumerate(f, 1):
                        if patron.lower() in linea.lower():
                            rel = archivo.relative_to(SANDBOX_ROOT)
                            resultados.append(str(rel) + ":" + str(num) + ": " + linea.strip()[:120])
                            if len(resultados) >= MAX_RESULTS:
                                return "\n".join(resultados)
            except Exception:
                continue
        return "\n".join(resultados) if resultados else "(sin resultados)"
    except Exception as e:
        return "[Error] " + str(e)

def ejecutar_herramienta(nombre, argumentos):
    if nombre == "leer_archivo":
        return leer_archivo(argumentos.get("ruta", ""))
    elif nombre == "listar_archivos":
        return listar_archivos(argumentos.get("carpeta", "."))
    elif nombre == "buscar_texto":
        return buscar_texto(argumentos.get("patron", ""), argumentos.get("carpeta", "docs"))
    elif nombre == "escribir_archivo":
        return escribir_archivo(argumentos.get("ruta", ""), argumentos.get("contenido", ""))
    elif nombre == "crear_carpeta":
        return crear_carpeta(argumentos.get("ruta", ""))
    elif nombre == "git_status":
        return git_status()
    elif nombre == "git_commit_push":
        return git_commit_push(argumentos.get("mensaje", ""))
    elif nombre == "generar_imagen":
        return generar_imagen(argumentos.get("prompt", ""), argumentos.get("nombre_archivo", "imagen_generada.png"))
    elif nombre == "generar_video":
        return generar_video(argumentos.get("prompt", ""), argumentos.get("nombre_archivo", "video_generado.mp4"))
    else:
        return "[Error] Herramienta desconocida: " + nombre

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "leer_archivo",
            "description": "Lee el contenido completo de un archivo de texto del proyecto.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ruta": {"type": "string", "description": "Ruta relativa, ej: 'docs/maestro-v2.0.md'"}
                },
                "required": ["ruta"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_archivos",
            "description": "Lista archivos y carpetas del proyecto.",
            "parameters": {
                "type": "object",
                "properties": {
                    "carpeta": {"type": "string", "description": "Carpeta relativa. Usa '.' para raiz."}
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_texto",
            "description": "Busca un patron en los documentos.",
            "parameters": {
                "type": "object",
                "properties": {
                    "patron": {"type": "string", "description": "Texto a buscar"},
                    "carpeta": {"type": "string", "description": "Carpeta donde buscar"}
                },
                "required": ["patron"]
            }
        }
    }
]

def escribir_archivo(ruta, contenido):
    """Crea o sobrescribe un archivo en el proyecto."""
    try:
        ruta_abs = _validar_ruta(ruta)
        ruta_abs.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta_abs, 'w', encoding='utf-8') as f:
            f.write(contenido)

        # Auto-commit y push a GitHub
        import subprocess
        try:
            subprocess.run(["git", "add", ruta], cwd=str(SANDBOX_ROOT), check=True, timeout=15)
            commit = subprocess.run(
                ["git", "commit", "-m", "Bot: actualizado " + ruta],
                cwd=str(SANDBOX_ROOT), capture_output=True, text=True, timeout=15
            )
            if commit.returncode == 0:
                subprocess.run(
                    ["git", "push", "origin", "main"],
                    cwd=str(SANDBOX_ROOT), capture_output=True, text=True, timeout=30
                )
        except Exception:
            pass

        return "[OK] Archivo escrito y subido a GitHub: " + ruta + " (" + str(len(contenido)) + " caracteres)"
    except Exception as e:
        return "[Error] " + str(e)

def crear_carpeta(ruta):
    """Crea una carpeta nueva en el proyecto."""
    try:
        ruta_abs = _validar_ruta(ruta)
        ruta_abs.mkdir(parents=True, exist_ok=True)
        return "[OK] Carpeta creada: " + ruta
    except Exception as e:
        return "[Error] " + str(e)

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "escribir_archivo",
        "description": "Crea o sobrescribe un archivo de texto en el proyecto.",
        "parameters": {
            "type": "object",
            "properties": {
                "ruta": {"type": "string", "description": "Ruta relativa, ej: 'docs/resumen.md'"},
                "contenido": {"type": "string", "description": "Contenido del archivo"}
            },
            "required": ["ruta", "contenido"]
        }
    }
})

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "crear_carpeta",
        "description": "Crea una carpeta nueva en el proyecto.",
        "parameters": {
            "type": "object",
            "properties": {
                "ruta": {"type": "string", "description": "Ruta relativa de la carpeta"}
            },
            "required": ["ruta"]
        }
    }
})

import subprocess

def _ejecutar_git(args, timeout=30):
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=str(SANDBOX_ROOT),
            capture_output=True,
            text=True,
            timeout=timeout
        )
        salida = (result.stdout + result.stderr).strip()
        return "[OK]\n" + salida if result.returncode == 0 else "[Error]\n" + salida
    except subprocess.TimeoutExpired:
        return "[Error] Comando git excedio el tiempo limite"
    except Exception as e:
        return "[Error] " + str(e)

def git_status():
    return _ejecutar_git(["status", "--short"])

def git_commit_push(mensaje):
    try:
        if not mensaje or len(mensaje) < 5:
            return "[Error] El mensaje de commit debe tener al menos 5 caracteres"
        
        subprocess.run(["git", "add", "-A"], cwd=str(SANDBOX_ROOT), check=True, timeout=30)
        commit = subprocess.run(
            ["git", "commit", "-m", mensaje],
            cwd=str(SANDBOX_ROOT),
            capture_output=True, text=True, timeout=30
        )
        if commit.returncode != 0:
            if "nothing to commit" in (commit.stdout + commit.stderr):
                return "[OK] No hay cambios para guardar"
            return "[Error commit]\n" + commit.stdout + commit.stderr
        
        push = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=str(SANDBOX_ROOT),
            capture_output=True, text=True, timeout=60
        )
        if push.returncode != 0:
            return "[Error push]\n" + push.stdout + push.stderr
        
        return "[OK] Commit y push exitosos:\n" + commit.stdout
    except Exception as e:
        return "[Error] " + str(e)

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "git_status",
        "description": "Muestra que archivos han cambiado en el proyecto (git status).",
        "parameters": {"type": "object", "properties": {}, "required": []}
    }
})

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "git_commit_push",
        "description": "Guarda todos los cambios y los sube a GitHub. Usar solo cuando el usuario lo pida explicitamente.",
        "parameters": {
            "type": "object",
            "properties": {
                "mensaje": {"type": "string", "description": "Mensaje del commit (min 5 caracteres)"}
            },
            "required": ["mensaje"]
        }
    }
})

def generar_imagen(prompt, nombre_archivo=None):
    import os, base64
    from datetime import datetime
    if not nombre_archivo:
        from datetime import datetime as _dt
        nombre_archivo = "img_" + _dt.now().strftime("%Y%m%d_%H%M%S") + ".png"
    # Sanitizar nombre_archivo
    import unicodedata
    nombre_archivo = unicodedata.normalize("NFKD", nombre_archivo).encode("ascii", "ignore").decode("ascii")
    nombre_archivo = nombre_archivo.replace(" ", "_").replace(".", "_")
    if not nombre_archivo.endswith("_png"):
        nombre_archivo = nombre_archivo.replace("_png", "") + ".png"
    else:
        nombre_archivo = nombre_archivo.replace("_png", ".png")
    api_key = os.getenv("AGNES_API_KEY")
    base_url = os.getenv("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")
    modelo = os.getenv("AGNES_IMAGE_MODEL", "agnes-image-2.5-flash")
    if not api_key:
        return "[Error] AGNES_API_KEY no configurada"
    try:
        import httpx
        payload = {"model": modelo, "prompt": prompt, "n": 1, "size": "1024x1024", "response_format": "b64_json"}
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        r = httpx.post(f"{base_url}/images/generations", headers=headers, json=payload, timeout=120)
        if r.status_code != 200:
            if r.status_code == 429:
                return "[Error] Limite de generacion de video alcanzado. Intenta mas tarde."
            return f"[Error] Agnes respondio {r.status_code}: {r.text[:200]}"
        data = r.json()
        if "data" not in data or not data["data"]:
            return "[Error] Respuesta sin imagen"
        item = data["data"][0]
        carpeta = "/root/Mi-primer-proyecto/backend/app/static/img/imagenes"
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, nombre_archivo)
        if item.get("b64_json"):
            with open(ruta, "wb") as f:
                f.write(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            img = httpx.get(item["url"], timeout=60)
            with open(ruta, "wb") as f:
                f.write(img.content)
        else:
            return "[Error] Formato de respuesta desconocido"
        return f"[OK] Imagen creada. URL publica: https://lens-portside-masses.ngrok-free.dev/img/imagenes/{nombre_archivo}"
    except Exception as e:
        return f"[Error] {str(e)[:200]}"

def generar_video(prompt, nombre_archivo=None):
    import os
    api_key = os.getenv("AGNES_API_KEY")
    base_url = os.getenv("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")
    modelo = os.getenv("AGNES_VIDEO_MODEL", "agnes-video-2.5-flash")
    if not api_key:
        return "[Error] AGNES_API_KEY no configurada"
    try:
        import httpx
        payload = {"model": modelo, "prompt": prompt, "mode": "t2v"}
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        r = httpx.post(f"{base_url}/videos", headers=headers, json=payload, timeout=300)
        if r.status_code != 200:
            return f"[Error] Agnes respondio {r.status_code}: {r.text[:200]}"
        data = r.json()
        if "data" not in data or not data["data"]:
            return "[Error] Respuesta sin video"
        item = data["data"][0]
        url = item.get("url")
        if not url:
            return "[Error] No se obtuvo URL del video"
        carpeta = "/root/Mi-primer-proyecto/backend/app/static/img/videos"
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, nombre_archivo)
        vid = httpx.get(url, timeout=180)
        with open(ruta, "wb") as f:
            f.write(vid.content)
            return f"[OK] Video creado. URL publica: /img/videos/{nombre_archivo}"
    except Exception as e:
        return f"[Error] {str(e)[:200]}"

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "generar_imagen",
        "description": "Genera una imagen a partir de una descripcion. Util para crear diagramas, ilustraciones y material visual educativo.",
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "Descripcion detallada de la imagen a generar"},
                "nombre_archivo": {"type": "string", "description": "Nombre del archivo (opcional, por defecto imagen_generada.png)"}
            },
            "required": ["prompt"]
        }
    }
})

TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "generar_video",
        "description": "Genera un video a partir de una descripcion. Util para crear material audiovisual educativo.",
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "Descripcion detallada del video a generar"},
                "nombre_archivo": {"type": "string", "description": "Nombre del archivo (opcional, por defecto video_generado.mp4)"}
            },
            "required": ["prompt"]
        }
    }
})
