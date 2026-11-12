from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from datetime import datetime
import os

def crear_expediente_harina_con_recetas():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    title = doc.add_heading('EXPEDIENTE TÉCNICO: HARINA DE PESCADO CONDIMENTADA', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'\nEntidad: PDL DESSPEZ / PDL AQUAPÓNICA\nFecha: {datetime.now().strftime("%d/%m/%Y")}\nDocumento Oficial para la Comisión de Precios')
    run.font.size = Pt(10)
    run.italic = True
    
    doc.add_heading('1. CARTA TECNOLÓGICA Y PROCESO OPERATIVO', level=1)
    doc.add_paragraph('A continuación se detallan los pasos técnicos para la elaboración de 1 kg de Harina de Pescado Condimentada:')
    
    pasos = [
        "Recepción y Lavado: Recibir el pescado fresco, verificar su estado organoléptico y lavarlo con agua potable.",
        "Cocción: Someter el pescado a cocción por vapor o agua caliente para coagular las proteínas.",
        "Prensado: Separar el líquido (agua y aceite) de la masa sólida utilizando una prensa mecánica.",
        "Secado: Extender la masa y secarla al sol o en horno a baja temperatura hasta alcanzar una humedad menor al 10%.",
        "Molienda: Triturar el pescado seco en un molino hasta obtener un polvo fino (harina base).",
        "Mezclado (Adición de Sazón): Incorporar el sazón completo en una proporción exacta del 5% (50 gramos por cada 1 kg de harina base).",
        "Empaque: Envasar en bolsas herméticas o pomos sellados de 250 gramos.",
        "Etiquetado: Colocar la etiqueta con fecha de producción, vencimiento (6 meses) y peso neto."
    ]
    
    for paso in pasos:
        doc.add_paragraph(paso, style='List Number')
        
    doc.add_heading('2. FICHA DE COSTOS Y TARIFAS', level=1)
    doc.add_paragraph('Cálculo basado en la Resolución 148/2023 del MFP, incluyendo materia prima (pescado entero a 250 CUP + transporte 100 CUP) y adición de sazón al 5%.')
    
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Fila'
    hdr_cells[1].text = 'Conceptos'
    hdr_cells[2].text = 'Importe (CUP)'
    
    datos = [
        ("1", "Gasto de Material (Pescado 4kg x 350 + Sazón 50g x 12,500)", "2,025.00"),
        ("2", "Salario directo (20.00 x 7.0 min)", "140.00"),
        ("3", "Otros gastos directos (Empaque + Etiqueta)", "30.00"),
        ("4", "Gastos asociados a producción (5%)", "109.75"),
        ("5", "COSTO TOTAL", "2,304.75"),
        ("6", "Gastos generales y admin. (5%)", "115.24"),
        ("7", "Gastos de distribución/ventas (3%)", "69.14"),
        ("8", "Gastos financieros", "0.00"),
        ("9", "Gastos tributarios (19%)", "26.60"),
        ("10", "SUBTOTAL DE COSTOS Y GASTOS", "2,515.73"),
        ("11", "Impuesto sobre ventas (10%)", "279.53"),
        ("12", "TOTAL DE COSTOS Y GASTOS", "2,795.26"),
        ("13", "Utilidad (10% ajustado)", "251.57"),
        ("14", "PRECIO DE VENTA FINAL (por kg)", "3,050.00"),
    ]
    
    for fila, concepto, importe in datos:
        row_cells = table.add_row().cells
        row_cells[0].text = fila
        row_cells[1].text = concepto
        row_cells[2].text = importe

    doc.add_page_break()
    doc.add_heading('3. ANEXO: INSTRUCTIVO DE USO Y RECETAS (ENVASE DE 250g)', level=1)
    doc.add_paragraph('Rendimiento del Envase: 1 envase de 250g rinde para preparar aproximadamente 8 litros de caldo o 4 comidas familiares.')
    
    doc.add_heading('Receta 1: Caldo Concentrado de Pescado (4 Raciones)', level=2)
    doc.add_paragraph('Porción de harina: 30 gramos (2 cucharadas soperas colmadas).\nRendimiento: 1 litro de caldo.\nPreparación: Disolver los 30g en agua tibia, agregar a la olla con 1 litro de agua y viandas. Hervir hasta que las viandas ablanden.')
    
    doc.add_heading('Receta 2: Arroz con Pescado a la Cubana (4 Raciones)', level=2)
    doc.add_paragraph('Porción de harina: 45 gramos (3 cucharadas soperas).\nRendimiento: 2 tazas de arroz cocido.\nPreparación: Sofreír cebolla, disolver los 45g en agua, añadir el arroz y cocinar hasta absorber.')
    
    doc.add_heading('Receta 3: Sopa de Pescado con Fideos (4 Raciones)', level=2)
    doc.add_paragraph('Porción de harina: 25 gramos (1.5 cucharadas soperas).\nRendimiento: 1.5 litros de sopa.\nPreparación: Hervir 1.5 litros de agua, agregar los 25g de harina disuelta, añadir fideos y cocinar por 10 minutos.')

    filename = "Expediente_Harina_Pescado_Recetas.docx"
    filepath = f"/root/Mi-primer-proyecto/backend/app/static/{filename}"
    doc.save(filepath)
    print(f"✅ Generado: https://lens-portside-masses.ngrok-free.dev/{filename}")

crear_expediente_harina_con_recetas()
