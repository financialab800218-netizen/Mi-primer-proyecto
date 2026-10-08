import json
from pathlib import Path

SANDBOX_ROOT = Path("/data/data/com.termux/files/home/tutoria-cuba").resolve()
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
