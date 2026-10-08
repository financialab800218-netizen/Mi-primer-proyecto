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
    elif nombre == "escribir_archivo":
        return escribir_archivo(argumentos.get("ruta", ""), argumentos.get("contenido", ""))
    elif nombre == "crear_carpeta":
        return crear_carpeta(argumentos.get("ruta", ""))
    elif nombre == "git_status":
        return git_status()
    elif nombre == "git_commit_push":
        return git_commit_push(argumentos.get("mensaje", ""))
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
        return "[OK] Archivo escrito: " + ruta + " (" + str(len(contenido)) + " caracteres)"
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
