from contabilidad import supabase
import unicodedata
from almacenamiento import subir_archivo_a_nube
import os
from datetime import datetime
from docx import Document
from fpdf import FPDF
import PyPDF2

RUTA_DOCS = "/root/Mi-primer-proyecto/backend/app/static/docs"
URL_BASE = "https://lens-portside-masses.ngrok-free.dev/docs/"


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

def generar_pdf(texto: str, nombre_archivo: str):
    """Genera un archivo PDF a partir de un texto."""
    try:
        os.makedirs(RUTA_DOCS, exist_ok=True)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Codificar el texto para soportar caracteres latinos
        texto_encoded = texto.encode('latin-1', 'replace').decode('latin-1')
        
        for linea in texto_encoded.split('\n'):
            pdf.cell(200, 10, txt=linea, ln=True)
            
        if not nombre_archivo.endswith('.pdf'):
            nombre_archivo += '.pdf'
            
        ruta_completa = os.path.join(RUTA_DOCS, nombre_archivo)
        pdf.output(ruta_completa)
        
        url_nube = subir_archivo_a_nube(nombre_archivo, nombre_archivo)
        return f"PDF generado en la nube: {url_nube}"
    except Exception as e:
        return f"Error al generar PDF: {str(e)}"

def leer_documento(nombre_archivo: str):
    """Lee un archivo Word o PDF y devuelve su texto."""
    ruta_completa = os.path.join(RUTA_DOCS, nombre_archivo)
    
    if not os.path.exists(ruta_completa):
        return f"Error: El archivo {nombre_archivo} no existe."

    try:
        if nombre_archivo.endswith('.docx'):
            doc = Document(ruta_completa)
            texto = "\n".join([parrafo.text for parrafo in doc.paragraphs])
            return f"Contenido del documento:\n\n{texto}"
            
        elif nombre_archivo.endswith('.pdf'):
            with open(ruta_completa, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                texto = ""
                for pagina in reader.pages:
                    texto += pagina.extract_text() + "\n"
            return f"Contenido del PDF:\n\n{texto}"
            
        else:
            return "Error: Formato no soportado. Use .docx o .pdf."
    except Exception as e:
        return f"Error al leer documento: {str(e)}"
