import re
import os
from datetime import datetime
from contabilidad import supabase

ruta_leg = '/root/Mi-primer-proyecto/documentos_legales.py'

with open(ruta_leg, 'r', encoding='utf-8') as f:
    codigo = f.read()

# Creamos la nueva función de Word usando el método oficial de Supabase Storage
nueva_funcion_word = '''
def generar_contrato_tcp(nombre, nivel, categoria, porcentaje, bono_base):
    try:
        from docx import Document
        
        # 1. Crear el documento Word
        doc = Document()
        doc.add_heading('CONTRATO DE TRABAJO - PROFESOR TCP', 0)
        doc.add_paragraph(f'Nombre: {nombre}')
        doc.add_paragraph(f'Nivel: {nivel}')
        doc.add_paragraph(f'Categoría: {categoria}')
        doc.add_paragraph(f'Porcentaje: {porcentaje}%')
        doc.add_paragraph(f'Bono Base: {bono_base} CUP')
        
        # 2. Guardar localmente
        nombre_archivo = f"contrato_{nombre.replace(' ', '_')}_{datetime.now().strftime('%H%M%S')}.docx"
        doc.save(nombre_archivo)
        
        # 3. Subir a Supabase Storage (Igual que el Excel)
        with open(nombre_archivo, 'rb') as f:
            supabase.storage.from_('Documentos').upload(nombre_archivo, f, file_options={"content-type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"})
            
        # 4. Obtener URL pública
        url = supabase.storage.from_('Documentos').get_public_url(nombre_archivo)
        
        # 5. Borrar local
        os.remove(nombre_archivo)
        
        return f"[OK] Contrato generado en la nube: {url}"
    except Exception as e:
        return f"[Error] Falló la generación/subida del contrato: {e}"
'''

# Reemplazamos la función vieja por la nueva
patron = r"def generar_contrato_tcp\(.*?\):.*?(?=\ndef |\Z)"
codigo = re.sub(patron, nueva_funcion_word, codigo, flags=re.DOTALL)

with open(ruta_leg, 'w', encoding='utf-8') as f:
    f.write(codigo)

print("✅ documentos_legales.py reparado con el método de Supabase Storage.")
