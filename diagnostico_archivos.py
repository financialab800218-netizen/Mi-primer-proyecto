import os

archivos = ['documentos.py', 'documentos_legales.py', 'herramientas_media.py', 'agentes_media.py', 'tools.py']

for archivo in archivos:
    ruta = f'/root/Mi-primer-proyecto/{archivo}'
    if os.path.exists(ruta):
        print(f"\n🔍 Revisando {archivo}:")
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                if "def " in linea:
                    print(f"   -> {linea.strip()}")
    else:
        print(f"\n⚠️ El archivo {archivo} no existe.")
